# Lab 03 - Kiểm thử Form Đăng nhập bằng Selenium

Đây là dự án tự động hóa kiểm thử cho form đăng nhập theo yêu cầu của Lab 03 - Introduction to Software Engineering.

## Yêu cầu hệ thống

* Python 3.8+
* Trình duyệt Google Chrome
* ChromeDriver tương thích với phiên bản Chrome

## Hướng dẫn cài đặt và chạy test

1.  **Clone repository về máy:**
    ```bash
    git clone [https://github.com/GiaLe2005/selenium-automation-test.git](https://github.com/GiaLe2005/selenium-automation-test.git)
    cd selenium-automation-test
    ```

2.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install selenium webdriver-manager
    ```

3.  **Chạy test:**
    Mở terminal trong thư mục dự án và chạy lệnh sau:
    ```bash
    python test_login.py
    ```
    *Lưu ý: Script sẽ tự động tải về ChromeDriver phiên bản phù hợp.*

4.  **Xem kết quả:**
    * Kết quả của từng test case sẽ được in ra trong terminal.
    * Ảnh chụp màn hình làm bằng chứng sẽ được tự động lưu vào thư mục `/screenshots`.

## Sơ đồ Use Case

![Sơ đồ Use Case](use-case.png)