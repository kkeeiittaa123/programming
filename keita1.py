# ライブラリの読み込み
from bs4 import BeautifulSoup
import urllib.request

# URL
url = "https://www.yahoo.co.jp/"
# URLにアクセス 
html = urllib.request.urlopen(url)
# HTMLをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")
# 出力
print(soup)