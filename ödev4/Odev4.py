from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class TestLogin:
    #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def testUserName(self): 
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys()
        sleep(2)
        passwordInput.send_keys()
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        testDonus = errorMessage.text == "Epic sadface: Username is required"
        sleep(2)
        print(f"Test Sonucu : {testDonus}")
        sleep(5)
    #Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def testPassword(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        sleep(2)

        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("b")
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testDonus = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu : {testDonus}")
        sleep(5)

    #Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def lockedOutUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce" )
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testDonus = errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 
        print(f"Test Sonucu : {testDonus}")
        sleep(5)

    #Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    def ikonX(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)

        iconFind = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")
        iconFind.click()
        sleep(3)
    #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    def enterInventoryPage(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)

        invertoryList = driver.find_element(By.CLASS_NAME,"/inventory.html")
        print(f"Swag Labs da {len(invertoryList)}(6)adet ürün bulunmaktadır.")
        sleep(100)


Class = TestLogin()
Class.testUserName()
Class.testPassword()
Class.lockedOutUser()
Class.ikonX()
Class.enterInventoryPage()