import json
import requests
code = input().lower()
url = (f'http://www.floatrates.com/daily/{code}.json') #site
op = requests.get(url).json()
dict_currencies = {}
if code != 'usd':
	dict_currencies['usd'] = float(op['usd']['rate'])
if code != 'eur':
	dict_currencies['eur'] = float(op['eur']['rate'])


while True:
	received_code = input().lower()
	if received_code == '':
		break
	amount = int(input())
	print('Checking the cache...')
	rate = float(op[received_code]['rate'])
	if received_code in dict_currencies.keys():
		print('Oh! It is in the cache!')
	else:
		print('Sorry, but it is not in the cache!')
		dict_currencies[received_code] = rate
	result = round(amount * rate, 2)
	print(f'You received {result} {received_code.upper()}.')
