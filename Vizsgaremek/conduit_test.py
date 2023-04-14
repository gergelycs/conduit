from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv

# Változók:

username = 'klingonuser'
email = 'klingonuser@klingonmail.com'
jelszo = 'Kl1Ngon$'

article_title_1 = 'bogyó'
about_1 = "és"
article_text_1 = 'babóca'
tag_1 = 'meséje'

article_title_2 = 'hetedhet orszag'
article_text_2 = 'krisztoforo'
tag_2 = 'treffhetes'
comment_input_1 = 'mikkamakka'


class TestConduit(object):

    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://localhost:1667/#/"
        self.browser.get(URL)
        self.browser.maximize_window()
        self.page_name = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/h1')
        assert self.page_name.is_displayed()
        assert self.page_name.text == "conduit"

    def teardown_method(self):
        self.browser.quit()

    def login(self):
        sign_in_page_button = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        sign_in_page_button.click()

        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        email_input.send_keys(email)
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_input.send_keys(jelszo)

        sign_in_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
        sign_in_button.click()

        your_feed = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link router-link-exact-active active"]')))
        assert your_feed.is_displayed()

    # Cookies kezelése
    def test_cookies(self):
        accept = self.browser.find_element(By.CLASS_NAME, 'cookie__bar__buttons__button--accept')
        accept.click()
        time.sleep(1)
        cookie_container = self.browser.find_elements(By.CSS_SELECTOR, 'footer > .container > #cookie-policy-panel')
        assert len(cookie_container) == 0

    # helyes regisztráció:
    def test_registration(self):
        sign_up = self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')
        sign_up.click()

        user_name_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH, '//input[@type="password"]')
        sign_up_btn = self.browser.find_element(By.XPATH, '//button[contains(text(), "Sign up")]')

        user_name_input.send_keys(username)
        email_input.send_keys(email)
        password_input.send_keys(jelszo)
        sign_up_btn.click()

        self.browser.implicitly_wait(time_to_wait=5)
        welcome = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
        welcome.click()

    # Regisztráció helytelen email címmel
    def test_registration_wrong_email(self):
        sign_up_button = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_button.click()

        username_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

        username_input.send_keys(username)
        email_input.send_keys('test@')
        password_input.send_keys(jelszo)

        sign_up_button2 = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_button2.click()

        time.sleep(5)
        registration_message = self.browser.find_element(By.XPATH, '//div[@class="swal-title"]')
        registration_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert registration_message.text == "Registration failed!"
        assert registration_problem.text == "Email must be a valid email."

        registration_failed_button = self.browser.find_element(By.XPATH,
                                                               '//button[@class="swal-button swal-button--confirm"]')
        registration_failed_button.click()

    # Regisztráció üres mező kitöltésekkel
    def test_registration_empty_fields(self):
        sign_up_button = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_button.click()

        username_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

        username_input.send_keys()
        email_input.send_keys()
        password_input.send_keys()

        sign_up_button2 = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_button2.click()

        time.sleep(5)
        registration_message = self.browser.find_element(By.XPATH, '//div[@class="swal-title"]')
        registration_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert registration_message.text == "Registration failed!"
        assert registration_problem.text == "Username field required."

        registration_failed_button = self.browser.find_element(By.XPATH,
                                                               '//button[@class="swal-button swal-button--confirm"]')
        registration_failed_button.click()

    # Bejelentkezés funkció ellenőrzése üres mező kitöltéssel
    def test_login_empty_fields(self):
        sing_in_page_button = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        sing_in_page_button.click()

        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        email_input.send_keys()
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_input.send_keys()

        sing_in_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sing_in_button.click()

        time.sleep(2)
        login_message = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]')
        assert login_message.text == "Login failed!"

        time.sleep(2)
        sign_fail = self.browser.find_element(By.XPATH, '//html/body/div[2]/div/div[4]/div/button')
        sign_fail.click()

    # Bejelentkezés funkció ellenőrzése helytelen adattal (jelszó)
    def test_login_wrong_password(self):
        sing_in_page_button = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        sing_in_page_button.click()
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        email_input.send_keys(email)
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_input.send_keys('nemjójelsz0')

        sing_in_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sing_in_button.click()

        login_message = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        login_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert login_message.text == "Login failed!"
        assert login_problem.text == "Invalid user credentials."

        login_failed_button = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        login_failed_button.click()

    # Bejelentkezés helyes adatokkal
    def test_login(self):
        TestConduit.login(self)

    # Global Feed oldalainak végigjárása
    def test_page_number(self):
        TestConduit.login(self)

        page_numbers_list = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
        for page in page_numbers_list:
            page.click()
            actual_page = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, '//li[@class="page-item active"]')))
            assert page.text == actual_page.text

    # Szűkített tag alapú lista bejárás
    def test_tags(self):
        TestConduit.login(self)

        lorem_tag = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@class="sidebar"]/div[@class="tag-list"]/a[@href="#/tag/lorem"]')))
        lorem_tag.click()

        article_list = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]/h1')))
        assert len(article_list) != 0

    # Bejegyzés létrehozása, adatbevitel ellenőrzése
    def test_article_create1(self):
        TestConduit.login(self)

        time.sleep(5)
        new_article_link = self.browser.find_element(By.XPATH, '//a[@href="#/editor"]')
        new_article_link.click()
        WebDriverWait(self.browser, 3).until(EC.url_to_be('http://localhost:1667/#/editor'))
        article_title = self.browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
        about = self.browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
        article_text = self.browser.find_element(By.XPATH,
                                                 '//textarea[@placeholder="Write your article (in markdown)"]')
        tag = self.browser.find_element(By.CSS_SELECTOR, 'input.ti-new-tag-input')
        publish_btn = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        article_title.send_keys(article_title_1)
        about.send_keys(about_1)
        article_text.send_keys(article_text_1)
        tag.send_keys(tag_1)
        article_text.click()
        publish_btn.click()

        time.sleep(5)
        actual_article_title = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        assert actual_article_title.text == article_title_1
        actual_author = self.browser.find_element(By.CSS_SELECTOR, '.article-meta .author')
        assert actual_author.text == username
        actual_article_content = self.browser.find_element(By.CSS_SELECTOR, '.article-content div div')
        assert actual_article_content.text == article_text_1
        actual_tags = self.browser.find_element(By.CSS_SELECTOR, '.article-content .tag-list')
        assert actual_tags.text == tag_1

    # Bejegyzés adatainak módosítása,
    def test_article_edit(self):
        TestConduit.login(self)

        time.sleep(5)
        new_article_link = self.browser.find_element(By.XPATH, '//a[@href="#/editor"]')
        new_article_link.click()
        WebDriverWait(self.browser, 3).until(EC.url_to_be('http://localhost:1667/#/editor'))
        article_title = self.browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
        about = self.browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
        article_text = self.browser.find_element(By.XPATH,
                                                 '//textarea[@placeholder="Write your article (in markdown)"]')
        tag = self.browser.find_element(By.CSS_SELECTOR, 'input.ti-new-tag-input')
        publish_btn = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        article_title.send_keys(article_title_1)
        about.send_keys(about_1)
        article_text.send_keys(article_title_1)
        tag.send_keys(tag_1)
        article_text.click()
        publish_btn.click()

        time.sleep(5)
        actual_article_title = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        assert actual_article_title.text == 'bogyó'
        actual_author = self.browser.find_element(By.CSS_SELECTOR, '.article-meta .author')
        assert actual_author.text == username
        actual_article_content = self.browser.find_element(By.CSS_SELECTOR, '.article-content div div')
        assert actual_article_content.text == 'babóca'
        actual_tags = self.browser.find_element(By.CSS_SELECTOR, '.article-content .tag-list')
        assert actual_tags.text == 'meséje'

        edit_article = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/span/a/span')
        edit_article.click()
        time.sleep(3)
        article_title.clear()
        article_title.send_keys(article_title_2)
        article_text.clear()
        article_text.send_keys(article_text_2)
        tag.clear()
        tag.send_keys(tag_2)
        article_text.click()
        publish_btn.click()
        home = self.browser.find_element(By.CSS_SELECTOR, 'a[href="#/"]')
        home.click()

    # Bejegyzés törlése
    def test_article_delete(self):
        TestConduit.login(self)

        time.sleep(5)
        new_article_link = self.browser.find_element(By.XPATH, '//a[@href="#/editor"]')
        new_article_link.click()
        time.sleep(3)
        WebDriverWait(self.browser, 3).until(EC.url_to_be('http://localhost:1667/#/editor'))
        article_title = self.browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
        about = self.browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
        article_text = self.browser.find_element(By.XPATH,
                                                 '//textarea[@placeholder="Write your article (in markdown)"]')
        tag = self.browser.find_element(By.CSS_SELECTOR, 'input.ti-new-tag-input')
        publish_btn = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
        time.sleep(3)
        article_title.send_keys('bogyó')
        about.send_keys('és')
        article_text.send_keys('babóca')
        tag.send_keys('meséje')
        article_text.click()
        publish_btn.click()
        time.sleep(3)
        article_url = self.browser.current_url
        delete_article_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
        delete_article_button.click()

        time.sleep(5)

        assert self.browser.current_url != article_url

    # Komment hozzáadása, új adatbevitel ellenőrzése
    def test_comment_create(self):
        TestConduit.login(self)

        time.sleep(5)
        new_article_link = self.browser.find_element(By.XPATH, '//a[@href="#/editor"]')
        new_article_link.click()
        WebDriverWait(self.browser, 3).until(EC.url_to_be('http://localhost:1667/#/editor'))
        article_title = self.browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
        about = self.browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
        article_text = self.browser.find_element(By.XPATH,
                                                 '//textarea[@placeholder="Write your article (in markdown)"]')
        tag = self.browser.find_element(By.CSS_SELECTOR, 'input.ti-new-tag-input')
        publish_btn = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        article_title.send_keys(article_title_1)
        about.send_keys(about_1)
        article_text.send_keys(article_text_1)
        tag.send_keys(tag_1)
        article_text.click()
        publish_btn.click()

        comment_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
        comment_input.send_keys(comment_input_1)
        post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
        post_comment_button.click()

        new_comment = \
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card"]')))[0]
        assert new_comment.is_displayed()

    #  Komment törlése funkció ellenőrzése
    def test_comment_delete(self):
        TestConduit.login(self)

        time.sleep(5)
        new_article_link = self.browser.find_element(By.XPATH, '//a[@href="#/editor"]')
        new_article_link.click()
        WebDriverWait(self.browser, 3).until(EC.url_to_be('http://localhost:1667/#/editor'))
        article_title = self.browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
        about = self.browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
        article_text = self.browser.find_element(By.XPATH,
                                                 '//textarea[@placeholder="Write your article (in markdown)"]')
        tag = self.browser.find_element(By.CSS_SELECTOR, 'input.ti-new-tag-input')
        publish_btn = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        article_title.send_keys(article_title_1)
        about.send_keys(about_1)
        article_text.send_keys(article_text_1)
        tag.send_keys(tag_1)
        article_text.click()
        publish_btn.click()

        comment_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
        comment_input.send_keys(comment_input_1)
        post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
        post_comment_button.click()

        new_comment = \
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card"]')))[0]
        assert new_comment.is_displayed()

        delete_comment_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
        delete_comment_button.click()

        comments = WebDriverWait(self.browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card"]')))
        comment_pieces = len(comments)
        assert comment_pieces != 0

    # kilépés funkció ellenőrzése:

    def test_log_out(self):
        TestConduit.login(self)

        self.browser.implicitly_wait(time_to_wait=2)
        log_out = self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[5]/a')
        log_out.click()

        sign_in_page_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))
        assert sign_in_page_button.is_displayed()

    # adatbevitel fájlból:
    def test_source(self):
        self.login()

        path = r"Vizsgaremek/alapanyag.csv"
        time.sleep(4)

        with open(path, 'r', encoding='utf-8') as alapanyag:
            alap_reader = csv.reader(alapanyag, delimiter=',')

            for alapanyag in alap_reader:
                new_article_link = self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[2]/a')
                new_article_link.click()
                time.sleep(2)
                article_title = self.browser.find_element(By.CLASS_NAME, 'form-control-lg')
                about = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="What\'s this article about?"]')
                write = self.browser.find_element(By.CSS_SELECTOR,
                                                  'textarea[placeholder="Write your article (in markdown)"]')
                tag = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter tags"]')
                publish = self.browser.find_element(By.CLASS_NAME, 'btn-primary')
                article_title.send_keys(alapanyag[0])
                about.send_keys(alapanyag[1])
                write.send_keys(alapanyag[2])
                tag.send_keys(alapanyag[3])
                publish.click()
                time.sleep(5)
                published = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/h1').text
                assert published == alapanyag[0]
                home = self.browser.find_element(By.CSS_SELECTOR, 'a[href="#/"]')
                home.click()

    # adat mentése fájlba:

    def test_save(self):
        self.login()

        tag_list = WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class="sidebar"]/div/a[@class="tag-pill tag-default"]')))
        with open('save.txt', 'w') as file:
            writer = csv.writer(file)
            for tag in tag_list:
                writer.writerow([tag.text])
        with open('save.txt', 'r') as file:
            first_row = file.readline().rstrip('\n')
            assert first_row == tag_list[0].text

    def test_tobszoros_adatbevitel(self):
        self.login()
        path = r"Vizsgaremek/alapanyag.csv"
        with open(path, 'r', encoding='utf-8') as alapanyag:
            alap_reader = csv.reader(alapanyag, delimiter=',')

            for alapanyag in alap_reader:
                time.sleep(2)
                new_article_link = self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[2]/a')
                new_article_link.click()
                time.sleep(2)
                article_title = self.browser.find_element(By.CLASS_NAME, 'form-control-lg')
                about = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="What\'s this article about?"]')
                write = self.browser.find_element(By.CSS_SELECTOR,
                                                  'textarea[placeholder="Write your article (in markdown)"]')
                tag = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter tags"]')
                publish = self.browser.find_element(By.CLASS_NAME, 'btn-primary')
                article_title.send_keys(alapanyag[0])
                about.send_keys(alapanyag[1])
                write.send_keys(alapanyag[2])
                tag.send_keys(alapanyag[3])
                publish.click()
                time.sleep(3)
                published = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/h1').text
                assert published == alapanyag[0]

                comment_input = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
                comment_input.send_keys(alapanyag[2])
                post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
                post_comment_button.click()
                time.sleep(4)
                comment_input.send_keys(alapanyag[3])
                post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
                post_comment_button.click()

        time.sleep(6)

        path = r"Vizsgaremek/alapanyag.csv"
        time.sleep(4)
        # a megnyitott fájlt soronként commenteljük

        with open(path, "r") as soronkent:
            tartalom = soronkent.readlines()
            for sor in tartalom:
                sor = sor.rstrip()  # sorvége-jel eltávolítása
                print(sor)

        comment_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
        comment_input.send_keys(sor)
        post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
        post_comment_button.click()
        time.sleep(4)
        comment_input.send_keys(sor)
        post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
        post_comment_button.click()
        home = self.browser.find_element(By.CSS_SELECTOR, 'a[href="#/"]')
        home.click()
