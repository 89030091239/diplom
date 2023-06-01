import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

@pytest.fixture(scope="session")
def logger(request):
    # Определение пути к файлу логов
    log_path = r'C:\Users\Sever\PycharmProjects\diplom\log_file.txt'

    # Проверка существования файла логов и его создание, если он не существует
    if not os.path.exists(log_path):
        open(log_path, 'w').close()

    # Создание логгера
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)

    # Создание обработчика файла
    handler = logging.FileHandler(log_path)
    handler.setLevel(logging.INFO)

    # Установка формата логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    logger.addHandler(handler)

    start_time = time.time()

    def finalizer():
        end_time = time.time()
        total_time = end_time - start_time
        logger.info(f'Время выполнения всех тестов: {total_time} сек.')

        # Получение статуса прохождения теста
        test_status = "Успешно" if request.node.testsfailed == 0 else "Неуспешно"
        logger.info(f'Статус прохождения теста: {test_status}')

        # Запись имени ошибки, если тест завершился неуспешно
        if test_status == "Неуспешно":
            for item in request.session.items:
                if item.nodeid == request.node.nodeid and item.when == 'call' and item.longrepr is not None:
                    error_name = item.longrepr.reprcrash.message
                    logger.error(f"Ошибка при выполнении теста: {error_name}")


    request.addfinalizer(finalizer)

    return logger


@pytest.fixture(scope="function")
def setup(request, logger):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    pytest.driver = driver

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)

    # Rest of the setup code
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Добавление информации о запуске теста в лог-файл
    test_name = request.node.name
    logger.info(f'Запуск теста: {test_name}')

    # Return the driver instance
    return driver



@pytest.fixture(scope="function")
def navigate_to_registration_page(setup, logger):
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
def navigate_to_authorization_page(setup, logger):
    pytest.driver = setup
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))  # Ждем загрузки страницы с формой "Авторизация"
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
