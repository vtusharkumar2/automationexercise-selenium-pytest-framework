import pytest
import pytest_html
import os
from datetime import datetime
from selenium import webdriver
import base64
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    
    # 🔥 Required for GitHub Actions
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    
    driver.get("https://automationexercise.com/login")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver", None)

        if report.failed and driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join("screenshots", screenshot_name)

            driver.save_screenshot(screenshot_path)

            # 🔥 FIX: embed image
            with open(screenshot_path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extras", [])
            extra.append(pytest_html.extras.image(encoded, mime_type="image/png"))
            report.extras=extra


