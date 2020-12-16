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
		elif string == "Информация отсутствует":
			return "NULL"
		elif string == "Показать подробную информацию":
			return "NULL"
		else:
			if ":" in string:
				string = string.strip()
				arr = string.split(':\n')

				if arr[0] == "День рождения":
					return f"День рождения      | {arr[1]}"
				elif arr[0] == "Город":
					return f"Город              | {arr[1]}"
				elif arr[0] == "Семейное положение":
					return f"Семейное положение | {arr[1]}"
				elif arr[0] == "Образование":
					return f"Образование        | {arr[1]}"
				elif arr[0] == "Место учёбы":
					return f"Место учёбы        | {arr[1]}"
				elif arr[0] == "Сайт":
					return f"Сайт               | {arr[1]}"
				elif arr[0] == "Языки":
					return f"Языки              | {arr[1]}"
				elif arr[0] == "Бабушка":
					return f"Бабушка            | {arr[1]}"
				elif arr[0] == "Дедушка":
					return f"Дедушка            | {arr[1]}"
				elif arr[0] == "Родители":
					return f"Родители           | {arr[1]}"
				elif arr[0] == "Мать":
					return f"Мать               | {arr[1]}"
				elif arr[0] == "Отец":
					return f"Отец               | {arr[1]}"
				elif arr[0] == "Братья, сёстры":
					return f"Братья, сёстры     | {arr[1]}"
				elif arr[0] == "Сестра":
					return f"Сестра             | {arr[1]}"
				elif arr[0] == "Брат":
					return f"Брат               | {arr[1]}"
				elif arr[0] == "Дети":
					return f"Дети               | {arr[1]}"
				elif arr[0] == "Дочь":
					return f"Дочь               | {arr[1]}"
				elif arr[0] == "Сын":
					return f"Сын                | {arr[1]}"
				elif arr[0] == "Моб. телефон":
					return f"Телефон            | {arr[1]}"
				elif arr[0] == "Доп. телефон":
					return f"Доп телефон        | {arr[1]}"
				elif arr[0] == "Instagram":
					return f"Instagram          | {arr[1]}"
				elif arr[0] == "Skype":
					return f"Skype              | {arr[1]}"
				elif arr[0] == "Twitter":
					return f"Twitter            | {arr[1]}"
				elif arr[0] == "Facebook":
					return f"Facebook           | {arr[1]}"
				elif arr[0] == "LiveJournal":
					return f"LiveJournal        | {arr[1]}"
				elif arr[0] == "Родной город":
					return f"Родной город       | {arr[1]}"
				elif arr[0] == "Место работы":
					return f"Место работы       | {arr[1]}"
				elif arr[0] == "Дом":
					return f"Дом                | {arr[1]}"
				elif arr[0] == "Место работы:":
					return f"Место работы       | {arr[1]}"
				elif arr[0] == "Вуз":
					return f"Вуз                | {arr[1]}"
				elif arr[0] == "Факультет":
					return f"Факультет          | {arr[1]}"
				elif arr[0] == "Специальность":
					return f"Специальность      | {arr[1]}"
				elif arr[0] == "Форма обучения":
					return f"Форма обучения     | {arr[1]}"
				elif arr[0] == "Статус":
					return f"Статус             | {arr[1]}"
				elif arr[0] == "Школа":
					return f"Школа              | {arr[1]}"
				elif arr[0] == "Войсковая часть":
					return f"Войсковая часть    | {arr[1]}"
				elif arr[0] == "Полит. предпочтения":
					return f"Полит предпочтения | {arr[1]}"
				elif arr[0] == "Главное в людях":
					return f"Главное в людях    | {arr[1]}"
				elif arr[0] == "Главное в жизни":
					return f"Главное в жизни    | {arr[1]}"
				elif arr[0] == "Отн. к курению":
					return f"Отнош. к курению   | {arr[1]}"
				elif arr[0] == "Отн. к алкоголю":
					return f"Отнош. к алкоголю  | {arr[1]}"
				elif arr[0] == "Вдохновляют":
					return f"Вдохновляют        | {arr[1]}"
				elif arr[0] == "Мировоззрение":
					return f"Мировоззрение      | {arr[1]}"
				elif arr[0] == "Деятельность":
					return f"Деятельность       | {arr[1]}"
				elif arr[0] == "Интересы":
					return f"Интересы           | {arr[1]}"
				elif arr[0] == "Любимая музыка":
					return f"Любимая музыка     | {arr[1]}"
				elif arr[0] == "Любимые фильмы":
					return f"Любимые фильмы     | {arr[1]}"
				elif arr[0] == "Любимые телешоу":
					return f"Любимые телешоу    | {arr[1]}"
				elif arr[0] == "Любимые книги":
					return f"Любимые книги      | {arr[1]}"
				elif arr[0] == "Любимые игры":
					return f"Любимые игры       | {arr[1]}"
				elif arr[0] == "Любимые цитаты":
					return f"Любимые цитаты     | {arr[1]}"
				elif arr[0] == "О себе":
					return f"О себе             | {arr[1]}"
				elif arr[0] == "Группы":
					return f"Группы             | {arr[1]}"

			else:
				return str( string )

	else:
		return "NULL"


