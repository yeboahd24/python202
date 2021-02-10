#!usr/bin/env/python3
import requests
# from requests_futures.sessions import  FuturesSession
from concurrent.futures import ProcessPoolExecutor
from time import sleep
from bs4 import BeautifulSoup as BS

Making multiple requests 
def task(url):
	data = requests.get(url)
	soup = BS(data.content, 'lxml')
	print(soup.encode('utf-8'))

def main():
	with ProcessPoolExecutor(max_workers=2) as executor:
		task1 = executor.submit(task, 'https://uenr.edu.gh')
		task2 = excutor.submit(task, 'https://google.com.gh')
		sleep(3)




# if __name__ == '__main__':
# 	main()

# s = requests.Session()
# r = s.get('https://uenr.edu.gh')
# print(r.text)






# with requests.Session() as session:
# 	print(list(map(session.get, urls)))

# def multiple_request():
# 	with FuturesSession(executor=ProcessPoolExecutor(max_workers=8)) as session:
# 		futures = [session.get(url) for url in urls]
# 		for future in futures:
# 			future.result()


# if __name__ == '__main__':
# 	multiple_request()


