import requests

URL = 'http://127.0.0.1/'


def request_method():
	response = requests.get(URL, params={'name': 'wxj', 'age': 20})
	print(response.status_code)


if __name__ == '__main__':
	request_method()
