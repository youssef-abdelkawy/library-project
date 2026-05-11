import os

class Config:
    # السطر ده هو "الجوكر" اللي بيخلي الموقع يشم رابط الداتابيز في ريلواي أوتوماتيك
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    # تصحيح بسيط لأن ريلواي بيبدأ بـ postgres والكود محتاج postgresql
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key_here'
