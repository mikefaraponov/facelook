import os

ROOT_PATH = os.path.dirname(__file__)

CASCADE_PATH = os.path.abspath(ROOT_PATH) + \
    '/haarcascade_frontalface_default.xml'

WHITELIST = ['png', 'jpeg']
