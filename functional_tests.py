import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""

    def setUp(self) -> None:
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        """демонтаж"""
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """подтверждение строки в таблице списка"""
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""
        # Солнышко слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решила оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби -
        # вязанье рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажимает Enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Страница снова обновляется, и теперь показывает оба элемента ее списка
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушки из павлиньих перьев')

        # Солнышко интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес - об этом
        # выводится небольшой текст с объяснениями.

        # Она посещает этот URL-адрес - ее список по-прежнему там.

        # Удовлетворенная, она снова ложится спать
        self.fail('Закончить тест!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
