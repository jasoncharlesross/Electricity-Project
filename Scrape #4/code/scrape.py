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

def write_list_to_file(list, file):
    i = 0
    while i < len(list):
        file.write("\"" + list[i] + "\",")
        i += 1

def scrape(pipeline_names, dates1, dates2, dates4, dates6, error):
    # open browser
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
    driver.implicitly_wait(15)
    cookieAccept = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
    WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(cookieAccept))
    time.sleep(0.5)
    cookieAccept.click()

    pipeline_textbox = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/input")
    start_date = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/input")
    end_date =  driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/input")

    # Load pipeline names

    run_screen = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/button")
    criteria = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]")
    p = driver.current_window_handle

    for pipeline in pipeline_names:
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(pipeline_textbox))
        pipeline_textbox.clear()
        pipeline_textbox.send_keys(pipeline)

        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(start_date))
        start_date.clear()
        start_date.send_keys(dates1[0][0])

        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(end_date))
        end_date.clear()
        end_date.send_keys(dates1[0][1])
        
        num_results_element = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[10]/div[2]/div[4]/div[1]")

        time.sleep(2)

        # choose correct date granularity dependending on number of results
        num_results = num_results_element.text
        while num_results == "":
            time.sleep(0.5)
            num_results = num_results_element.text
        if ">" in num_results:
            dates = dates6
        else:
            num_results = int(num_results.replace(",", ""))
            if num_results > 210000:
                dates = dates6
            elif num_results > 105000:
                dates = dates4
            elif num_results > 52500:
                dates = dates2
            else:
                dates = dates1    
        
        j = 0
        for date in dates:

            driver.implicitly_wait(15)

            WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(start_date))
            start_date.clear()
            start_date.send_keys(date[0])

            WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(end_date))
            end_date.clear()
            end_date.send_keys(date[1])
            
            time.sleep(0.5)
            run_screen.click()

            # new stuff    

            num_results_element = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div/div/div/div[1]/div[2]/div[10]/div[2]/div[4]/div[1]")

            time.sleep(2)
            num_results = num_results_element.text
            while num_results == "":
                time.sleep(0.5)
                num_results = num_results_element.text
            if ">" in num_results:
                error.write("\"" +  str(pipeline) + "\",")
                write_list_to_file([date[0], date[1], "250000"], error)
                error.write("\"> 250000 entries (no downloads made past this one)\"\n")
                break
            else:
                num_results = int(num_results.replace(",", ""))
                if num_results > 65000:
                    error.write("\"" + str(pipeline) + "\",")
                    write_list_to_file([date[0], date[1], str(num_results)], error)
                    error.write("\"65000 < num_entries < 250000\"\n")
                    try:
                        criteria.click()
                        continue
                    except WebDriverException:
                        try:
                            time.sleep(5.0)
                            criteria.click()
                            continue
                        except WebDriverException:
                            try: 
                                time.sleep(5.0)
                                criteria.click()
                                continue
                            except WebDriverException:
                                try:
                                    time.sleep(7.0)
                                    criteria.click()
                                    continue
                                except WebDriverException:
                                    time.sleep(7.0)
                                    criteria.click()
                                    continue
                if num_results == 0:
                    error.write("\"" + str(pipeline) + "\",")
                    write_list_to_file([date[0], date[1], "0"], error)
                    error.write("\"0 entries\"\n")
                    try:
                        criteria.click()
                        continue
                    except WebDriverException:
                        try:
                            time.sleep(5.0)
                            criteria.click()
                            continue
                        except WebDriverException:
                            try: 
                                time.sleep(5.0)
                                criteria.click()
                                continue
                            except WebDriverException:
                                try:
                                    time.sleep(7.0)
                                    criteria.click()
                                    continue
                                except WebDriverException:
                                    time.sleep(7.0)
                                    criteria.click()
                                    continue

            # end new stuff
            
            driver.implicitly_wait(60)
            export = driver.find_element(By.XPATH, "//*[@id='applicationHost']/div/div[2]/div[2]/div[4]/div[16]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div/div/div[3]/div/button[1]")
            WebDriverWait(driver, 45).until(expected_conditions.element_to_be_clickable(export))
            time.sleep(1)
            export.click()

            try:
                driver.implicitly_wait(60)
                download = driver.find_element(By.CLASS_NAME, "downloadLink")
            except NoSuchElementException:
                try:
                    export.click()
                    driver.implicitly_wait(60)
                    download = driver.find_element(By.CLASS_NAME, "downloadLink")
                except:
                    error.write("\"" + str(pipeline) + "\",")
                    write_list_to_file([date[0], date[1], str(num_results)], error)
                    error.write("\"failed download\"\n")
                    criteria.click()
                    continue
            except TimeoutException:
                try:    
                    export.click()
                    driver.implicitly_wait(60)
                    download = driver.find_element(By.CLASS_NAME, "downloadLink")
                except:
                    error.write("\"" + str(pipeline) + "\",")
                    write_list_to_file([date[0], date[1], str(num_results)], error)
                    error.write("\"failed download\"\n")
                    criteria.click()
                    continue

            WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(download))
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
        j += 1
    time.sleep(5)
    driver.quit()