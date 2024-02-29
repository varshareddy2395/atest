import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    # Initialize WebDriver (make sure to provide the correct path to your webdriver executable)
    chrome_options = Options()
    service = webdriver.chrome.service.Service('C:\Program Files\chrome-win32\chrome.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver  # this is the teardown part, executed after the test function
    driver.quit()

def test_google_search(browser):
    # Open Google in the browser
    browser.get("https://www.google.com")

    # Find the search box and input a query
    search_box = browser.find_element("name", "q")
    search_box.send_keys("pytest with Selenium")

    # Submit the search
    search_box.send_keys(Keys.RETURN)

    # Verify that the search results page contains the expected text
    assert "pytest with Selenium" in browser.title

    # Open YouTube in the browser
    browser.get("https://www.youtube.com")

    # Verify that the YouTube page is opened
    assert "YouTube" in browser.title

if __name__ == "__main__":
    pytest.main(["-v", "sample.py"])
