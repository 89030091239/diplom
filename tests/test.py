import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password, valid_phone, not_valid_phone, not_valid_password, not_valid_email, \
    not_valid_login, not_valid_acc_number, not_correct_phone, not_correct_email, special_characters


def test_registration_with_empty_fields(navigate_to_registration_page):
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'button').text == "Зарегистрироваться"
    # Проверям на подсказки ошибок пользователя
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ или +375XXX")]').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert pytest.driver.find_element(By.XPATH,
                                      "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]").text == "Длина пароля должна быть не менее 8 символов"
    assert pytest.driver.find_element(By.XPATH,
                                      "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]").text == "Длина пароля должна быть не менее 8 символов"


def test_password_confirmation_error_handling(navigate_to_registration_page):
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим не верный пароль
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(not_valid_password)
    # Нажимаем кнопку зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()
    # Проверяем появление подсказки об ошибке пользователя
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Пароли не совпадают')]").text == "Пароли не совпадают"


def test_for_work_with_incorrect_input_field_data_(navigate_to_registration_page):
    # Вводим данные в поле Имя и ожидаем подсказку об ошибке
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ss")
    # Кликаем мышью в любое место что-бы появилась подсказка об ошибке пользователя.
    # pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').click()
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(Keys.DELETE)

    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Аа1")
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(Keys.DELETE)

    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("А")
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(Keys.DELETE)

    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Аа")
    # Ждем что подсказка не появилась
    assert WebDriverWait(pytest.driver, 5).until(EC.invisibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))

    # Вводим данные в поле Фамилия и ожидаем подсказку об ошибке
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("Ss")
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    # Очищаем поле
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(Keys.DELETE)

    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("Аа1")
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(Keys.DELETE)

    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("А")
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(Keys.DELETE)

    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("Аа")
    # Ждем что подсказка не появилась
    assert WebDriverWait(pytest.driver, 5).until(EC.invisibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))


def test_for_work_with_incorrect_input_phone_or_email(navigate_to_registration_page):
    # Вводим данные в поле телефон или емайл и ожидаем подсказку об ошибке
    pytest.driver.find_element(By.ID, 'address').send_keys(not_correct_phone)
    """Если раскомментировать эту строку, тест будет зеленый)"""
    # # Кликаем мышью в любое место что-бы появилась подсказка об ошибке пользователя.
    # pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').click()
    # Проверяем на ошибку
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ или +375XXX")]').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    # Очищаем поле
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим данные в поле телефон или емайл и ожидаем подсказку об ошибке
    pytest.driver.find_element(By.ID, 'address').send_keys(not_correct_email)
    # # Кликаем мышью в любое место что-бы появилась подсказка об ошибке пользователя.
    # pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').click()
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ или +375XXX")]').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    # Очищаем поле
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим корретные данные в поле телефон или емайл и ожидаем что ошибки нет
    pytest.driver.find_element(By.ID, 'address').send_keys(valid_email)
    # # Кликаем мышью в любое место что-бы появилась подсказка об ошибке пользователя.
    # pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').click()
    assert WebDriverWait(pytest.driver, 5).until(EC.invisibility_of_element_located(
        (By.XPATH, '//span[contains(text(),"Введите телефон в формате +7ХХХХХХХХХХ или +375XXX")]')))


    """Так я и не победил выпадающий список с регионами"""
# def test_for_work_input_fields_region_with_drop_down_list(navigate_to_registration_page):
#     assert pytest.driver.find_element(By.XPATH,
#                                       "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]").text == "Регион"
#     pytest.driver.find_element(By.XPATH,
#                                "/html/body/div[1]/main/section[2]/div/div/div/form/div[2]/div/div/input").send_keys("Алтайский край")
#     list_element = pytest.driver.find_element(By.XPATH,
#                                               "/html/body/div[1]/main/section[2]/div/div/div/form/input")
#
#     actions = ActionChains(pytest.driver)
#
#     actions.move_to_element(list_element).click().perform()
#     actions.move_by_offset(0, 50).perform()
#     actions.move_by_offset(0, -50).perform()


def test_work_icons_eyes(navigate_to_registration_page):
    # Проверяем что иконка "Глаз" в поле пароль закрыта
    assert pytest.driver.find_element(By.ID, "password").get_attribute("type") == "password"
    # Нажимаем на иконку глаз в поле ввода пароль
    pytest.driver.find_element(By.XPATH,
                               "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/*[1]").click()
    # Проверяем что иконка "Глаз" открыта
    assert pytest.driver.find_element(By.ID, "password").get_attribute("type") == "text"
    # Нажимаем на иконку глаз в поле ввода пароль
    pytest.driver.find_element(By.XPATH,
                               "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/*[1]").click()
    # Проверяем что иконка "Глаз" в поле пароль закрыта
    assert pytest.driver.find_element(By.ID, "password").get_attribute("type") == "password"

    # Проверяем что иконка "Глаз" в поле подтверждения пароля закрыта
    assert pytest.driver.find_element(By.ID, "password-confirm").get_attribute("type") == "password"
    # Нажимаем на иконку глаз в поле подтверждения пароля
    pytest.driver.find_element(By.XPATH,
                               "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[2]/*[1]").click()
    # Проверяем что иконка "Глаз" открыта
    assert pytest.driver.find_element(By.ID, "password-confirm").get_attribute("type") == "text"
    # Нажимаем на иконку глаз в поле ввода пароль
    pytest.driver.find_element(By.XPATH,
                               "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[2]/*[1]").click()
    # Проверяем что иконка "Глаз" в поле подтверждения пароля закрыта
    assert pytest.driver.find_element(By.ID, "password-confirm").get_attribute("type") == "password"


