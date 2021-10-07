#!/usr/bin/env python
"""
Settings
"""
import os
from os.path import exists

__author__ = "Blake Dukes"
__version__ = "0.1.0"
__license__ = "MIT"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Root path, do not change!

FONT_PATH = os.path.join(ROOT_DIR, 'fonts/AlexBrush-Regular.ttf')
CLEANED_DATA_PATH = os.path.join(ROOT_DIR, 'Data_Cleaned/cleaned.csv')
if exists('Data_Raw/chat_history.json'):
    RAW_CHAT_HIST = os.path.join(ROOT_DIR, 'Data_Raw/chat_history.json')
else:
    RAW_CHAT_HIST = os.path.join(ROOT_DIR, 'Data_Raw/sample_chat_history.json')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    print('This is the settings file, modify this file to alter project variables.')
