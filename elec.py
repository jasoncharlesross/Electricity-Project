import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

def scrape(pipelineNames, dates):
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://platform.spgi.spglobal.com/web/Login?auth=inherit&bmctx=431A16D7B69544E3000D3C27B5817697&enablePersistentLogin=true&OAUTH_SSO_ENC_KEY=C57DBB5C08DA42B6E90C86AF0C895A9B1C0828BB0FD48E2881852858161950DE&password=secure_string&contextType=external&IS_OAUTH_OAM_SSO_LINK_ENABLED=true&OAUTH_SSO_ID_DOMAIN=SPGLBDomain&IS_OAUTH_USER_ASSERTION_ENABLED=true&contextValue=%2foam&env=WAM12C&SwitchGetToPostLimit=50000&username=string&challenge_url=https%3a%2f%2fplatform.spgi.spglobal.com%2fweb%2fclient%3fauth%3dinherit%23security%2flogin&request_id=3830297398968941193&authn_try_count=0&locale=en_US&resource_url=https%253A%252F%252Fwww.capitaliq.spglobal.com%252FSNL.Services.Application.Common.Service%252Fv1%252Fclient%252Flanding#/")
    driver.implicitly_wait(5)

    # login 
    username = driver.find_element(By.NAME, "username").send_keys("jasonross@uchicago.edu")
    time.sleep(0.5)
    password =  driver.find_element(By.NAME, "password").send_keys("gyvfen-wujCe4-newxun")
    login = driver.find_element(By.XPATH, "//*[@id='login-mfe-container']/div/div/div/main/div/div/div/form/div[4]/div[1]/button").click()

    # navigate to correct site, dismiss pop-up messages
    time.sleep(5)
    driver.get("https://www.capitaliq.spglobal.com/web/client?auth=inherit#office/screener?perspective=241019")
    driver.implicitly_wait(30)
    cookieAccept = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()

    textbox = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/input")
    startDate = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/input")
    endDate =  driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/input")

    # Load pipeline names

    runScreen = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/button")
    criteria = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]")
    p = driver.current_window_handle

    for pipeline in pipelineNames:
        nullPipelineCounter = 0
        driver.implicitly_wait(15)
        textbox.clear()
        textbox.send_keys(pipeline)
        for date in dates:
            if nullPipelineCounter >= 12:
                print(pipeline, " HAS NO ENTRIES")
                break
            driver.implicitly_wait(15)
            WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(endDate))
            endDate.clear()
            endDate.send_keys(date[1])
            WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(startDate))
            startDate.clear()
            startDate.send_keys(date[0])
            runScreen.click()
            # dismiss new user guide pop ups (first subiteration of first iteration only)
            if pipeline == pipelineNames[0] and date == dates[0]:
                driver.implicitly_wait(60)
                next1 = driver.find_element(By.XPATH, "//*[@id='walkme-balloon-6823803']/div/div[1]/div[4]/div[2]/div/button")
                WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(next1))
                next1.click()
            # determine whether export link is available (would be unavailable if zero data to export)
            # if no export link is available, abandon this iteration of the loop
            try:
                driver.implicitly_wait(60)
                export = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div/div/div[3]/div/button[1]")
                WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable(export))
                time.sleep(1)
                export.click()
            except ElementNotInteractableException:
                nullPipelineCounter += 1
                WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(criteria))
                criteria.click()
                continue
            except TimeoutException or WebDriverException:
                nullPipelineCounter += 1
                WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(criteria))
                criteria.click()
                continue
            except NoSuchElementException:
                nullPipelineCounter += 1
                WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(criteria)) 
                criteria.click()
                continue
            else:
                nullPipelineCounter = 0
                # determine whether download link is available (would be unavailable if too much data to export)
                # if no download link is available, break this iteration of the loop (and report to terminal)
                try:
                    driver.implicitly_wait(80)
                    download = driver.find_element(By.CLASS_NAME, "downloadLink")
                except:
                    criteria.click()
                    print(pipeline, " HAS TOO MANY ENTRIES")
                    break
                else:
                    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(download))
                    time.sleep(0.5)
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

    time.sleep(30)
    driver.quit()