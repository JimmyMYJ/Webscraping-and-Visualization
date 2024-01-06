# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://ca.indeed.com/")

searchJob = driver.find_element(By.ID,"text-input-what")
searchJob.clear()
searchJob.send_keys("Programming")

searchArea = driver.find_element(By.ID,"text-input-where")
searchArea.clear()
searchArea.send_keys("Edmonton, AB" + Keys.ENTER)

jobTitle = []
maximumPages = 5
#for i in range(maximumPages):
time.sleep(3)

jobListings = driver.find_element(By.ID,"mosaic-provider-jobcards")
jobs = jobListings.find_elements(By.CLASS_NAME,"job_seen_beacon")




time.sleep(10)
driver.quit()