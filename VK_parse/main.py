from bs4 import BeautifulSoup as bf
import requests


def check_null(string):
	if string:
		return string.strip()
	else:
		return "NULL"


def check_data(string):
	if string:
		if string == "Подробная информация":
			return "NULL"
		else:
			if ":" in string:
				arr = string.split(': ')
				if arr[0] == "Город":
					return f"Город         | {arr[1]}"
				elif arr[0] == "Образование":
					return f"Образование   | {arr[1]}"
				elif arr[0] == "Место работы":
					return f"Место работы  | {arr[1]}"
			else:
				return str( string )
	else:
		return "NULL"


file = open("data.txt", "w")

for i in range(20):
	base = "https://vk.com/id"
	link = base + str( 200 + i )

	markup = requests.get(link)

	soup = bf( markup.text, "lxml" )

	print( f"ID: {link}" )
	print(f"Фамилия и имя | {soup.h2.text}")
	print(f"Время входа   | {check_null(soup.select_one('.pp_last_activity_text').text)}")

	file.write( f"ID: {link}\n" )
	file.write( f"Фамилия и имя | {soup.h2.text}\n" )
	file.write( f"Время входа   | {check_null( soup.select_one( '.pp_last_activity_text' ).text )}\n" )

	data = soup.select(".OwnerInfo__rowCenter")

	for dat in data:
		info = check_data(dat.text)
		if info != "NULL":
			print( info )
			file.write( str(info) + "\n" )

	print("")
	file.write("\n")

file.close()