def test_login_with_valid_phone(navigate_to_authorization_page):
    # Вводим номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_phone)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления главной страницы пользователя
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/span[1]')))
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]/span[1]').text == valid_phone


def test_login_with_not_valid_phone(navigate_to_authorization_page):
    # Вводим не верный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys(not_valid_phone)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления сообщения "Неверный логин или пароль"
    WebDriverWait(pytest.driver, 1).until(EC.presence_of_element_located(
        (By.ID, 'form-error-message')))
    # Проверяем, что появилось сообщение "Неверный логин или пароль"
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_login_with_not_valid_password(navigate_to_authorization_page):
    # Вводим номер не верный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_phone)
    # Вводим не верный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(not_valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления сообщения "Неверный логин или пароль"
    WebDriverWait(pytest.driver, 1).until(EC.presence_of_element_located(
        (By.ID, 'form-error-message')))
    # Проверяем, что появилось сообщение "Неверный логин или пароль"
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_login_with_valid_email(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Почта"
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-mail').text == "Почта"
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления главной страницы пользователя
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]/span[1]')))
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]/span[1]').text == valid_email


def test_login_with_not_valid_email(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Почта"
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-mail').text == "Почта"
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys(not_valid_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления сообщения "Неверный логин или пароль"
    WebDriverWait(pytest.driver, 1).until(EC.presence_of_element_located(
        (By.ID, 'form-error-message')))
    # Проверяем, что появилось сообщение "Неверный логин или пароль"
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_login_with_not_valid_user_name(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Логин"
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-login').text == "Логин"
    # Вводим логин
    pytest.driver.find_element(By.ID, 'username').send_keys(not_valid_login)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления сообщения "Неверный логин или пароль"
    WebDriverWait(pytest.driver, 1).until(EC.presence_of_element_located(
        (By.ID, 'form-error-message')))
    # Проверяем, что появилось сообщение "Неверный логин или пароль"
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_link_work_forgot_password(navigate_to_authorization_page):
    # Нажимаем на ссылку "Забыл пароль"
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Восстановление пароля"
    assert pytest.driver.find_element(By.XPATH, "// img[contains( @ alt, 'Captcha')]")


def test_negative_authorization_with_the_social_network_ya(navigate_to_authorization_page):
    # Нажимаем на кнопку входа с помощью входа с помощью соц. сетей Яндекс
    pytest.driver.find_element(By.XPATH, '//*[@id="oidc_ya"]').click()
    # # Почему-то после первого клика страница с формой перезагружается
    # pytest.driver.find_element(By.XPATH, '//*[@id="oidc_ya"]').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, "h1")
    pytest.driver.find_element(By.ID, 'passp-field-login').send_keys('your_name_in_yandex')
    pytest.driver.find_element(By.ID, 'passp:sign-in').click()
    pytest.driver.find_element(By.ID, 'passp-field-passwd').send_keys("your_password")
    pytest.driver.find_element(By.ID, 'password-toggle').click()
    pytest.driver.find_element(By.ID, 'passp:sign-in').click()
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "field:input-passwd:hint")))
    # Яндекс не пускает пароль(хотя пароль верный, внимательно проверил)
    assert pytest.driver.find_element(By.ID, "field:input-passwd:hint").text == "Неверный пароль"


def test_transition_to_page_authorization_with_the_social_network_ok(navigate_to_authorization_page):
    # Нажимаем на кнопку входа с помощью входа с помощью соц. сетей Однокласники
    pytest.driver.find_element(By.ID, 'oidc_ok').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.title_is("Одноклассники"))
    # Проверяем, что мы на нужной нам странице
    assert pytest.driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[1]/div').text == "Одноклассники"
    pytest.driver.back()
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))  # Ждем загрузки страницы с формой "Авторизация"
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"


def test_transition_to_page_authorization_with_the_social_network_mail(navigate_to_authorization_page):
    # Нажимаем на кнопку входа с помощью входа с помощью соц. сетей Майл
    pytest.driver.find_element(By.ID, 'oidc_mail').click()
    # time.sleep(20)
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    # Проверяем, что мы на нужной нам странице <h1>Необходим доступ к вашим данным</h1>
    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "Необходим доступ к вашим данным"
    pytest.driver.back()
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))  # Ждем загрузки страницы с формой "Авторизация"
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"


