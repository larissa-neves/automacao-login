import os 
from playwright.sync_api import sync_playwright

URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(URL)
        page.locator('[name="user.login"]').fill(USERNAME)
        page.locator('[name="user.senha"]').fill(PASSWORD)
        page.locator('[value="Entrar"]').click()
        page.locator('[id="avaliacao-portal"]').screenshot(path='screenshot.png')

        print("Login successful!")

        pause = input("Press Enter to close the browser...")

        browser.close()

if __name__ == "__main__":
    main()