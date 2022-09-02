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
from get_missing_obs import *

# adjust directory, file name as appropriate (temp.csv is test data, pipeline_names.csv is actual data)
with open('/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #3/input/missing_dates_fixed.csv', newline = '') as f:
    reader = csv.reader(f)
    input = list(reader)

error = open("/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #3/errors.csv", "w")

scrape(input[1:len(input)], error)