# Argon Dashboard Flask [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/home?status=Material%20Dashboard,%20a%20free%20Material%20Bootstrap%204%20Admin%20Template%20%E2%9D%A4%EF%B8%8F%20https%3A//bit.ly/2Lyat1Y%20%23bootstrap%20%23material%20%23design%20%23developers%20%23freebie%20%20via%20%40CreativeTim)

![版本](https://img.shields.io/badge/version-1.0.1-blue.svg) [![GitHub未解决问题](https://img.shields.io/github/issues/creativetimofficial/argon-dashboard-flask.svg?maxAge=2592000)](https://github.com/creativetimofficial/argon-dashboard-flask/issues?q=is%3Aopen+is%3Aissue) [![GitHub已关闭问题](https://img.shields.io/github/issues-closed-raw/creativetimofficial/argon-dashboard-flask.svg?maxAge=2592000)](https://github.com/creativetimofficial/argon-dashboard-flask/issues?q=is%3Aissue+is%3Aclosed)

![Argon Dashboard Flask界面演示](https://github.com/creativetimofficial/argon-dashboard-flask/blob/master/media/argon-dashboard-flask-intro.gif)

<br />

> 免费开源的 **Flask仪表盘** 项目 - 主要功能：

- 最新依赖项：**Flask 2.0.1**
- 通过 **Gulp** 编译SCSS
- UI组件库：**Argon Dashboard**（免费版）由 **[Creative-Tim](https://www.creative-tim.com/)** 提供
- Flask代码架构由 **[AppSeed](https://appseed.us/)** 构建
- 支持 SQLite/PostgreSQL 数据库
- 使用 SQLAlchemy ORM
- Alembic 数据库迁移
- 模块化蓝图设计
- 基于会话的认证系统（flask_login）
- 表单验证
- 部署配置（Docker, Gunicorn/Nginx, Heroku）

<br />

## 目录

- [Argon Dashboard Flask ](#argon-dashboard-flask-)
  - [目录](#目录)
  - [在线演示](#在线演示)
  - [Docker支持](#docker支持)
  - [快速开始](#快速开始)
  - [文档](#文档)
  - [文件结构](#文件结构)
  - [重新编译CSS](#重新编译css)
  - [浏览器支持](#浏览器支持)
  - [资源](#资源)
  - [问题报告](#问题报告)
  - [技术支持或问题咨询](#技术支持或问题咨询)
  - [许可](#许可)
  - [有用的链接](#有用的链接)
  - [社交媒体](#社交媒体)

<br />

## 在线演示

> 使用默认凭证 ***test / pass*** 登录或访问[注册页面](https://www.creative-tim.com/live/argon-dashboard-flask)创建新用户。

- **Argon Dashboard Flask** [登录页面](https://www.creative-tim.com/live/argon-dashboard-flask)

<br />

## Docker支持

> 获取代码

```bash
$ git clone https://github.com/app-generator/argon-dashboard-flask.git
$ cd argon-dashboard-flask
```

> 在Docker中启动应用

```bash
$ docker-compose pull   # 下载依赖项
$ docker-compose build  # 本地设置
$ docker-compose up -d  # 启动应用
```

在浏览器中访问 `http://localhost:85`。应用应该已经启动并运行。

<br />

## 快速开始

> 解压源码或克隆私有仓库。获取代码后，打开终端并导航到包含产品源代码的工作目录。

```bash
$ # 获取代码
$ git clone https://github.com/creativetimofficial/argon-dashboard-flask.git
$ cd argon-dashboard-flask
$
$ # 虚拟环境模块安装（基于Unix的系统）
$ virtualenv env
$ source env/bin/activate
$
$ # 虚拟环境模块安装（基于Windows的系统）
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # 安装模块 - SQLite数据库
$ pip3 install -r requirements.txt
$
$ # 或者使用PostgreSQL连接器
$ # pip install -r requirements-pgsql.txt
$
$ # 设置FLASK_APP环境变量
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # 设置DEBUG环境
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # 启动应用（开发模式）
$ # --host=0.0.0.0 - 在所有网络接口上暴露应用（默认127.0.0.1）
$ # --port=5000    - 指定应用端口（默认5000）  
$ flask run --host=0.0.0.0 --port=5000
$
$ # 在浏览器中访问仪表盘：http://127.0.0.1:5000/
```

> 注意：要使用该应用，请访问注册页面并创建新用户。认证后，应用将解锁私有页面。

<br />

## 文档
**Argon Dashboard Flask** 的文档托管在我们的 [网站](https://demos.creative-tim.com/argon-dashboard-flask/docs/1.0/getting-started/getting-started-flask.html) 上。

<br />

## 文件结构
在下载的文件中，您会找到以下目录和文件：

```bash
< 项目根目录 >
   |
   |-- apps/
   |    |
   |    |-- home/                          # 一个简单的应用，用于提供HTML文件
   |    |    |-- routes.py                 # 定义应用路由
   |    |
   |    |-- authentication/                # 处理认证路由（登录和注册）
   |    |    |-- routes.py                 # 定义认证路由  
   |    |    |-- models.py                 # 定义模型  
   |    |    |-- forms.py                  # 定义认证表单（登录和注册） 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS文件、Javascript文件
   |    |
   |    |-- templates/                     # 用于渲染页面的模板
   |    |    |-- includes/                 # HTML片段和组件
   |    |    |    |-- navigation.html      # 顶部菜单组件
   |    |    |    |-- sidebar.html         # 侧边栏组件
   |    |    |    |-- footer.html          # 应用页脚
   |    |    |    |-- scripts.html         # 所有页面通用的脚本
   |    |    |
   |    |    |-- layouts/                   # 主页面
   |    |    |    |-- base-fullscreen.html  # 认证页面使用
   |    |    |    |-- base.html             # 普通页面使用
   |    |    |
   |    |    |-- accounts/                  # 认证页面
   |    |    |    |-- login.html            # 登录页面
   |    |    |    |-- register.html         # 注册页面
   |    |    |
   |    |    |-- home/                      # UI套件页面
   |    |         |-- index.html            # 首页
   |    |         |-- 404-page.html         # 404页面
   |    |         |-- *.html                # 所有其他页面
   |    |    
   |  config.py                             # 设置应用
   |    __init__.py                         # 初始化应用
   |
   |-- requirements.txt                     # 开发模块 - SQLite存储
   |-- requirements-mysql.txt               # 生产模块  - Mysql数据库管理系统
   |-- requirements-pqsql.txt               # 生产模块  - PostgreSql数据库管理系统
   |
   |-- Dockerfile                           # 部署
   |-- docker-compose.yml                   # 部署
   |-- gunicorn-cfg.py                      # 部署   
   |-- nginx                                # 部署
   |    |-- appseed-app.conf                # 部署 
   |
   |-- .env                                 # 通过环境注入配置
   |-- run.py                               # 启动应用 - WSGI网关
   |
   |-- ************************************************************************
```

<br />

> 启动流程

- `run.py` 加载 `.env` 文件
- 使用指定的配置文件初始化应用：*Debug* 或 *Production*
  - 如果 `env.DEBUG` 设置为 *True*，则使用SQLite存储
  - 如果 `env.DEBUG` 设置为 *False*，则使用指定的数据库驱动（MySql, PostgreSQL）
- 调用在 `app/__init__.py` 中定义的应用工厂方法 `create_app`
- 将访客用户重定向到登录页面
- 为认证用户解锁由 *home* 蓝图提供的页面

<br />

## 重新编译CSS
要重新编译SCSS文件，请按照以下设置进行操作：

<br />

**步骤 #1** - 安装工具

- [NodeJS](https://nodejs.org/en/) 12.x 或更高版本
- [Gulp](https://gulpjs.com/) - 全局安装 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/)（可选） 

<br />

**步骤 #2** - 将工作目录更改为 `assets` 文件夹

```bash
$ cd apps/static/assets
```

<br />

**步骤 #3** - 安装模块（这将创建一个经典的 `node_modules` 目录）

```bash
$ npm install
// 或者
$ yarn
```

<br />

**步骤 #4** - 编辑并重新编译SCSS文件 

```bash
$ gulp scss
```

生成的文件将保存在 `static/assets/css` 目录中。

<br />

## 浏览器支持
目前，我们官方支持以下浏览器的最后两个版本：

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

<br />

## 资源

- 演示：<https://www.creative-tim.com/live/argon-dashboard-flask>
- 下载页面：<https://www.creative-tim.com/product/argon-dashboard-flask>
- 文档：<https://demos.creative-tim.com/argon-dashboard-flask/docs/1.0/getting-started/getting-started-flask.html>
- 许可协议：<https://www.creative-tim.com/license>
- 支持：<https://www.creative-tim.com/contact-us>
- 问题：[Github问题页面](https://github.com/creativetimofficial/argon-dashboard-flask/issues)

<br />

## 问题报告
我们使用GitHub问题作为 **Argon Dashboard Flask** 的官方错误跟踪器。以下是一些建议，供想要报告问题的用户参考：

1. 确保您使用的是 **Argon Dashboard Flask** 的最新版本。请在我们的 [网站](https://www.creative-tim.com/) 上查看您的仪表盘的更新日志。
2. 为我们提供可重现问题的步骤，这将缩短问题修复的时间。
3. 有些问题可能是特定于浏览器的，因此指定您遇到问题的浏览器可能会有所帮助。

<br />

## 技术支持或问题咨询
如果您有问题或需要帮助集成产品，请 [联系我们](https://www.creative-tim.com/contact-us)，而不是打开一个问题。

<br />

## 许可
- 版权所有 2019 - 至今 [Creative Tim](https://www.creative-tim.com/)
- 根据 [Creative Tim最终用户许可协议](https://www.creative-tim.com/license) 许可

<br />

## 有用的链接

- [Creative Tim的更多产品](https://www.creative-tim.com/bootstrap-themes)
- [教程](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w)
- [Creative Tim的免费资源](https://www.creative-tim.com/bootstrap-themes/free)
- [联盟计划](https://www.creative-tim.com/affiliates/new)（赚取收入）

<br />

## 社交媒体

- 推特：<https://twitter.com/CreativeTim>
- 脸书：<https://www.facebook.com/CreativeTim>
- Dribbble：<https://dribbble.com/creativetim>
- 照片墙：<https://www.instagram.com/CreativeTimOfficial>

<br />

---
[Argon Dashboard Flask](https://www.creative-tim.com/product/argon-dashboard-flask) - 由 [Creative Tim](https://www.creative-tim.com/) 和 [AppSeed](https://appseed.us) 提供