def check_counter(counter):
	if counter:
		label = counter.select_one(".label").text
		count = counter.select_one(".count").text

		if label == "подписчик" or label == "подписчикa" or label == "подписчиков":
			print(f"Подписок           | {count}")
			file.write(f"Подписок           | {count}\n")

		elif label == "запись" or label == "записи" or label == "записей":
			print(f"Постов             | {count}")
			file.write(f"Постов             | {count}\n")

		elif label == "фотография" or label == "фотографии" or label == "фотографий":
			print(f"Фотографий         | {count}")
			file.write(f"Фотографий         | {count}\n")

		elif label == "отметка" or label == "отметки" or label == "отметок":
			print(f"Отметок            | {count}")
			file.write(f"Отметок            | {count}\n")

	else:
		return "NULL"


file = open("data.txt", "a")
file.write( f"==============================\n\n" )

for i in range(400):
	base = "https://vk.com/id"
	link = base + str( 600 + i )

	markup = requests.get(link)

	soup = bf( markup.text, "lxml" )

	print( f"ID: {link}" )
	file.write( f"ID: {link}\n" )

	if soup.select_one(".message_page_body"):
		print(f"Фамилия и имя      | ХЗ")
		print(f"Доступность        | Не существует")

		file.write( f"Фамилия и имя      | ХЗ\n" )
		file.write( f"Доступность        | Не существует\n" )

	elif soup.select_one("#login_blocked_img"):
		print(f"Фамилия и имя      | ХЗ")
		print(f"Доступность        | Заблокирована")

		file.write( f"Фамилия и имя      | ХЗ\n" )
		file.write( f"Доступность        | Заблокирована\n" )

	elif soup.select_one("#page_current_info"):
		if soup.select_one("#page_current_info").text == "Страница скрыта":
			print(f"Фамилия и имя      | {soup.select_one('.page_name').text}")
			print(f"Доступность        | Скрыта")

			file.write( f"Фамилия и имя      | {soup.select_one('.page_name').text}\n" )
			file.write( f"Доступность        | Скрыта\n" )

	else:
		print(f"Фамилия и имя      | {soup.select_one('.page_name').text.rstrip()}")
		print(f"Доступность        | Открыта")
		print(f"Время входа        | {check_null(soup.select_one('.profile_online_lv').text)}")

		file.write( f"Фамилия и имя      | {soup.select_one('.page_name').text}\n" )
		file.write( f"Доступность        | Открыта\n" )
		file.write( f"Время входа        | {check_null( soup.select_one( '.profile_online_lv' ).text)}\n" )

		data = soup.select(".profile_info_row")

		for dat in data:
			info = check_data(dat.text)
			if info != "NULL":
				print( info )
				file.write( str(info) + "\n" )

		counters = soup.select(".page_counter")

		for counter in counters:
			count = check_counter(counter)

	print("")
	file.write("\n")

file.close()
