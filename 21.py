# még nincs minden import használva de ami szürke marad a végére törölve lesz....
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
#------------------------------------------------------------------------------------------------

# Conduit kezdő oldal megnyitása

#browser = webdriver.Chrome(service=service, options=options)
#URL = "http://localhost:1667/#/"
#browser.get(URL)
#browser.maximize_window()

# Sign Up mező tesztelése üres mezős kitöltés CON_TC_000

#browser = webdriver.Chrome(service=service, options=options)
#URL = "http://localhost:1667/#/"
#browser.get(URL)
#browser.maximize_window()
#elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
#elfogad.click()

#sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
#sign_up.click()

#sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
#sign_up_btn.click()
#browser.implicitly_wait(time_to_wait=5)
#reg_fail= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
#reg_fail_url=browser.get(URL)
#browser.implicitly_wait(time_to_wait=5)
#assert reg_fail_url != URL
#reg_fail.click()

#Sign Up mező tesztelése üres email és password mezők kitöltése nélkül CON_TC_001

#browser = webdriver.Chrome(service=service, options=options)
#URL = "http://localhost:1667/#/"
#browser.get(URL)
#browser.maximize_window()
#elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
#elfogad.click()

#sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
#sign_up.click()

#sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
#Username= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')

#Username.send_keys('klingonuser')
#sign_up_btn.click()
#browser.implicitly_wait(time_to_wait=5)
#reg_fail= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
#reg_fail_url=browser.get(URL)
#browser.implicitly_wait(time_to_wait=5)
#assert reg_fail_url != URL
#reg_fail.click()

#Sign Up mező tesztelése üres password mező kitöltése nélkül CON_TC_002

#browser = webdriver.Chrome(service=service, options=options)
#URL = "http://localhost:1667/#/"
#browser.get(URL)
#browser.maximize_window()
#elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
#elfogad.click()

#sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
#sign_up.click()

#sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
#Username= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
#Email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')

#Username.send_keys('klingonuser')
#Email.send_keys('klingonuser@klingonmail.com')
#time.sleep(6)
#sign_up_btn.click()
#browser.implicitly_wait(time_to_wait=5)
#reg_fail= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
#reg_fail_url=browser.get(URL)
#browser.implicitly_wait(time_to_wait=5)
#assert reg_fail_url != URL
#reg_fail.click()


#Sign Up mező tesztelése helyes kitöltés CON_TC_003 (hogy lehet a beviteli mezőkhöz plusz egy számot hozzá adni hogy mindig tudjak regisztrálni?

#browser = webdriver.Chrome(service=service, options=options)
#URL = "http://localhost:1667/#/"
#browser.get(URL)
#browser.maximize_window()
#elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
#elfogad.click()

#sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
#sign_up.click()

#sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
#Username= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
#Email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
#Password=browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')

#Username.send_keys('klingonuser')
#Email.send_keys('klingonuser@klingonmail.com')
#Password.send_keys('Kl1Ngon$')
#sign_up_btn.click()
#browser.implicitly_wait(time_to_wait=5)
#welcome= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
#welcome.click()


# böngésző bezárása

#browser.quit()

