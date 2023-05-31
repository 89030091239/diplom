import pytest
import logging
from logging.handlers import RotatingFileHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# @pytest.fixture(scope="session", autouse=True)
# def setup_logging():
#     # Настройка логгера для записи сообщений в файл
#     log_path = r'C:\Users\Sever\PycharmProjects\diplom\log_file.txt'
#     logging.basicConfig(filename=log_path)


@pytest.fixture(scope="function")
def setup(request):
    # Создаем логгер и настраиваем обработчик для записи в файл
    log_path = r'C:\Users\Sever\PycharmProjects\diplom\log_file.txt'
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)

    # Создаем обработчик и устанавливаем его уровень логирования
    handler = RotatingFileHandler(log_path, maxBytes=100000, backupCount=1)
    handler.setLevel(logging.INFO)

    # Форматирование сообщений лога
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    pytest.driver = webdriver.Chrome(r'C:\Users\Sever\PycharmProjects\diplom\tests\chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Получение названия текущего теста
    test_name = request.node.name

    # Добавление информации о названии теста в лог-файл
    logger.info(f'Запуск теста: {test_name}')

    start_time = time.time()

    @pytest.hookimpl(tryfirst=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        result = outcome.get_result()

        # Получение статуса выполнения теста
        if result.when == 'call':
            if result.passed:
                status = 'Успешно'
            else:
                status = 'Неуспешно'

            # Получение имени ошибки (если есть)
            error_name = ''
            if result.failed:
                error_name = result.longreprtext

            # Добавление информации о статусе и ошибке в лог-файл
            logger.info(f'Статус выполнения теста: {status}')
            if error_name:
                logger.info(f'Имя ошибки: {error_name}')

    def teardown():
        end_time = time.time()
        total_time = end_time - start_time

        # Добавление информации о времени выполнения теста в лог-файл
        logger.info(f'Тест завершен. Время выполнения: {total_time} сек.')

        pytest.driver.quit()

    request.addfinalizer(teardown)
    return pytest.driver

@pytest.fixture(scope="function")
def navigate_to_registration_page(setup):
    pytest.driver = setup
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))  # Ждем загрузки страницы с формой "Авторизация"
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    # Нажимаем на ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Ожидание появления страницы с формой "Регистрация"
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//h1[contains(text(),"Регистрация")]')))
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"


@pytest.fixture(scope="function")
def navigate_to_authorization_page(setup):
    pytest.driver = setup
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))  # Ждем загрузки страницы с формой "Авторизация"
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
