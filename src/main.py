import os
import requests

import os 
from playwright.sync_api import sync_playwright

URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_telegram(caminho_imagem: str, legenda: str = "Atividades do portal SIGAA"):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

    with open(caminho_imagem, "rb") as img:
        r = requests.post(
            url,
            data={"chat_id": TELEGRAM_CHAT_ID, "caption": legenda},
            files={"photo": img},
            timeout=30,
        )
    r.raise_for_status()

def main():
    caminho_print = "screenshot.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL)
        page.locator('[name="user.login"]').fill(USERNAME)
        page.locator('[name="user.senha"]').fill(PASSWORD)
        page.locator('[value="Entrar"]').click()

        page.locator('[id="avaliacao-portal"]').screenshot(path=caminho_print)
        print("Login successful!")

        browser.close()

        enviar_telegram(caminho_print, "Relatório do Portal SIGAA")
        print("Print enviado ao Telegram!")

if __name__ == "__main__":
    main()