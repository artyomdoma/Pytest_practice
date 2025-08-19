# План обучения Automation QA (Python + pytest + Selenium + API + gRPC)

Этот план рассчитан на 8 недель (4–5 ч/день), с теорией, практикой, pytest, ссылками и мини‑проектами.

---

## Неделя 1 — Основы Python, типы данных, циклы

### День 1
- Теория: Mutable vs Immutable (list, dict, set — изменяемые; tuple, str, int — неизменяемые)
- Практика: написать функции, демонстрирующие разницу между изменяемыми и неизменяемыми объектами.
- pytest: тесты для этих функций.
- Полезные ссылки:
  - https://docs.python.org/3/library/stdtypes.html
  - https://realpython.com/python-data-types/

### День 2
- Теория: списки, операции, методы, list comprehension.
- Практика: фильтрация и сортировка списка пользователей по возрасту.
- pytest: тестирование фильтрации.
- Полезные ссылки:
  - https://docs.python.org/3/tutorial/datastructures.html

### День 3
- Теория: словари, методы, dict comprehension.
- Практика: преобразование списка кортежей в словарь и обратно.
- pytest: тесты преобразований.

### День 4
- Теория: условные операторы, тернарный оператор.
- Практика: программа-калькулятор с выбором операции.
- pytest: тесты на каждую операцию.

### День 5
- Теория: циклы for, while; break, continue.
- Практика: генерация чисел Фибоначчи до N.
- pytest: тест генератора.

### День 6
- Повторение, решение задач с LeetCode/Easy.
- pytest: оформление тестов.

### День 7 — Мини-проект
- Реализовать модуль для анализа списка заказов (dict + list comprehension).
- Выводить статистику по категориям и сумме.
- pytest: тесты для подсчётов.

---

## Неделя 2 — Функции, декораторы, итераторы

### День 1
- Теория: функции, *args, **kwargs.
- Практика: функция суммирования произвольного числа аргументов.
- pytest: тесты.

### День 2
- Теория: замыкания, колбеки.
- Практика: функция с обработчиком-колбеком.
- pytest: тесты.

### День 3
- Теория: декораторы (простые и с параметрами).
- Практика: декоратор логирования вызова функций.
- pytest: тесты.

### День 4
- Теория: генераторы (yield) и итераторы.
- Практика: итератор чисел Фибоначчи.
- pytest: тесты.

### День 5
- Теория: itertools (chain, cycle, islice).
- Практика: генерация последовательностей с itertools.
- pytest: тесты.

### День 6
- Повторение, задачи с использованием декораторов и генераторов.

### День 7 — Мини-проект
- Реализовать систему кеширования с декоратором.
- pytest: тесты корректности кеша.

---

## Неделя 3 — ООП в Python

### День 1
- Теория: классы, __init__, атрибуты.
- Практика: класс BankAccount.
- pytest: тесты.

### День 2
- Теория: наследование, переопределение методов.
- Практика: SavingsAccount.
- pytest: тесты.

### День 3
- Теория: статические и классовые методы.
- Практика: утилитарный класс с @staticmethod.
- pytest: тесты.

### День 4
- Теория: инкапсуляция (public/protected/private).
- Практика: скрытые поля в классе.
- pytest: тесты.

### День 5
- Теория: контекстные менеджеры.
- Практика: менеджер для работы с файлами.
- pytest: тесты.

### День 6
- Повторение.

### День 7 — Мини-проект
- Класс UsersManager для CRUD операций.
- pytest: тесты.

---

## Неделя 4 — pytest расширенный

### День 1
- Теория: структура тестов, asserts.
- Практика: простые тесты.

### День 2
- Теория: фикстуры, scope.
- Практика: фикстуры function/module/session.

### День 3
- Теория: autouse фикстуры.
- Практика: логирование тестов.

### День 4
- Теория: параметризация тестов.
- Практика: parametrize.

### День 5
- Теория: финализаторы.
- Практика: освобождение ресурсов.

### День 6
- Повторение.

### День 7 — Мини-проект
- Тестирование модуля с фикстурами, параметризацией.

