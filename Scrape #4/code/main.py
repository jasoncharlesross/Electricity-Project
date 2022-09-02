# import packages
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# import function definitions from elec.py
from scrape import *

# adjust directory, file name as appropriate (temp.csv is test data, pipeline_names.csv is actual data)
with open('/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #4/input/pipeline_names.csv', newline = '') as f:
    reader = csv.reader(f)
    pipeline_names = list(reader)

with open('/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #4/input/dates_by_month.csv', newline = '') as f:
    reader = csv.reader(f)
    dates = list(reader)

error = open("/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #4/errors.csv", "w")

scrape(pipeline_names, dates, error)