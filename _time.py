import time


def human_time():
    car = time.localtime()
    stuff = f"{car[3]}:{car[4]}  {car[1]}/{car[2]}"
    return stuff