**Полезные ссылки:**
- Pytest API‑тестирование — LambdaTest: https://www.lambdatest.com/learning-hub/pytest-api-testing?utm_source=chatgpt.com
- Видео: интеграционные REST‑API‑тесты с pytest: https://www.youtube.com/watch?v=7dgQRVqF1N0&utm_source=chatgpt.com

---

## Неделя 5 — Selenium + Selenoid

### День 1
- Теория: локаторы (id, name, css, xpath).
- Практика: поиск элементов.

### День 2
- Теория: явные и неявные ожидания.
- Практика: WebDriverWait.

### День 3
- Теория: DOM, iframe.
- Практика: переключение контекстов.

### День 4
- Теория: headless режим.
- Практика: тесты в headless.

### День 5
- Теория: Selenoid, Remote WebDriver.
- Практика: запуск тестов в Selenoid.

### День 6
- Повторение.

### День 7 — Мини-проект
- POM тест логина.

**Полезные ссылки:**
- Всесторонний гайд: Selenium + pytest (LambdaTest): https://www.lambdatest.com/learning-hub/selenium-pytest-tutorial?utm_source=chatgpt.com
- Пошаговый Selenium с Python (BrowserStack): https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test?utm_source=chatgpt.com
- Документация pytest‑selenium: https://pytest-selenium.readthedocs.io/en/latest/user_guide.html?utm_source=chatgpt.com
- Пример тестов с POM и pytest‑selenium: https://pytest-with-eric.com/automation/pytest-selenium/?utm_source=chatgpt.com

---

## Неделя 6 — HTTP API с requests

### День 1
- Теория: GET, POST.
- Практика: тест API.

### День 2
- Теория: заголовки, параметры.
- Практика: передача данных.

### День 3
- Теория: JSON, парсинг.
- Практика: проверка схем.

### День 4
- Теория: сессии requests.Session.
- Практика: авторизация.

### День 5
- Повторение.

### День 6 — Мини-проект
- API тестирование демо-сервиса.

**Полезные ссылки:**
- Pytest API‑тестирование (LambdaTest): https://www.lambdatest.com/learning-hub/pytest-api-testing?utm_source=chatgpt.com
- Видео‑интеграция REST‑API с pytest: https://www.youtube.com/watch?v=7dgQRVqF1N0&utm_source=chatgpt.com

---

## Неделя 7 — gRPC основы

### День 1
- Теория: gRPC, proto файлы.
- Практика: генерация клиента.

### День 2
- Теория: вызов методов.
- Практика: тест gRPC сервиса.

### День 3
- Повторение.

### День 4 — Мини-проект
- gRPC тестирование демо API.

**Полезные ссылки:**
- Коллекция awesome‑grpc: https://github.com/grpc-ecosystem/awesome-grpc?utm_source=chatgpt.com
- Тестирование gRPC на Python и Postman (Medium): https://medium.com/%40dneprokos/sdet-exploring-grpc-testing-practical-examples-with-postman-c-and-python-clients-f1a29f91e3eb?utm_source=chatgpt.com
- pytest‑grpc: пример фикстур и тестов: https://www.python4data.science/en/latest/data-processing/apis/grpc/test.html?utm_source=chatgpt.com
- Реализация gRPC‑сервиса в Python: https://www.velotio.com/engineering-blog/grpc-implementation-using-python?utm_source=chatgpt.com

---

## Неделя 8 — Паттерны POM/ROM

### День 1
- Теория: Page Object Model.
- Практика: перепись теста на POM.

### День 2
- Теория: Resource Object Model.
- Практика: API тесты в ROM.

### День 3
- Интеграция UI и API тестов.

### День 4
- Подготовка проекта к CI.

### День 5
- Запуск тестов в CI.

### День 6
- Повторение.

### День 7 — Итоговый проект
- Проект с UI+API+gRPC тестами, POM/ROM, pytest, CI.

**Полезные ссылки:**
- POM и CI — BrowserStack: https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test?utm_source=chatgpt.com
- POM и CI — LambdaTest: https://www.lambdatest.com/learning-hub/selenium-pytest-tutorial?utm_source=chatgpt.com
