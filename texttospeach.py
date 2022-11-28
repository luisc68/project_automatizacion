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