def test_transition_to_page_authorization_with_the_social_network_vk(navigate_to_authorization_page):
    # Нажимаем на кнопку входа с помощью входа с помощью соц. сетей VK
    pytest.driver.find_element(By.ID, 'oidc_vk').click()
    # time.sleep(20)
    # Проверяем, что мы на нужной нам странице <div class="box_msg_gray box_msg_padded">Для продолжения вам необходимо войти <b>ВКонтакте</b>.</div>
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="oauth_wrap_content"]/div[2]/div').text == "Для продолжения вам необходимо войти ВКонтакте."
    pytest.driver.back()
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1')))  # Ждем загрузки страницы с формой "Авторизация"
    # Проверяем, что нужная нам форма присутствует на странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"


def test_user_agreement_links(navigate_to_authorization_page):
    # Нажимаем на ссылку пользовательского соглашения
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    assert pytest.driver.find_element(By.XPATH, "h1")  # Текст не смог привязать


def test_login_with_not_valid_acc_number(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Лицевой счёт"
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').text == "Лицевой счёт"
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys(not_valid_acc_number)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ожидание появления сообщения "Неверный логин или пароль"
    WebDriverWait(pytest.driver, 1).until(EC.presence_of_element_located(
        (By.ID, 'form-error-message')))
    # Проверяем, что появилось сообщение "Неверный логин или пароль"
    assert pytest.driver.find_element(By.XPATH,
                                      '//*[@id="form-error-message"]').text == "Неверный логин или пароль"


def test_checkbox_remember_me(navigate_to_authorization_page):
    # Проверяем что чек-бокс называется "Запомнить меня"
    assert pytest.driver.find_element(By.XPATH,
                                      "//*[@id='page-right']/div/div/div/form/div[3]/div").text == "Запомнить меня"
    # Проверяем, что у чек-бокса стоит галка
    class_attribute = pytest.driver.find_element(By.XPATH,
                                                 "//*[@id='page-right']/div/div/div/form/div[3]/div").get_attribute(
        'class')
    expected_classes = ["rt-checkbox rt-checkbox--checked"]
    for class_name in expected_classes:
        assert class_name in class_attribute
    # Снимаем галку
    pytest.driver.find_element(By.XPATH, "//*[@id='page-right']/div/div/div/form/div[3]/div").click()
    # Проверяем что галка снята
    pytest.driver.find_element(By.XPATH, "//*[@id='page-right']/div/div/div/form/div[3]/div").get_attribute(
        'class') == "rt-checkbox"
    # Ставим галку на место
    pytest.driver.find_element(By.XPATH, "//*[@id='page-right']/div/div/div/form/div[3]/div").click()
    # Проверяем, что у чек-бокса стоит галка
    class_attribute = pytest.driver.find_element(By.XPATH,
                                                 "//*[@id='page-right']/div/div/div/form/div[3]/div").get_attribute(
        'class')
    expected_classes = ["rt-checkbox rt-checkbox--checked"]
    for class_name in expected_classes:
        assert class_name in class_attribute


def test_enter_incorrect_phone_number(navigate_to_authorization_page):
    # Вводим данные в поле телефон и ожидаем подсказку об ошибке
    pytest.driver.find_element(By.ID, 'username').send_keys(not_correct_phone)
    # Проверяем на ошибку
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[contains(text(),"Неверный формат телефона")]').text == "Неверный формат телефона"

    # Очищаем поле
    pytest.driver.find_element(By.ID, 'username').send_keys(Keys.CONTROL + 'a')
    pytest.driver.find_element(By.ID, 'username').send_keys(Keys.DELETE)

    # Вводим корретные данные в поле телефон и ожидаем что ошибки нет
    pytest.driver.find_element(By.ID, 'username').send_keys(not_valid_phone)
    assert WebDriverWait(pytest.driver, 5).until(EC.invisibility_of_element_located(
        (By.XPATH, '//span[contains(text(),"Неверный формат телефона")]')))


def test_enter_special_characters_in_the_username_field(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Логин"
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-login').text == "Логин"
    # Вводим спецсимволы
    pytest.driver.find_element(By.ID, 'username').send_keys(special_characters)
    # Ни какой ошибки не выводится
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[contains(text(),"Неверный формат логина")]').text == "Неверный формат логина"


def test_input_less_12_characters_in_acc_number(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Лицевой счёт"
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').text == "Лицевой счёт"
    # Вводим ЛС меньше 12 знаков
    pytest.driver.find_element(By.ID, 'username').send_keys(12345678910)
    """Если здесь щелкнуть мышкой по экрану или перейти в другое поле, тест будет зеленый """
    # Проверяем на ошибку
    assert pytest.driver.find_element(By.XPATH,
                                      "//span[contains(text(),'Проверьте, пожалуйста, номер лицевого счета')]").text == "Проверьте, пожалуйста, номер лицевого счета"


def test_input_more_than_12_characters_in_acc_number(navigate_to_authorization_page):
    # Переключаемся вручную на таб "Лицевой счёт"
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Проверяем что таб переключен
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').text == "Лицевой счёт"
    # Вводим ЛС меньше 12 знаков
    pytest.driver.find_element(By.ID, 'username').send_keys(1234567891011)
    # Проверяем на ошибку
    value = pytest.driver.find_element(By.XPATH,
                                       '//*[@id="page-right"]/div/div/div/form/div[1]/input[2]').get_attribute("value")
    assert len(value) == 12
