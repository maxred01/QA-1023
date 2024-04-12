import requests

# GET-запрос
response_get = requests.get('https://api.github.com', params={'param1': 'value1'}, timeout=5)

# POST-запрос с JSON
response_post = requests.post('https://api.github.com', json={'key': 'value'}, timeout=5)

# Создание сессии
session = requests.Session()

# Отправка запроса через сессию
response_session = session.get('https://api.github.com')

# Обработка исключений
try:
    response = requests.get('https://api.github.com', timeout=5)
except requests.exceptions.ConnectionError:
    print('Ошибка соединения')
except requests.exceptions.Timeout:
    print('Превышено время ожидания')
except requests.exceptions.RequestException as e:
    print(f'Произошла ошибка: {e}')

# DELETE-запрос
response_delete = requests.delete('https://api.github.com', params={'param1': 'value1'}, timeout=5)

# HEAD-запрос
response_head = requests.head('https://api.github.com', timeout=5)

# OPTIONS-запрос
response_options = requests.options('https://api.github.com', timeout=5)

# PATCH-запрос
response_patch = requests.patch('https://api.github.com', data={'key': 'value'}, timeout=5)

# PUT-запрос
response_put = requests.put('https://api.github.com', data={'key': 'value'}, timeout=5)

# Проверка кодов состояния
if response_get.status_code == requests.codes.ok:
    print('Запрос выполнен успешно')
else:
    print('Ошибка запроса')

# Получение исходного ответа
raw_response = response_get.raw

# Получение заголовков ответа
headers = response_get.headers

# Получение cookies из ответа
cookies = response_get.cookies

# Получение JSON ответа
json_response = response.json()

# Получение текста ответа
text_content = response.text

# Получение истории перенаправлений
history = response.history

# Проверка, является ли перенаправление постоянным
is_permanent_redirect = response.is_permanent_redirect

# Проверка, является ли ответ перенаправлением
is_redirect = response.is_redirect

# Итерация по содержимому ответа по частям
for chunk in response.iter_content(chunk_size=128):
    print(chunk)

# Итерация по строкам ответа
for line in response.iter_lines():
    print(line)

# Получение заголовков ответа
headers = response.headers

# Получение URL, с которого был получен ответ
url = response.url

# Проверка успешности ответа
if response.ok:
    print('Запрос выполнен успешно.')
else:
    print('Ошибка запроса.')

# Вывод причины ответа (обычно это фраза статуса HTTP)
reason = response.reason

# Закрытие соединения
response.close()
