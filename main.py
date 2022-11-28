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

#OBTENER AUDIO
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

#DESCARGAR VIDEO
def descargarvideo():
    link = 'https://www.youtube.com/watch?v=CepY-QYYAWY&ab_channel=ElMaii87'
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Intentando descargar video")
        youtubeObject.download()
    except:
        print("A ocurrido un error")
    print("Descarga completada satisfactoriamente")

    

#EDITAR VIDEO
def editarvideo():
    print("------------Editando Video------------")
    print()
    print("//////////////////////////////////////")
    print()
    print("------Adjuntando Audio con Video------")
    video = VideoFileClip("pruebavid.mp4")
    audio = AudioFileClip("audio2.mp3")
    video = video.set_audio(audio)
    video.write_videofile("vidconaudio.mp4")
    print()
    print("//////////////////////////////////////")
    print()
    print("--Modificando la velocidad del video--")
    # modificar la velocidad del video
    video = VideoFileClip("vidconaudio.mp4").fx(vfx.speedx, 0.90)
    video.write_videofile("velocidadcambiada.mp4")

    #agregar subtitulos a video

    #cortar video
    print()
    print("//////////////////////////////////////")
    print()
    print("------------Cortando Video------------")
    
    video = VideoFileClip("velocidadcambiada.mp4")

    cortado = video.subclip(1, 26)#el segundo 1 al 2 en este caso como prueba

    cortado.write_videofile("finalsubir.mp4")
    print()
    print("//////////////////////////////////////")
    print()
    print("-------Video Listo para subir---------")





#SUBIR VIDEO A TIKTOK
def subirtiktok():
    print("subir video a tiktok")
    print('Running bot now, get ready and login manually...')
    time.sleep(4)

    options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\josel\\AppData\\Local\\Google\\Chrome Beta\\User Data\\")##RUTA DEL PERFIL (CHROME VERSION)
    options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe" ##RUTA EJECUTABLE(CHROME VERSION)
    bot = webdriver.Chrome(options=options,  executable_path=CM().install())
    bot.set_window_size(1680, 900)


    bot.get('https://www.tiktok.com/upload/?lang=en')


    def check_exists_by_xpath(driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False

        return True


    def upload(video_path):
        while True:
            file_uploader = bot.find_element_by_xpath(
                '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/input')

            file_uploader.send_keys(video_path)

            caption = bot.find_element_by_xpath(
                '//*[@id="main"]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span')

            bot.implicitly_wait(10)
            ActionChains(bot).move_to_element(caption).click(
                caption).perform()
            # ActionChains(bot).key_down(Keys.CONTROL).send_keys(
            #     'v').key_up(Keys.CONTROL).perform()

            with open(r"caption.txt", "r") as f:
                tags = [line.strip() for line in f]

            for tag in tags:
                ActionChains(bot).send_keys(tag).perform()
                time.sleep(2)
                ActionChains(bot).send_keys(Keys.RETURN).perform()
                time.sleep(1)

            time.sleep(5)
            bot.execute_script("window.scrollTo(150, 300);")
            time.sleep(5)

            post = WebDriverWait(bot, 100).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div[5]/button[2]')))

            post.click()
            time.sleep(30)

            if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
                reupload = WebDriverWait(bot, 100).until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="portal-container"]/div/div/div[1]/div[2]')))

                reupload.click()
            else:
                print('Unknown error cooldown')
                while True:
                    time.sleep(600)
                    post.click()
                    time.sleep(15)
                    if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
                        break

            if check_exists_by_xpath(bot, '//*[@id="portal-container"]/div/div/div[1]/div[2]'):
                reupload = WebDriverWait(bot, 100).until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="portal-container"]/div/div/div[1]/div[2]')))
                reupload.click()

            time.sleep(1)

    # ================================================================
    # Here is the path of the video that you want to upload in tiktok.
    upload(r"C:\\Users\\josel\Desktop\\python\\finalsubir.mp4")
    # ================================================================

#CRONJOB
def automatizacion():
    print("I'm working... inicia aqui")
    obteneraudio()
    print("audio obtenido")
    descargarvideo()
    print("video descargado")
    editarvideo()
    print("video editado")
    subirtiktok()
    print("video subido a tiktok")
    

# Path: time.py
# hacer que un programa aplique un codigo a las 8 pm

schedule.every().day.at("8:00").do(automatizacion) #hacer que un programa aplique un codigo a las 8 am
while True:
    schedule.run_pending()
    time.sleep(1)

#automatizacion() # PROBAR CODIGO SIN EL HORARIO
