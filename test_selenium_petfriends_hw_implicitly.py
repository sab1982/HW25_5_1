import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('chromedriver.exe')
    # Неявное ожидание пока необходимые элементы загрузятся
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_all_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('1@3.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на ссылку мои питомцы
    pytest.driver.find_element_by_css_selector("a[href='/my_pets']").click()
    # Получаем данные пользователя
    pets = pytest.driver.find_elements_by_css_selector('div[class=".col-sm-4 left"]')
    # Получаем список питомцев на странице пользователя
    table_pets = pytest.driver.find_elements_by_css_selector('table[class="table table-hover"]>tbody>tr')

    pets_index = pets[0].text.split(" ")[2]
    pets_number = pets_index.split("\n")

    # Проверяем, что на странице пользователя присутствуют все питомцы
    assert pets_number[0] != str(len(table_pets))


def test_my_pets_half_photo():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('1@3.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на ссылку мои питомцы
    pytest.driver.find_element_by_css_selector("a[href='/my_pets']").click()
    # Получаем список питомцев на странице пользователя
    table_pets = pytest.driver.find_elements_by_css_selector('table[class="table table-hover"]>tbody>tr')
    #Получаем фото питомцев
    images = pytest.driver.find_elements_by_css_selector("th[scope='row']>img[src='']")

    print("len images", len(images))
    print("table_pets", len(table_pets)/2)

    # Проверяем, что на странице пользователя хотя бы половина питомцев с фото
    assert len(images) <= (len(table_pets))/2


def test_my_pets_name_age_animal_type():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('1@3.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на ссылку мои питомцы
    pytest.driver.find_element_by_css_selector("a[href='/my_pets']").click()
    # Получаем список питомцев на странице пользователя
    table_pets = pytest.driver.find_elements_by_css_selector("table[class='table table-hover']>tbody>tr>td")

    for i in range(len(table_pets)):
        if (i+4)%4 == 0:
            names = table_pets[i].text
            print("names", names)
            assert names != ''
        elif ((i-1)+4)%4 == 0:
            types = table_pets[i].text
            assert types != ''
        elif ((i-2)+4)%4 == 0:
            ages = table_pets[i].text
            assert ages != ''


def test_my_pets_name_different():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('1@3.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на ссылку мои питомцы
    pytest.driver.find_element_by_css_selector("a[href='/my_pets']").click()
    # Получаем список питомцев на странице пользователя
    table_pets = pytest.driver.find_elements_by_css_selector("table[class='table table-hover']>tbody>tr>td")
    names = []

    for i in range(len(table_pets)):
        if (i+4)%4 == 0:
            names.append(table_pets[i].text)

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            print(f"names[i]={names[i]} names[j]={names[j]}")
            assert names[i] != names[j]


def test_my_pets_different():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('1@3.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на ссылку мои питомцы
    pytest.driver.find_element_by_css_selector("a[href='/my_pets']").click()
    # Получаем список питомцев на странице пользователя
    table_pets = pytest.driver.find_elements_by_css_selector("table[class='table table-hover']>tbody>tr>td")

    names = []
    types = []
    ages = []
    for i in range(len(table_pets)):
        if (i+4)%4 == 0:
            names.append(table_pets[i].text)
        elif ((i - 1) + 4) % 4 == 0:
            types.append(table_pets[i].text)
        elif ((i - 2) + 4) % 4 == 0:
            ages.append(table_pets[i].text)

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if names[i] == names[j] and types[i] == types[j] and ages[i] == ages[j]:
                raise Exception("есть повторяющиеся животные")
