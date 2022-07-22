# import packages
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

# import function definitions from elec.py
from elec import *

# adjust directory, file name as appropriate (temp.csv is test data, pipeline_names.csv is actual data)
with open('/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/temp.csv', newline = '') as f:
    reader = csv.reader(f)
    pipelineNames = list(reader)

# adjust directory as appropriate (can also make date ranges more granular, should data exceed download limit)
with open('/Users/jasonross/Desktop/Hortaçsu/Electricity-Project/dateCustom.csv', newline = '') as f:
    reader = csv.reader(f)
    dates = list(reader)  

scrape(pipelineNames, dates)