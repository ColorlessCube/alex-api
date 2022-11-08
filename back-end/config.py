import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask参数，用于安全签署会话cookie的密钥，并可用于扩展应用程序的任何其他安全相关需求。它应该是一个长随机字符串
    SECRET_KEY = 'hard to guess string'
    # Flask参数，提供页面服务时，浏览器上文件的缓存时间，如果是None，则浏览器不会缓存页面文件，datetime.timedelta/秒数
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(hours=16)
    # Flask参数，采用session实现用户登录管理时，session的过期时间，datetime.timedelta/秒数
    PERMANENT_SESSION_LIFETIME = timedelta(hours=16)
    # Flask-Login参数，选中保持登录/记住我时，cookie的过期时间，datetime.timedelta/秒数
    REMEMBER_COOKIE_DURATION = timedelta(days=30)

    # 采用token管理用户登录时，token的名字，用于从header中获取对应的token值
    APP_TOKEN_AUTHORIZATION = 'Authorization'
    # 采用token管理用户登录时，token的过期时间
    APP_TOKEN_EXPIRES_IN = int(timedelta(hours=16).total_seconds())

    # 系统日志相关配置
    FLASKZ_LOGGER_FILENAME = None
    FLASKZ_LOGGER_FILEPATH = os.path.join(os.getcwd(), './syslog')
    FLASKZ_LOGGER_LEVEL = 'INFO'  # 'DEBUG'/'INFO'/'WARNING'/'WARN'/'ERROR'/'FATAL'/'CRITICAL'
    FLASKZ_LOGGER_FORMAT = '%(asctime)s %(filename)16s[line:%(lineno)-3d] %(levelname)8s: \n%(message)s\n'
    FLASKZ_LOGGER_WHEN = 'midnight'  # 每天midnight，将当日志文件按日期重命名保存，并生成一个新的日志文件
    FLASKZ_LOGGER_BACKUP_COUNT = 90
    FLASKZ_LOGGER_DISABLED = False
    FLASKZ_WZ_LOGGER_DISABLED = True

    # 请求响应相关配置
    FLASKZ_RES_SUCCESS_STATUS = "success"
    FLASKZ_RES_FAIL_STATUS = "fail"

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    HASS_BASE_URL = ''
    HASS_TOKEN = ''
    HASS_DEFAULT_HEADERS = {
        'Authorization': 'Bearer ' + HASS_TOKEN,
        'Content-Type': 'application/json'
    }


config = {
    'production': ProductionConfig,

    'default': ProductionConfig
    # 'default': DevelopmentConfig
}
