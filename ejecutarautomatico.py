# Path: time.py
# hacer que un programa aplique un codigo a las 8 pm

schedule.every().day.at("8:00").do(automatizacion) #hacer que un programa aplique un codigo a las 8 am
while True:
    schedule.run_pending()
    time.sleep(1)
