import os

# DATABASE ENV IMPORTS
DB_HOST=os.getenv('DB_HOST')
DB_USERNAME=os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
DB_PORT=os.getenv('DB_PORT')

# 
SECRET_KEY=os.getenv('SECRET_KEY')
DEBUG=bool(os.getenv('DEBUG'))
if DEBUG:
    ALLOWED_HOSTS=os.getenv('ALLOWED_HOSTS')
