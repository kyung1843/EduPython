#라이브러리 사용
import urllib.request

url = "http://www.yes24.com/main/default.aspx"

f= urllib.request.urlopen(url)

#인코딩
encoding = f.info().get_content_charset()

text = f.read(1000).decode(encoding)

print(text)

