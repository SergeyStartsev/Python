python
import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
# Установка базового URL для API
        self.base_url = 'http://your_api_server'

    def test_create_post_and_check_description(self):
# Создание нового поста
        post_data = {
            'title': 'New Post',
            'description': 'This is a new post'
        }
        response = requests.post(f'{self.base_url}/posts', json=post_data)
        self.assertEqual(response.status_code, 201)

# Получение списка всех постов
        response = requests.get(f'{self.base_url}/posts')
        self.assertEqual(response.status_code, 200)
        posts = response.json()

# Поиск созданного поста по полю "описание"
        found_post = None
        for post in posts:
            if post['description'] == post_data['description']:
                found_post = post
                break

# Проверка наличия созданного поста
        self.assertIsNotNone(found_post)
        self.assertEqual(found_post['title'], post_data['title'])
        self.assertEqual(found_post['description'], post_data['description'])

if __name__ == '__main__':
    unittest.main()
