import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Lấy 
HTML_FILE_PATH = 'file:///' + os.path.abspath('login.html')

class LoginAutomationTest(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        self.driver = webdriver.Chrome()
        self.driver.get(HTML_FILE_PATH)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # --- 6 TEST CASES HOÀN CHỈNH ---

    def test_1_successful_login(self):
        """[TC1] Kiểm tra đăng nhập thành công"""
        print("Running: test_1_successful_login")
        self.driver.find_element(By.ID, 'username').send_keys('admin')
        self.driver.find_element(By.ID, 'password').send_keys('12345')
        self.driver.find_element(By.CSS_SELECTOR, '.login-btn').click()
        time.sleep(1)
        
        # Kiểm tra URL đã chuyển sang trang dashboard.html
        self.assertIn('dashboard.html', self.driver.current_url)
        self.driver.save_screenshot('screenshots/TC1_successful_login.png')

    def test_2_incorrect_credentials(self):
        """[TC2] Sai thông tin đăng nhập"""
        print("Running: test_2_incorrect_credentials")
        self.driver.find_element(By.ID, 'username').send_keys('admin')
        self.driver.find_element(By.ID, 'password').send_keys('wrongpass')
        self.driver.find_element(By.CSS_SELECTOR, '.login-btn').click()
        time.sleep(1)

        # Kiểm tra thông báo lỗi có hiển thị không
        error_message = self.driver.find_element(By.ID, 'error-message')
        self.assertTrue(error_message.is_displayed())
        self.driver.save_screenshot('screenshots/TC2_incorrect_credentials.png')

    def test_3_empty_fields(self):
        """[TC3] Bỏ trống trường"""
        print("Running: test_3_empty_fields")
        # Không điền gì và nhấn login
        self.driver.find_element(By.CSS_SELECTOR, '.login-btn').click()
        time.sleep(1)
        # HTML5 validation sẽ ngăn form gửi đi, ta kiểm tra rằng URL không thay đổi
        self.assertNotIn('dashboard.html', self.driver.current_url)
        self.driver.save_screenshot('screenshots/TC3_empty_fields.png')

    def test_4_forgot_password_link(self):
        """[TC4] Link Forgot password?"""
        print("Running: test_4_forgot_password_link")
        forgot_link = self.driver.find_element(By.ID, 'forgot-password')
        self.assertTrue(forgot_link.is_displayed() and forgot_link.is_enabled())
        # forgot_link.click() # Bỏ comment dòng này nếu muốn test click
        self.driver.save_screenshot('screenshots/TC4_forgot_password_link.png')

    def test_5_signup_link(self):
        """[TC5] Link SIGN UP"""
        print("Running: test_5_signup_link")
        signup_link = self.driver.find_element(By.ID, 'signup')
        self.assertTrue(signup_link.is_displayed() and signup_link.is_enabled())
        # signup_link.click() # Bỏ comment dòng này nếu muốn test click
        self.driver.save_screenshot('screenshots/TC5_signup_link.png')

    def test_6_social_login_buttons(self):
        """[TC6] Nút social login"""
        print("Running: test_6_social_login_buttons")
        fb_button = self.driver.find_element(By.ID, 'fb-login')
        tw_button = self.driver.find_element(By.ID, 'tw-login')
        gg_button = self.driver.find_element(By.ID, 'gg-login')
        
        self.assertTrue(fb_button.is_displayed())
        self.assertTrue(tw_button.is_displayed())
        self.assertTrue(gg_button.is_displayed())
        self.driver.save_screenshot('screenshots/TC6_social_login_buttons.png')

# Đoạn code này để chạy các test case
if __name__ == '__main__':
    unittest.main(verbosity=2)