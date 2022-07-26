# import packages
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

# import function definitions from checkmissing.py
from checkmissing import *

# adjust directory, file name as appropriate (temp.csv is test data, pipeline_names.csv is actual data)
with open('/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #1/missing.csv', newline = '') as f:
    reader = csv.reader(f)
    pipelineNames = list(reader)

# adjust directory as appropriate (can also make date ranges more granular, should data exceed download limit)
with open('/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #1/dateCustom.csv', newline = '') as f:
    reader = csv.reader(f)
    dates = list(reader)  

scrape(pipelineNames, dates)