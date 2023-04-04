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


# ------------------------------------------------------------------------------------------------

# Conduit kezdő oldal megnyitása----------------------------------------------------------------------------------------

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# page_name = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/h1')
# assert page_name.is_displayed()
# assert page_name.text == "conduit"

# böngésző bezárása
# browser.quit()

class Conduit(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://localhost:1667/#/"
        self.browser.get(URL)
        self.browser.maximize_window()
        self.page_name = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/h1')
        assert self.page_name.is_displayed()
        assert self.page_name.text == "conduit"

    def teardown_method(self):
        self.browser.quit()

    def sign_up(self):
        sign_up_link = self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
        sign_up_link.click()

    def sign_up_btn(self):
        sign_up_btn = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
        sign_up_btn.click()

# Sign Up mező tesztelése üres mezős kitöltés CON_TC_000----------------------------------------------------------------

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()

# sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
# sign_up.click()

# sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# sign_up_btn.click()
# browser.implicitly_wait(time_to_wait=5)
# reg_fail= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
# reg_fail_url=browser.get(URL)
# browser.implicitly_wait(time_to_wait=5)
# assert reg_fail_url != URL
# reg_fail.click()

# browser.quit()

# Sign Up mező tesztelése üres email és password mezők kitöltése nélkül CON_TC_001---------------------------------------

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()

# sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
# sign_up.click()

# sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# Username= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')

# Username.send_keys('klingonuser')
# sign_up_btn.click()
# browser.implicitly_wait(time_to_wait=5)
# reg_fail= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
# reg_fail_url=browser.get(URL)
# browser.implicitly_wait(time_to_wait=5)
# assert reg_fail_url != URL
# reg_fail.click()

# browser.quit()


# Sign Up mező tesztelése üres password mező kitöltése nélkül CON_TC_002-------------------------------------------------

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()

# sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
# sign_up.click()

# sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# Username= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
# Email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')

# Username.send_keys('klingonuser')
# Email.send_keys('klingonuser@klingonmail.com')
# time.sleep(6)
# sign_up_btn.click()
# browser.implicitly_wait(time_to_wait=5)
# reg_fail= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
# reg_fail_url=browser.get(URL)
# browser.implicitly_wait(time_to_wait=5)
# assert reg_fail_url != URL
# reg_fail.click()
# browser.quit()

# Sign Up mező tesztelése helyes kitöltés CON_TC_003 (hogy lehet a beviteli mezőkhöz plusz egy számot hozzá adni hogy mindig tudjak regisztrálni?

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()

# sign_up= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
# sign_up.click()

# sign_up_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# Username= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
# Email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
# Password=browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')

# Username.send_keys('klingonuser')
# Email.send_keys('klingonuser@klingonmail.com')
# Password.send_keys('Kl1Ngon$')
# sign_up_btn.click()
# browser.implicitly_wait(time_to_wait=5)
# welcome= browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
# welcome.click()
# browser.quit()

# Helytelen bejelentkezés (hibás felhasználónév) CON_TC_004

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()
# sign_in= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[2]/a')
# sign_in.click()

# sign_in_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# sign_in_btn.click()

# sign_fail= browser.find_element(By.XPATH, '//html/body/div[2]/div/div[4]/div/button')
# sign_fail_url=browser.get(URL)
# browser.implicitly_wait(time_to_wait=2)
# assert sign_fail_url != URL
# sign_fail.click()

# Helytelen bejelentkezés (hibás jelszó) CON_TC_005

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()
# sign_in= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[2]/a')
# sign_in.click()

# sign_in_email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
# sign_in_email.send_keys('klingonuser@klingonmail.com')
# sign_in_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# sign_in_btn.click()

# browser.quit()

# Helyes bejelentkezés CON_TC_006

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()
# sign_in= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[2]/a')
# sign_in.click()

# sign_in_email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
# sign_in_email.send_keys('klingonuser@klingonmail.com')
# sign_in_password= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
# sign_in_password.send_keys('Kl1Ngon$')
# sign_in_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# sign_in_btn.click()

# browser.quit()

# Regisztrált felhaasználó kijelentkezése CON_TC_007

# browser = webdriver.Chrome(service=service, options=options)
# URL = "http://localhost:1667/#/"
# browser.get(URL)
# browser.maximize_window()
# elfogad= browser.find_element(By.XPATH, '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
# elfogad.click()
# sign_in= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[2]/a')
# sign_in.click()

# sign_in_email= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
# sign_in_email.send_keys('klingonuser@klingonmail.com')
# sign_in_password= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
# sign_in_password.send_keys('Kl1Ngon$')
# sign_in_btn= browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
# sign_in_btn.click()

# browser.implicitly_wait(time_to_wait=2)
# log_out= browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[5]/a')
# log_out.click()
# browser.quit()
