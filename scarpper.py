from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()#/usr/local/bin
url = "https://teams.microsoft.com/"
browser.get(url)


# path = "geckodriver"
class Scrapper():


  def Login():

    Email = "ding-han.yan@student.bodwell.edu"
    Password = "Seandork0919"

    try:
      Login_Email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))
      )
      Login_Email.send_keys(Email)
    
    except:
      print("can't find the element")

    try:
      Btn_Next = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
      )
      Btn_Next.click()

    except:
      print("BTN next wetn wrong")

    sleep(1)

    try:
      Login_Password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "i0118"))
      )
      Login_Password.send_keys(Password)
    except:
      print("Password SEND key went wrong")
    
   
    sleep(2)

    try:
      Btn_Sign_in = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
      )
      Btn_Sign_in.click()
    except:
      print("BTN login in went wrong")

    sleep(1)

    try:
      Btn_No = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idBtn_Back"))
      )
      Btn_No.click()
    except:
      print("BTN NO went wrong")

    sleep(3)

    Use_Web_App_Link = browser.find_element_by_link_text("Use the web app instead")
    Use_Web_App_Link.click()  
    # try:
    #   Use_Web_App_Link = WebDriverWait(browser, 10).until(
    #     EC.((By.CLASS_NAME, "use-app-link"))
    #   )
    #   Use_Web_App_Link.click()
    # except:
    #   print(" USE WEB APP LINK DIDN't WORK")



Scrapper.Login()
