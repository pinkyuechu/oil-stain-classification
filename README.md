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

* [在线演示](#在线演示)
* [Docker支持](#docker支持)
* [快速开始](#快速开始)
* [文档](#文档)
* [文件结构](#文件结构)
* [浏览器支持](#浏览器支持)
* [资源](#资源)
* [问题报告](#问题报告)
* [技术支持](#技术支持)
* [许可协议](#许可协议)
* [相关链接](#相关链接)

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

> Start the app in Docker

```bash
$ docker-compose pull   # download dependencies 
$ docker-compose build  # local set up
$ docker-compose up -d  # start the app 
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

## Quick start

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ # Get the code
$ git clone https://github.com/creativetimofficial/argon-dashboard-flask.git
$ cd argon-dashboard-flask
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Documentation
The documentation for the **Argon Dashboard Flask** is hosted at our [website](https://demos.creative-tim.com/argon-dashboard-flask/docs/1.0/getting-started/getting-started-flask.html).

<br />

## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- routes.py                 # Define authentication routes  
   |    |    |-- models.py                 # Defines models  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |    |    |-- includes/                 # HTML chunks and components
   |    |    |    |-- navigation.html      # Top menu component
   |    |    |    |-- sidebar.html         # Sidebar component
   |    |    |    |-- footer.html          # App Footer
   |    |    |    |-- scripts.html         # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt               # Production modules  - PostgreSql DMBS
   |
   |-- Dockerfile                           # Deployment
   |-- docker-compose.yml                   # Deployment
   |-- gunicorn-cfg.py                      # Deployment   
   |-- nginx                                # Deployment
   |    |-- appseed-app.conf                # Deployment 
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- `run.py` loads the `.env` file
- Initialize the app using the specified profile: *Debug* or *Production*
  - If env.DEBUG is set to *True* the SQLite storage is used
  - If env.DEBUG is set to *False* the specified DB driver is used (MySql, PostgreSQL)
- Call the app factory method `create_app` defined in app/__init__.py
- Redirect the guest users to Login page
- Unlock the pages served by *home* blueprint for authenticated users

<br />

## Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br />

## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

<br />

## Resources

- Demo: <https://www.creative-tim.com/live/argon-dashboard-flask>
- Download Page: <https://www.creative-tim.com/product/argon-dashboard-flask>
- Documentation: <https://demos.creative-tim.com/argon-dashboard-flask/docs/1.0/getting-started/getting-started-flask.html>
- License Agreement: <https://www.creative-tim.com/license>
- Support: <https://www.creative-tim.com/contact-us>
- Issues: [Github Issues Page](https://github.com/creativetimofficial/argon-dashboard-flask/issues)

<br />

## Reporting Issues

We use GitHub Issues as the official bug tracker for the **Argon Dashboard Flask**. Here are some advices for our users that want to report an issue:

1. Make sure that you are using the latest version of the **Argon Dashboard Flask**. Check the CHANGELOG from your dashboard on our [website](https://www.creative-tim.com/).
2. Providing us reproducible steps for the issue will shorten the time it takes for it to be fixed.
3. Some issues may be browser-specific, so specifying in what browser you encountered the issue might help.

<br />

## Technical Support or Questions

If you have questions or need help integrating the product please [contact us](https://www.creative-tim.com/contact-us) instead of opening an issue.

<br />

## Licensing

- Copyright 2019 - present [Creative Tim](https://www.creative-tim.com/)
- Licensed under [Creative Tim EULA](https://www.creative-tim.com/license)

<br />

## Useful Links

- [More products](https://www.creative-tim.com/bootstrap-themes) from Creative Tim
- [Tutorials](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w)
- [Freebies](https://www.creative-tim.com/bootstrap-themes/free) from Creative Tim
- [Affiliate Program](https://www.creative-tim.com/affiliates/new) (earn money)

<br />

## Social Media

- Twitter: <https://twitter.com/CreativeTim>
- Facebook: <https://www.facebook.com/CreativeTim>
- Dribbble: <https://dribbble.com/creativetim>
- Instagram: <https://www.instagram.com/CreativeTimOfficial>

<br />

---
[Argon Dashboard Flask](https://www.creative-tim.com/product/argon-dashboard-flask) - Provided by [Creative Tim](https://www.creative-tim.com/) and [AppSeed](https://appseed.us)
