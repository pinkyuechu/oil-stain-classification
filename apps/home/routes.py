# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask_login import login_required
from jinja2 import TemplateNotFound
from ultralytics import YOLO
from flask import  render_template,  redirect, flash,Flask, request, jsonify, send_from_directory
import os
import cv2
from werkzeug.utils import secure_filename
import shutil

app = Flask(__name__)
model = YOLO('best.pt')
folder_path = 'apps/static/results/predict'
app.config['UPLOAD_FOLDER'] = 'apps/static/uploads'
app.config['RESULT_FOLDER'] = 'apps/static/results'
app.secret_key = 'your_secret_key'


@blueprint.route('/api/upload_folder', methods=['POST'])
def upload_folder():
    uploaded_files = request.files.getlist('files[]')
    if not uploaded_files:
        return jsonify({'error': 'No files uploaded'}), 400

    # 创建一个新的上传子文件夹
    upload_subfolder_name = 'upload_session'
    upload_subfolder_path = os.path.join(app.config['UPLOAD_FOLDER'], upload_subfolder_name)
    if os.path.exists(upload_subfolder_path):
        shutil.rmtree(upload_subfolder_path)  # 如果文件夹已存在，先删除
    os.makedirs(upload_subfolder_path)

    # 创建一个新的结果文件夹
    result_folder_name = 'predict_results'
    result_folder_path = os.path.join(app.config['RESULT_FOLDER'], result_folder_name)
    if os.path.exists(result_folder_path):
        shutil.rmtree(result_folder_path)  # 如果文件夹已存在，先删除
    os.makedirs(result_folder_path)

    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_subfolder_path, filename)
        file.save(file_path)
        # 保存原始文件名和预测结果文件名
    original_filenames = [file.filename for file in uploaded_files]
    predicted_filenames = [f'predicted_{file.filename}' for file in uploaded_files]

    # 调用 folder_predict 函数进行预测
    folder_predict(upload_subfolder_path, result_folder_path)

    # 返回结果文件夹的路径
    return jsonify({
        'original_folder_path': upload_subfolder_path,
        'predicted_folder_path': result_folder_path,
        'original_filenames': original_filenames,
        'predicted_filenames': predicted_filenames
    })

@blueprint.route('/api/images_list', methods=['GET'])
def images_list():
    original_folder_path = os.path.join(app.config['UPLOAD_FOLDER'], 'upload_session')
    predicted_folder_path = os.path.join(app.config['RESULT_FOLDER'], 'predict_results')

    original_filenames = os.listdir(original_folder_path)
    predicted_filenames = os.listdir(predicted_folder_path)

    return jsonify({
        'original': original_filenames,
        'predicted': predicted_filenames
    })


@blueprint.route('/results/<path:filename>', methods=['GET'])
def get_result(filename):
    # 用于从 RESULT_FOLDER 提供文件
    return send_from_directory(app.config['RESULT_FOLDER'], filename)


def folder_predict(folder_path, result_folder_path):
    # 确保结果文件夹存在
    if not os.path.exists(result_folder_path):
        os.makedirs(result_folder_path)

    # 遍历文件夹中的所有图片文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # 使用YOLO模型进行预测
            results = model(image, conf=0.7)
            annotated_image = results[0].plot()

            # 保存带有预测结果的图片
            result_image_path = os.path.join(result_folder_path, f'{filename}')
            cv2.imwrite(result_image_path, annotated_image)

    # 返回结果文件夹的路径
    return result_folder_path


@blueprint.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        flash('没有文件部分')
        return redirect(request.url)
    video_file = request.files['video']
    if video_file.filename == '':
        flash('没有选择文件')
        return redirect(request.url)
    if video_file and allowed_file(video_file.filename):
        filename = secure_filename(video_file.filename)
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video_file.save(video_path)
        mode = request.form.get('mode')
        classes = [0, 1, 2, 6, 7, 8] if mode == '分类模式' else [3,4,5]
        output_path = video_predict(video_path, classes)   # 调用视频处理函数
        print(output_path)
        return jsonify({'filename': output_path})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'mp4', 'avi', 'mov', 'flv'}

def video_predict(video_path,classes = [3, 4, 5]):
    model = YOLO('best.pt')
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'x264')
    output_filename = os.path.basename(video_path)
    output_path = os.path.join(app.config['RESULT_FOLDER'], output_filename)
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height), True)
    while cap.isOpened():
        success, frame = cap.read()
        if success:
            results = model(frame, conf=0.7,classes=classes)
            annotated_frame = results[0].plot()
            out.write(annotated_frame)
        else:
            break
    cap.release()
    out.release()
    return output_filename  # 返回处理后的视频文件名
@blueprint.route('/api/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        app.logger.warning('No file part in the request')
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    desired_classes = [0, 1,2,6,7,8]
    model.predict(source=file_path, save=True, project=app.config['RESULT_FOLDER'],exist_ok=True,classes=desired_classes)
    results = model.predict(source=file_path,classes=[0,1,2,3,4,5,6,7,8])
    # 假设 results 是你的预测结果对象
    detections = []
    for r in results:
        for b in r.boxes:
            class_id =b.cls if isinstance(b.cls, int) else b.cls.item()
            class_name = r.names[class_id]
            confidence = b.conf if isinstance(b.conf, float) else b.conf.item()
            detections.append({
                'class_id': class_id,
                'class_name': class_name,
                'confidence': confidence

        })
    output_path = os.path.join('static/results/predict',  filename).replace('\\', '/')
    print(detections)
    return jsonify({
        'result_image_path': output_path,
        'detections': detections
    })
@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')



@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
