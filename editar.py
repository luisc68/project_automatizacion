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