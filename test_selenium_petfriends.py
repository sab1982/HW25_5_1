import time


def test_petfriends(web_browser):
    web_browser.get("https://petfriends.skillfactory.ru")
    time.sleep(5)

    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()
    time.sleep(2)
    field_link = web_browser.find_element_by_xpath("//a[@href='/login']")
    field_link.click()
    time.sleep(2)
    field_email = web_browser.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("1@3.ru")
    time.sleep(2)
    field_password = web_browser.find_element_by_id("pass")
    field_password.clear()
    field_password.send_keys("1234567")

    btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)

    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "Login or pass error!"
