python
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
class TestContactUs:
    def test_contact_us_form(self):
        driver = webdriver.Chrome()
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        # Шаги по авторизации и переходу на главную страницу личного кабинета

        # Шаги по открытию формы Contact Us, вводу данных и клику по кнопке

        # Проверка появления всплывающего alert

        driver.quit()
      login_page.open()
login_page.login(username, password)
home_page.go_to_contact_us()
home_page.open_contact_form()
home_page.fill_contact_form(name, email, message)
home_page.submit_contact_form()
alert = driver.switch_to.alert
assert "Ваше сообщение успешно отправлено!" in alert.text
driver.quit()
