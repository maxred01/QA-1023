import pytest
import pytest_check as check
from Maksim_Tsybulka.class_work_9_f.page.locators import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)


    check.equal(page.btn_headers_domain.get_text(), 'Дом43ены', 'Тест локатора не равен ожидаймому результату')
    check.is_true(page.btn_headers_mail.is_visible())
