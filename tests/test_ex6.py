# tests.py
from django.test import LiveServerTestCase
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.auth.models import User
from selenium.webdriver.chrome.options import Options


class SimpleSeleniumTest(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")  # تشغيل Chrome في وضع headless
        # ChromeDriver المناسب لنسخة Chrome الحالية
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        # إنشاء مستخدم تجريبي لاختبارات login
        User.objects.create_user(username='admin', password='admin')

    def tearDown(self):
        self.driver.quit()

    def test_admin_page(self):
        # تأكد من URL صفحة login admin page
        self.driver.get(f"{self.live_server_url}/admin/")

        # self.assertIn("admin", self.driver.title)
        self.assertIn("admin", self.driver.page_source)


# arrange fixture for selenium driver Phase1
@pytest.fixture(scope="class")
def selenium_driver(request):
    options = Options()
    options.add_argument("--headless")  # تشغيل Chrome في وضع headless
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()


@pytest.mark.usefixtures("selenium_driver")
class TestSeleniumLogin:
    def test_login(self, selenium_driver, live_server):
        # إنشاء مستخدم تجريبي لاختبارات login
        User.objects.create_user(username='admin', password='admin')

        selenium_driver.get(f"{live_server.url}/admin/")

        username_input = selenium_driver.find_element(By.NAME, "username")
        password_input = selenium_driver.find_element(By.NAME, "password")
        login_button = selenium_driver.find_element(
            By.XPATH, '//input[@type="submit"]')

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_button.click()

        # الانتظار حتى يتم تحميل الصفحة التالية

        assert "Log in | Django site admin" in selenium_driver.page_source
