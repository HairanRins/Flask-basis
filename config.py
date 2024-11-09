import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'rins'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'rins'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'book_management'

