from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

# Навигация к странице
driver.get("https://demoqa.com/sortable")

# Получение элементов
tabs = driver.find_element(By.XPATH, "//ul[@class='nav nav-tabs']/li")
items = driver.find_element(By.XPATH, "//ul[@id='sortable']/li")

# Проверка всех вкладок
for tab in tabs:
    tab.click()
    assert tab.get_attribute("class") == "active", f"{tab.text} вкладка не активна"

# Проверка сортировки путем перетаскивания
for i in range(len(items)):
    for j in range(len(items)):
        # Перетаскивание элементов
        source_item = items[i]
        target_item = items[j]
        ActionChains(driver).drag_and_drop(source_item, target_item).perform()

        # Проверка сортировки
        sorted_items = driver.find_element(By.XPATH,"//ul[@id='sortable']/li")
        expected_order = sorted(items, key=lambda x: x.text)
        actual_order = [item.text for item in sorted_items]
        assert actual_order == [item.text for item in
                                expected_order], f"Сортировка не работает для элементов {source_item.text} и {target_item.text}"

# Закрытие браузера
driver.quit()
