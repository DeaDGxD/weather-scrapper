from selenium import webdriver
import time
from _time import human_time

while True:
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.google.com/search?q=tempature&oq=tempa&aqs=chrome.0.69i59j69i57.3083j0j1&sourceid=chrome&ie=UTF-8")
    print("Grabbing Temp")
    tempature = driver.find_element_by_xpath("""//*[@id="wob_tm"]""")
    print("Grabbing Rain")
    per = driver.find_element_by_xpath("""//*[@id="wob_pp"]""")
    print("Grabbing Humidity")
    hum = driver.find_element_by_xpath("""//*[@id="wob_hm"]""")
    print("Grabbing Wind")
    wind = driver.find_element_by_xpath("""//*[@id="wob_ws"]""")
    with open("temp.txt", "a") as t:
        t.write(f"Tempature: {tempature.text} Percipitation: {per.text} Humidity: {hum.text} Wind: {wind.text} {human_time()}\n")
    driver.close()
    time.sleep(300)
    continue


