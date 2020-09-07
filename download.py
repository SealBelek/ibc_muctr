import requests
import sys
import os

if len(sys.argv) < 4+1:
  exit()

login = sys.argv[1]
password = sys.argv[2]
bookUrl = sys.argv[3]
pages = sys.argv[4]

s=requests.Session()
data={"family":login, "library_card_number":password}
url = "https://lib.muctr.ru/reader/login"
r = s.post(url, data)

for i in range(1, int(pages)):
  response = s.get(bookUrl + f'{i}')
  file = open(f"{i}.png", "wb")
  while(file.write(response.content) == 0):
    pass
    
os.system('files=$(ls -1v *.png); convert $files book.pdf')
