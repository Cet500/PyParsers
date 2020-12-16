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
				string = string.strip()
				arr = string.split(':\n')

				if arr[0] == "День рождения":
					return f"День рождения | {arr[1]}"
				elif arr[0] == "Город":
					return f"Город         | {arr[1]}"
				elif arr[0] == "Образование":
					return f"Образование   | {arr[1]}"
				elif arr[0] == "Место работы":
					return f"Место работы  | {arr[1]}"
				elif arr[0] == "Сайт":
					return f"Сайт          | {arr[1]}"
			else:
				return str( string )
	else:
		return "NULL"


file = open("data.txt", "a")
file.write( f"==============================\n\n" )

for i in range(50):
	base = "https://vk.com/id"
	link = base + str( 200 + i )

	markup = requests.get(link)

	soup = bf( markup.text, "lxml" )

	print( f"ID: {link}" )
	file.write( f"ID: {link}\n" )

	if soup.select_one(".message_page_body"):
		print(f"Фамилия и имя | ХЗ")
		print(f"Доступность   | Не существует")

		file.write( f"Фамилия и имя | ХЗ\n" )
		file.write( f"Доступность   | Не существует\n" )

	elif soup.select_one("#login_blocked_img"):
		print(f"Фамилия и имя | ХЗ")
		print(f"Доступность   | Заблокирована")

		file.write( f"Фамилия и имя | ХЗ\n" )
		file.write( f"Доступность   | Заблокирована\n" )

	elif soup.select_one("#page_current_info"):
		if soup.select_one("#page_current_info").text == "Страница скрыта":
			print(f"Фамилия и имя | {soup.select_one('.page_name').text}")
			print(f"Доступность   | Скрыта")

			file.write( f"Фамилия и имя | {soup.select_one('.page_name').text}\n" )
			file.write( f"Доступность   | Скрыта\n" )

	else:
		print(f"Фамилия и имя | {soup.select_one('.page_name').text}")
		print(f"Доступность   | Открыта")
		print(f"Время входа   | {check_null(soup.select_one('.profile_online_lv').text)}")

		file.write( f"Фамилия и имя | {soup.select_one('.page_name').text}\n" )
		file.write( f"Доступность   | Открыта\n" )
		file.write( f"Время входа   | {check_null( soup.select_one( '.profile_online_lv' ).text)}\n" )

		data = soup.select(".profile_info_row")

		for dat in data:
			info = check_data(dat.text)
			if info != "NULL":
				print( info )
				file.write( str(info) + "\n" )

	print("")
	file.write("\n")

file.close()
