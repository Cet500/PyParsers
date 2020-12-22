from bs4 import BeautifulSoup as bf
from urllib.parse import quote

import requests
import pymysql

con = pymysql.connect("localhost", "root", "root", "rgr_parse")
cur = con.cursor()

print("==============================================")
print("================== РИЕЛТОРЫ ==================")
print("==============================================")
print("")

alfavit = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЮЯ"
base_url = "https://reestr.rgr.ru/search-result/?type=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8+%D1%80%D0%B8%D1%8D%D0%BB%D1%82%D0%BE%D1%80%D0%B0&zapros=&char="

for letter in alfavit:
	markup = requests.get(base_url + quote(letter))
	soup = bf( markup.text, "lxml" )
	data = soup.select("tr")

	print(f"================== {letter} ==================")
	print()

	for dat in data:
		arr = [i for i in range(0, 8)]
		temp = dat.select_one(".ttl").text.split(" ")

		arr[0] = temp[1]
		arr[1] = temp[0]
		arr[2] = temp[2]
		arr[3] = dat.select(".desc-row")[0].text.strip()
		arr[4] = dat.select(".desc-row")[1].text
		arr[5] = dat.select_one(".raiting").text
		arr[6] = dat.select_one(".attestat").text
		arr[7] = dat.select_one(".attestat-date").text.replace("Срок действия –   ", "")

		for ar in arr:
			print(ar)

		cur.execute( """INSERT INTO `data_rieltors`
						( `name`, `lastname`, `patronymic`, `company`, `city`, `raiting`, `attestat`, `date` )
						VALUES ( %s, %s, %s, %s, %s, %s, %s, %s );""",
					( arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7] ) )

		con.commit()

		print()

print("==============================================")
print("================= ОРГАНИЗАЦИИ ================")
print("==============================================")
print("")

alfavit = "123456789АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ"
base_url = "https://reestr.rgr.ru/search-result/?type=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8+%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%BE&zapros=&char="

for letter in alfavit:
	markup = requests.get(base_url + quote(letter))
	soup = bf( markup.text, "lxml" )
	data = soup.select("tr")

	print(f"================== {letter} ==================")
	print()

	for dat in data:
		arr = [i for i in range(0, 5)]

		arr[0] = dat.select_one(".ttl").text
		arr[1] = dat.select_one(".desc-row").text
		arr[2] = dat.select_one(".raiting").text.replace("Рейтинг агентства в реестре: ", "")

		if dat.select_one(".attestat").text.strip() == "Сертификат  - нет":
			arr[3] = None
			arr[4] = None

		else:
			arr[3] = dat.select_one(".attestat").text
			arr[4] = dat.select_one(".attestat-date").text.replace("Срок действия –   ", "")

		cur.execute( """INSERT INTO `data_organizations`
						( `name`, `city`, `raiting`, `attestat`, `date` )
						VALUES ( %s, %s, %s, %s, %s );""",
		             ( arr[0], arr[1], arr[2], arr[3], arr[4] ) )

		con.commit()

		for ar in arr:
			print(ar)

		print()
