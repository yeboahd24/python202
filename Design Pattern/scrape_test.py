from concurrent.futures import ThreadPoolExecutor
import threading
import time
import requests
state = threading.Lock()

def get_google(base_url):
	state.acquire()
	return requests.get(base_url)
	time.sleep(.2)
	state.release()

def get_python(base_url):
	state.acquire()
	return requests.get(base_url)
	time.sleep(.2)
	state.release()

def main():
	print('Testing...')
	with ThreadPoolExecutor(max_workers=3) as executor:
		task1 = executor.submit(get_google, ('https://www.google.com'))
		task1 = executor.submit(get_python, ('https://www.google.org'))

if __name__ == '__main__':
	main()
