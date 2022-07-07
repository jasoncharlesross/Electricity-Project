import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Safari()
action = ActionChains(driver)
driver.maximize_window()
driver.get("https://platform.spgi.spglobal.com/web/Login?auth=inherit&bmctx=431A16D7B69544E3000D3C27B5817697&enablePersistentLogin=true&OAUTH_SSO_ENC_KEY=C57DBB5C08DA42B6E90C86AF0C895A9B1C0828BB0FD48E2881852858161950DE&password=secure_string&contextType=external&IS_OAUTH_OAM_SSO_LINK_ENABLED=true&OAUTH_SSO_ID_DOMAIN=SPGLBDomain&IS_OAUTH_USER_ASSERTION_ENABLED=true&contextValue=%2foam&env=WAM12C&SwitchGetToPostLimit=50000&username=string&challenge_url=https%3a%2f%2fplatform.spgi.spglobal.com%2fweb%2fclient%3fauth%3dinherit%23security%2flogin&request_id=3830297398968941193&authn_try_count=0&locale=en_US&resource_url=https%253A%252F%252Fwww.capitaliq.spglobal.com%252FSNL.Services.Application.Common.Service%252Fv1%252Fclient%252Flanding#/")
driver.implicitly_wait(5)

# login
username = driver.find_element(By.NAME, "username").send_keys("jasonross@uchicago.edu")
password =  driver.find_element(By.NAME, "password").send_keys("gyvfen-wujCe4-newxun")
login = driver.find_element(By.XPATH, "//*[@id='login-mfe-container']/div/div/div/main/div/div/div/form/div[4]/div[1]/button").click()

# navigate to correct site, dismiss pop-up messages
time.sleep(5)
driver.get("https://www.capitaliq.spglobal.com/web/client?auth=inherit#office/screener?perspective=241019")
driver.implicitly_wait(10)
cookieAccept = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
next1 = driver.find_element(By.XPATH, "//*[@id='walkme-balloon-6823803']/div/div[1]/div[4]/div[2]/div/button").click()
next2 =  driver.find_element(By.XPATH, "//*[@id='walkme-balloon-3054154']/div/div[1]/div[4]/div[2]/div/button").click()

textbox = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/input")
startDate = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/input")
endDate =  driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/input")

# Load pipeline names

runScreen = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/button")
criteria = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]")
p = driver.current_window_handle

with open('/Users/jasonross/Desktop/Hortaçsu/Electricity/temp.csv', newline = '') as f:
    reader = csv.reader(f)
    pipelineNames = list(reader)

with open('/Users/jasonross/Desktop/Hortaçsu/Electricity/dates.csv', newline = '') as f:
    reader = csv.reader(f)
    dates = list(reader)  

for pipeline in pipelineNames:
    for date in dates:
        driver.implicitly_wait(15)
        textbox.clear()
        textbox.send_keys(pipeline)
        startDate.clear()
        startDate.send_keys(date[0])
        endDate.clear()
        endDate.send_keys(date[1])
        runScreen.click()
        driver.implicitly_wait(60)
        export = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div/div/div[3]/div/button[1]")
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(export))
        export.click()
        driver.implicitly_wait(60)
        download = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[2]/a")
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(download))
        download.click()
        time.sleep(2)
        chwd = driver.window_handles
        for w in chwd:
            if (w != p):
                driver.switch_to.window(w)
                break
        driver.close()
        driver.switch_to.window(p)
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(criteria))
        criteria.click()