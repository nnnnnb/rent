# rent
# 1、创建项目
django-admin startproject 项目名称

# 2、创建应用
python3 manage.py startapp 应用名

# 3、启动服务器
python3 manage.py runserver

# 4、创建管理员
python3 manage.py createsuperuser

# LANGUAGE_CODE = 'zh-hans' #使用中国语言
# TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间


python3 manage.py makemigrations
python3 manage.py migrate

apps __init__.py
import pymysql
pymysql.install_as_MySQLdb()


mysql -uroot -p myproject < myproject/apply_block.sql;



上传图片：
	# settings.py
	MEDIA_ROOT = BASE_DIR    #os.path.join(BASE_DIR, 'media')
	MEDIA_URL = '/media/'
