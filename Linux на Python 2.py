python
import unittest
import subprocess

python
class TestCommands(unittest.TestCase):
    pass

python
class TestCommands(unittest.TestCase):
    def test_list_files(self):
# Тестирование команды вывода списка файлов (l)
# Ваш код теста

    def test_extract_with_paths(self):
# Тестирование команды разархивирования с путями (x)
# Ваш код теста

python
class TestCommands(unittest.TestCase):
    def test_list_files(self):
# Тестирование команды вывода списка файлов (l)
        result = subprocess.run(['tar', 'tf', 'archive.tar'], capture_output=True, text=True)
        expected_output = "file1.txt\nfile2.txt\nfile3.txt\n"
        self.assertEqual(result.stdout, expected_output)

    def test_extract_with_paths(self):
# Тестирование команды разархивирования с путями (x)
        subprocess.run(['tar', 'xf', 'archive.tar'])
        extracted_files = ['path/to/file1.txt', 'path/to/file2.txt', 'path/to/file3.txt']
        for file in extracted_files:
            self.assertTrue(os.path.exists(file))

python
if __name__ == '__main__':
    unittest.main





