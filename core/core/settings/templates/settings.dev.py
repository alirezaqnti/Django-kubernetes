# local settings sits here
#  such as logging
from dotenv import load_dotenv

load_dotenv()
import os


DEBUG = True
SECRET_KEY = str(os.getenv("SECRET_KEY"))
