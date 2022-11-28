import os
import moviepy 
from moviepy.editor import *

#poner el video en la carpeta del proyecto y con el nombre del video
video = VideoFileClip("Parkour en minecraft 118 ✅ sin hablar ✅.mp4")




# editar video por cantidad de segundosrimer intervalo desde el segundo en que queremos cortar hasta donde deseamos cortar
video = VideoFileClip("video_ejemplo.mp4")
cortado = video.subclip(1, 25)#el segundo 1 al 2 en este caso como prueba
cortado.write_videofile("cortado.mp4")

# cambiar dimensiones del video para que encaje con la api de tik tok
video = VideoFileClip("video_ejemplo.mp4")
reducido = video.resize(width=720).write_videofile("reducido.mp4")
reducido.write_videofile("resultado.mp4")

#ver tamaño del videoq
video = VideoFileClip("video_ejemplo.mp4")
print(video.size)
