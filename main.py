#IMPORTACIONES DE LIBRERIAS
import pyttsx3
import docx2txt
from pytube import YouTube
import download
import os
import moviepy
from moviepy.editor import *

import time
import schedule
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

def obteneraudio():
    
    print("------------Obtener Audio-------------")
    print()
    print("//////////////////////////////////////")
    print()
    print("------Convirtiendo Texto a Audio------")
    engine = pyttsx3.init()
    #Leer archivo de word
    my_text = docx2txt.process("text.docx")
    #Guardar audio
    engine.save_to_file(my_text, 'audio2.mp3')
    engine.runAndWait()
    print()
    print("--------------Audio Listo-------------")
    print()