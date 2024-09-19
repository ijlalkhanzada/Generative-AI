import os

# Secret key for session management
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')

# MySQL database configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'yourpassword')
MYSQL_DB = 'login_system'
MYSQL_CURSORCLASS = 'DictCursor'
