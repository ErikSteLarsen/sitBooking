from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import time



def bookTrening(tid):
    brukernavn = "X"
    passord = "X"


    driver = webdriver.Chrome()

    driver.get("https://www.sit.no/trening/treneselv")
    driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/div/div[2]/p[2]/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/section/div[3]/div/div/div/div/div[1]/div/form/div/div[1]/div/div[1]/a").click()
    #driver.get("https://auth.dataporten.no/discovery?returnTo=https%3A%2F%2Fauth.dataporten.no%2Foauth%2Fauthorization%3Fclient_id%3D93ae97a1-5633-45ac-92a0-86ba891aec02%26redirect_uri%3Dhttps%253A%252F%252Fwww.sit.no%252Foauth%252Fauthorized2%252F1%26response_type%3Dcode%26scope%3Demail%2520longterm%2520peoplesearch%2520profile%2520userid%2520userid-feide%2520userinfo%2520groups%2520phone&clientid=93ae97a1-5633-45ac-92a0-86ba891aec02")


    # Login to the website
    orgInput = driver.find_element_by_id("org-chooser-selectized")
    orgInput.send_keys("NTNU", Keys.RETURN)
    orgInput.submit()

    driver.find_element_by_id("username").send_keys(brukernavn)
    driver.find_element_by_id("password").send_keys(passord)
    driver.find_element_by_xpath("//button[@type='submit']").click()



    driver.get("https://www.sit.no/trening/treneselv")
    time.sleep(3)
    driver.switch_to.frame("ibooking-iframe")
    x = driver.find_elements_by_xpath("//button[@class='active']")

    while not x:
        driver.get("https://www.sit.no/trening/treneselv")
        time.sleep(3)
        driver.switch_to.frame("ibooking-iframe")
        x = driver.find_elements_by_xpath("//button[@class='active']")

    for element in x[1:5]:
        element.click()

    om2dager = driver.find_elements_by_class_name("day")[2]
    tider = om2dager.find_elements_by_xpath(".//p[@class='time']")

    for knapp in tider:
        if knapp.text == tid:
            knapp.click()
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div/div[3]/div[8]/button[1]").click()



# Sjekk om tiden IRL faktisk er det den må være først
while True:
    if time.localtime()[3] == 14 and time.localtime()[4] == 0 and time.localtime()[5] < 10:
        bookTrening("14.00–15.00")
    else:
        print(time.localtime()[3], 14)
        print(time.localtime()[4], 0)
        print(time.localtime()[5] < 20)

    if time.localtime()[3] == 15 and time.localtime()[4] == 0 and time.localtime()[5] < 10:
        bookTrening("15.00–16.00")

    if time.localtime()[3] == 16 and time.localtime()[4] == 0 and time.localtime()[5] < 10:
        bookTrening("16.00–17.00")
    time.sleep(1)