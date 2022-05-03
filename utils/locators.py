from email.message import EmailMessage
from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):  

    LOGO = (By.XPATH, "//header/nav[1]/div[1]/div[1]/a[1]/img[1]")
    SEARCH = (By.XPATH, "//input[@id='q']")
    MENU = (By.XPATH, "//a[contains(text(),'Giới Thiệu')]")
    MENU_TITLE = (By.XPATH, "//a[contains(text(),'Thành Phần')]")
    MENU = (By.XPATH, "//a[contains(text(),'Công Dụng')]")
    MENU = (By.CSS_SELECTOR, "div.wrapper:nth-child(2) nav.navbar.navbar-fixed-top.affix div.container div.collapse.navbar-collapse ul.nav.navbar-nav.navbar-right li:nth-child(5) > a:nth-child(1)")


    SETBUY = (By.XPATH, "//body/div[@id='page-top']/section[@id='app-download-area']/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]")
    EMAIL = (By.CSS_SELECTOR, "#Email") 


