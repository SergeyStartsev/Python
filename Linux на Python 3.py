python
import unittest

class TestFixtures(unittest.TestCase):
    def setUp(self):
# Создание файла stat.txt перед каждым тестом
        with open('stat.txt', 'w') as f:
            f.write('')

    def tearDown(self):
# Удаление файла stat.txt после каждого теста
        os.remove('stat.txt')

    def test_step1(self):
# Шаг 1 теста
# Ваш код теста
        self._append_stat('Step 1')

    def test_step2(self):
# Шаг 2 теста
# Ваш код теста
        self._append_stat('Step 2')

    def _append_stat(self, step):
# Дописывание информации в файл stat.txt
        with open('stat.txt', 'a') as f:
# Получение времени
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Получение количества файлов из конфига
            file_count = get_file_count_from_config()
# Получение размера файла из конфига
            file_size = get_file_size_from_config()
# Получение статистики загрузки процессора из файла /proc/loadavg
            cpu_load = get_cpu_load_from_file('/proc/loadavg')
# Запись информации в файл stat.txt
            f.write(f"{current_time}, {file_count}, {file_size}, {cpu_load}\n")
