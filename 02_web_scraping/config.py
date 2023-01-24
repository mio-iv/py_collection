import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


ROOT = os.path.dirname(__file__)    # pyProgram本体
DOWNLOAD_DIR = ROOT+r'/download'

def set_driver():
    '''chromedriver設定'''
    chromeOptions = webdriver.ChromeOptions()   # option設定
    prefs = {}
    prefs["credentials_enable_service"]=False                             # パスワード保存のポップアップを無効
    prefs["profile.default_content_setting_values.notifications"]=False   # 通知ポップアップを無効
    prefs["download.default_directory"]=DOWNLOAD_DIR                      # ダウンロード先フォルダの設定

    chromeOptions.add_experimental_option('prefs', prefs)
    chromeOptions.add_experimental_option('excludeSwitches',
        [
            'enable-automation',    # 「自動テストソフトウェアによって制御されています」を非表示
            'enable_logging'    # [Getting Default Adapter failed]エラー回避：enable_logging
            ]    
    )
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),   # driver自動インストール
        options=chromeOptions
    )
    return driver