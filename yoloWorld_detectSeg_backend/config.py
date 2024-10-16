from datetime import timedelta

# 可以随便写 越长越安全解密越慢
SECRET_KEY = 'Flat-White'

# 访问令牌的过期时间为60分钟
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
# 刷新令牌的过期时间为30天
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '020627'
DATABASE = 'yanglao_order_sys'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
# 未配置邮箱账号以及授权码 如需使用请自行更改
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '3023538364@qq.com'
MAIL_PASSWORD = 'wmtbuaxfstwqdced'
MAIL_DEFAULT_SENDER = ("基于YOLO-World的目标检测及其分割管理平台", "3023538364@qq.com")
