python
import unittest
import paramiko

class TestFixtures(unittest.TestCase):
    def setUp(self):
# Создание SSH-соединения перед каждым тестом
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect('your_remote_server', username='your_username', password='your_password')

    def tearDown(self):
# Закрытие SSH-соединения после каждого теста
        self.ssh_client.close()

    def test_step1(self):
# Шаг 1 теста
# Ваш код теста
        self._append_stat('Step 1')

    def test_step2(self):
# Шаг 2 теста
# Ваш код теста
        self._append_stat('Step 2')

    def _append_stat(self, step):
# Выполнение команды на удаленном сервере для дописывания информации в файл stat.txt
        command = f"echo '{step}' >> stat.txt"
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
# Проверка вывода команды и обработка ошибок

if __name__ == '__main__':
    unittest.main()
