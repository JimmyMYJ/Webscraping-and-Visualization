# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from flask import Flask, request, render_template

from analyze import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')


def webscrape(keyword):
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://ca.indeed.com/")
    time.sleep(1)
    searchJob = driver.find_element(By.ID,"text-input-what")
    searchJob.clear()
    searchJob.send_keys(keyword)

    searchArea = driver.find_element(By.ID,"text-input-where") 
    time.sleep(1)
    number_of_characters = len(searchArea.get_attribute('value'))
    searchArea.send_keys(number_of_characters * Keys.BACKSPACE)
    searchArea.send_keys("Edmonton, AB" + Keys.ENTER )


    maximumPages = 1
    #for i in range(maximumPages):
    time.sleep(3)

    jobListings = driver.find_element(By.ID,"mosaic-jobResults")
    jobs = jobListings.find_elements(By.CLASS_NAME,"job_seen_beacon")
    job_num = 0
    job_desc = {}
    with open("result.txt",'w') as f:
        pass
    for job in jobs:
        jobTitles= (job.find_element(By.CLASS_NAME,"jobTitle").text)
        jobLinks=(job.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
        companyNames=(job.find_element(By.CSS_SELECTOR,"span[data-testid='company-name']").text)
        companyLocations=(job.find_element(By.CSS_SELECTOR,"div[data-testid='text-location']").text)
        conditions = job.find_elements(By.CSS_SELECTOR, "div[data-testid='attribute_snippet_testid']")
        jobCondition=([condition.text for condition in conditions])
        jobCondition = ','.join(jobCondition)
        jobButton = job.find_element(By.CLASS_NAME,"jobTitle")
        jobButton.click()
        time.sleep(1)
        jobDescription=(driver.find_element(By.ID,"jobDescriptionText").text)
        text = "Job Titles: "+jobTitles + "\n"+"Company Names: "+companyNames +"\n" \
            +"Company Location: "+companyLocations + "\n" +"Job Condition: "+jobCondition +"\n" +\
            "Job Description:" + "\n" + jobDescription+"\n\n"
        job_desc[job_num] = text
        job_num += 1

        with open("result.txt",'a') as f:
            f.write(text)
    return job_desc[0]




    time.sleep(1)
    driver.quit()

@app.route('/submit', methods=['POST'])
def submit():
    input_data = request.form["job_url"]
    # Process input_data in your Python script as needed
    # For now, let's just print it
    job = webscrape(input_data)
    result = get_response(job)
    return render_template('main.html', result=result)

app.run(debug=False)
