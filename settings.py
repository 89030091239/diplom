import os
from dotenv import load_dotenv

load_dotenv()
user_name_1 = os.environ.get('user_name_1')
user_name_2 = os.environ.get('user_name_2')
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
not_valid_phone = os.getenv('not_valid_phone')
not_valid_password = os.getenv('not_valid_password')
not_valid_email = os.getenv('not_valid_email')
not_valid_login = os.getenv('not_valid_login')
not_valid_acc_number = os.getenv('not_valid_acc_number')
not_correct_phone = os.getenv('not_correct_phone')
not_correct_email = os.getenv('not_correct_email')
special_characters = os.getenv('special_characters')
