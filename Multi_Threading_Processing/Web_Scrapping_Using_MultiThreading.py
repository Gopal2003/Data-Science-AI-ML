import threading
import requests
from bs4 import BeautifulSoup


urls = [
    'https://www.w3resource.com/python-exercises/BeautifulSoup/index.php',
    'https://www.w3resource.com/python-exercises/BeautifulSoup/python-beautifulsoup-exercise-1.php'
]

def fetch_content(url):
    responce = requests.get(url)

    # print(responce.content,"\n\n")
    soup = BeautifulSoup(responce.content,'html.parser')
    print(soup)
    print(f'Fetched {(len(soup.text))} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Web Pages Fetched!")