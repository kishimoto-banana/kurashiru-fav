import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


def fetch_fav_html():
    driver = webdriver.Remote(
        command_executor="http://chrome:4444/wd/hub",
    )
    driver.get("https://accounts.kurashiru.com/accounts/v1/login")

    email = driver.find_element(by=By.ID, value="login_email")
    email.send_keys(EMAIL)
    password = driver.find_element(by=By.ID, value="login_password")
    password.send_keys(PASSWORD)
    password.submit()

    driver.get("https://www.kurashiru.com/account/favorites")

    win_height = driver.execute_script("return window.innerHeight")

    # スクロール開始位置の初期値（ページの先頭からスクロールを開始する）
    last_top = 1

    # ページの最下部までスクロールする無限ループ
    while True:

        # スクロール前のページの高さを取得
        last_height = driver.execute_script("return document.body.scrollHeight")

        # スクロール開始位置を設定
        top = last_top

        # ページ最下部まで、徐々にスクロールしていく
        while top < last_height:
            top += int(win_height * 0.8)
            driver.execute_script("window.scrollTo(0, %d)" % top)
            time.sleep(0.5)

        # １秒待って、スクロール後のページの高さを取得する
        time.sleep(1)
        new_last_height = driver.execute_script("return document.body.scrollHeight")

        # スクロール前後でページの高さに変化がなくなったら無限スクロール終了とみなしてループを抜ける
        if last_height == new_last_height:
            break

        # 次のループのスクロール開始位置を設定
        last_top = last_height

    html = str(driver.page_source)
    driver.quit()

    return html
