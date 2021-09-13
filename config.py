import os
class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_ECHO                = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY                     = 'p9Bv<3Eid9%$i01hdjkfhlsajkfl!@#$%^&*()!@#$%^*&^%$#@fdfk+_)(*&^%$#@'


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    def genURL(host, port, user, password):
        return user+':'+password+'@'+host+':'+port+'/'

    # extracting postgres credentials from environment
    postgresHost = os.environ['DB_POSTGRES_HOST']
    postgresPort = os.environ['DB_POSTGRES_PORT']
    postgresUserName = os.environ['POSTGRES_USER']
    postgresPassword = os.environ['POSTGRES_PASSWORD']


    # extracting maria credentials from environment
    mariaHost = os.environ['DB_MARIA_HOST']
    mariaPort = os.environ['DB_MARIA_PORT']
    mariaUserName = os.environ['DB_MARIA_USERNAME']
    mariaPassword = os.environ['DB_MARIA_PASSWORD']

    SQLALCHEMY_DATABASE_URI = 'postgresql://'+ genURL(postgresHost, postgresPort, postgresUserName, postgresPassword)+'portaldb'
    DEBUG                   = True
    SQLALCHEMY_BINDS        = {
            'maindb': 'mysql+pymysql://'+ genURL(mariaHost, mariaPort, mariaUserName, mariaPassword)+'gigdev',
            'geodb' : 'mysql+pymysql://'+ genURL(mariaHost, mariaPort, mariaUserName, mariaPassword)+'geodb',
            }
    ENV        = 'development'
    CACHE_TYPE = 'simple'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
      'development': DevelopmentConfig,
    # 'production' : ProductionConfig
}
