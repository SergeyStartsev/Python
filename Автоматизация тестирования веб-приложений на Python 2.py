python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebsite(unittest.TestCase):
    def setUp(self):
        # Установка базового URL для веб-сайта
        self.base_url = 'http://your_website'

        # Инициализация драйвера браузера
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Завершение работы драйвера браузера
        self.driver.quit()

    def test_create_post_and_check_title(self):
        # Вход на веб-сайт
        self.driver.get(f'{self.base_url}/login')
        username_input = self.driver.find_element_by_id('username')
        password_input = self.driver.find_element_by_id('password')
        login_button = self.driver.find_element_by_id('login-button')

        username_input.send_keys('your_username')
        password_input.send_keys('your_password')
        login_button.click()

        # Создание нового поста
        post_title_input = self.driver.find_element_by_id('post-title')
        post_description_input = self.driver.find_element_by_id('post-description')
        create_post_button = self.driver.find_element_by_id('create-post-button')

        post_title_input.send_keys('New Post')
        post_description_input.send_keys('This is a new post')
        create_post_button.click()

        # Проверка наличия названия поста на странице
        post_title = self.driver.find_element_by_class_name('post-title').text
        self.assertEqual(post_title, 'New Post')

if __name__ == '__main__':
    unittest.main()
