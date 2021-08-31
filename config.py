import hashlib
import os



mysql_host = "localhost"
mysql_password = "123456"
mysql_username = "root"
mysql_port = 3306
mysql_database = "sys"



class Config:
  DEBUG = False
  JSON_AS_ASCII = False
  SQLALCHEMY_DATABASE_URL = "mysql://root:123456@127.0.0.1:3306/sys"
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  MAX_CONTENT_LENGTH = 3*1024*1924
  PORT=5010
  basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class DevlopConfig(Config):
  DEBUG = True

class PrductConfig(Config):
  pass
