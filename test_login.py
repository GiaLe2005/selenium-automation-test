import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# --- CÀI ĐẶT CHUNG ---
# Lấy đường dẫn tuyệt đối đến thư mục chứa file script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Tạo đường dẫn đến chromedriver và file html
chromedriver_path = os.path.join(script_dir, 'chromedriver.exe')
html_file_path = os.path.join(script_dir, 'login.html')

# Khởi tạo WebDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Tạo thư mục 'screenshots' nếu chưa tồn tại
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

try:
    # Mở file HTML cục bộ
    driver.get('file:///' + html_file_path)
    time.sleep(1) # Chờ trang tải

    # --- TEST CASE 1: Đăng nhập thành công ---
    print("--- Running Test Case 1: Successful Login ---")
    driver.find_element(By.ID, 'username').send_keys('admin')
    driver.find_element(By.ID, 'password').send_keys('password123')
    driver.find_element(By.CLASS_NAME, 'login-button').click()
    time.sleep(1)
    message = driver.find_element(By.ID, 'message').text
    assert message == 'Login success'
    driver.save_screenshot('screenshots/01_successful_login.png')
    print("Test Case 1: PASSED")
    # Refresh trang để thực hiện test case tiếp theo
    driver.refresh()
    time.sleep(1)

    # --- TEST CASE 2: Sai thông tin đăng nhập ---
    print("\n--- Running Test Case 2: Failed Login ---")
    driver.find_element(By.ID, 'username').send_keys('admin')
    driver.find_element(By.ID, 'password').send_keys('wrongpassword')
    driver.find_element(By.CLASS_NAME, 'login-button').click()
    time.sleep(1)
    message = driver.find_element(By.ID, 'message').text
    assert message == 'Invalid username or password'
    driver.save_screenshot('screenshots/02_failed_login.png')
    print("Test Case 2: PASSED")
    driver.refresh()
    time.sleep(1)

    # --- TEST CASE 3: Bỏ trống trường thông tin ---
    print("\n--- Running Test Case 3: Empty Fields ---")
    driver.find_element(By.ID, 'username').send_keys('') # Để trống username
    driver.find_element(By.ID, 'password').send_keys('somepassword')
    driver.find_element(By.CLASS_NAME, 'login-button').click()
    time.sleep(1)
    message = driver.find_element(By.ID, 'message').text
    assert 'Vui lòng nhập đầy đủ' in message
    driver.save_screenshot('screenshots/03_empty_fields.png')
    print("Test Case 3: PASSED")
    driver.refresh()
    time.sleep(1)

    # --- TEST CASE 4: Link "Forgot password?" ---
    print("\n--- Running Test Case 4: Forgot Password Link ---")
    forgot_link = driver.find_element(By.CLASS_NAME, 'forgot-password')
    assert forgot_link.is_displayed()
    assert forgot_link.is_enabled()
    forgot_link.click()
    # Kiểm tra URL đã thay đổi (thêm #forgot)
    assert '#forgot' in driver.current_url
    driver.save_screenshot('screenshots/04_forgot_password_link.png')
    print("Test Case 4: PASSED")
    driver.back() # Quay lại trang chính
    time.sleep(1)

    # --- TEST CASE 5: Link "SIGN UP" ---
    print("\n--- Running Test Case 5: Sign Up Link ---")
    signup_link = driver.find_element(By.CSS_SELECTOR, '.signup-link a')
    assert signup_link.is_displayed()
    assert signup_link.is_enabled()
    signup_link.click()
    assert '#signup' in driver.current_url
    driver.save_screenshot('screenshots/05_signup_link.png')
    print("Test Case 5: PASSED")
    driver.back()
    time.sleep(1)

    # --- TEST CASE 6: Nút social login ---
    print("\n--- Running Test Case 6: Social Login Buttons ---")
    facebook_btn = driver.find_element(By.CSS_SELECTOR, '.social-icon.facebook')
    twitter_btn = driver.find_element(By.CSS_SELECTOR, '.social-icon.twitter')
    google_btn = driver.find_element(By.CSS_SELECTOR, '.social-icon.google')
    
    assert facebook_btn.is_displayed() and facebook_btn.is_enabled()
    assert twitter_btn.is_displayed() and twitter_btn.is_enabled()
    assert google_btn.is_displayed() and google_btn.is_enabled()
    
    driver.save_screenshot('screenshots/06_social_buttons.png')
    print("Test Case 6: PASSED")

    print("\n\nAll test cases passed successfully!")

finally:
    # Đóng trình duyệt sau khi hoàn thành
    time.sleep(3) # Chờ 3 giây để xem kết quả cuối cùng
    driver.quit()
    