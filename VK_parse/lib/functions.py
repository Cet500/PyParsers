import database
from config import *


def check_null(string):
	# функция проверки пустого значения

	if string:
		return string.strip()
	else:
		return "NULL"


def check_data(string):
	# функция разбора и возврата данных профиля

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
					return "День рождения", f"{arr[1]}"
				elif arr[0] == "Город":
					return "Город", f"{arr[1]}"
				elif arr[0] == "Семейное положение":
					return "Семейное положение", f"{arr[1]}"
				elif arr[0] == "Образование":
					return "Образование", f"{arr[1]}"
				elif arr[0] == "Место учёбы":
					return "Место учёбы", f"{arr[1]}"
				elif arr[0] == "Сайт":
					return "Сайт", f"{arr[1]}"
				elif arr[0] == "Языки":
					return "Языки", f"{arr[1]}"
				elif arr[0] == "Бабушка":
					return "Бабушка", f"{arr[1]}"
				elif arr[0] == "Дедушка":
					return "Дедушка", f"{arr[1]}"
				elif arr[0] == "Родители":
					return "Родители", f"{arr[1]}"
				elif arr[0] == "Мать":
					return "Мать", f"{arr[1]}"
				elif arr[0] == "Отец":
					return "Отец", f"{arr[1]}"
				elif arr[0] == "Братья, сёстры":
					return "Братья, сёстры", f"{arr[1]}"
				elif arr[0] == "Сестра":
					return "Сестра", f"{arr[1]}"
				elif arr[0] == "Брат":
					return "Брат", f"{arr[1]}"
				elif arr[0] == "Дети":
					return "Дети", f"{arr[1]}"
				elif arr[0] == "Дочь":
					return "Дочь", f"{arr[1]}"
				elif arr[0] == "Сын":
					return "Сын", f"{arr[1]}"
				elif arr[0] == "Внуки":
					return "Внуки", f"{arr[1]}"
				elif arr[0] == "Внучка":
					return "Внучка", f"{arr[1]}"
				elif arr[0] == "Внук":
					return "Внук", f"{arr[1]}"
				elif arr[0] == "Моб. телефон":
					return "Телефон", f"{arr[1]}"
				elif arr[0] == "Доп. телефон":
					return "Доп телефон", f"{arr[1]}"
				elif arr[0] == "Instagram":
					return "Instagram", f"{arr[1]}"
				elif arr[0] == "Skype":
					return "Skype", f"{arr[1]}"
				elif arr[0] == "Twitter":
					return "Twitter", f"{arr[1]}"
				elif arr[0] == "Facebook":
					return "Facebook", f"{arr[1]}"
				elif arr[0] == "LiveJournal":
					return "LiveJournal", f"{arr[1]}"
				elif arr[0] == "Родной город":
					return "Родной город", f"{arr[1]}"
				elif arr[0] == "Место работы":
					return "Место работы", f"{arr[1]}"
				elif arr[0] == "Дом":
					return "Дом", f"{arr[1]}"
				elif arr[0] == "Место работы:":
					return "Место работы", f"{arr[1]}"
				elif arr[0] == "Вуз":
					return "Вуз", f"{arr[1]}"
				elif arr[0] == "Факультет":
					return "Факультет", f"{arr[1]}"
				elif arr[0] == "Специальность":
					return "Специальность", f"{arr[1]}"
				elif arr[0] == "Форма обучения":
					return "Форма обучения", f"{arr[1]}"
				elif arr[0] == "Статус":
					return "Статус", f"{arr[1]}"
				elif arr[0] == "Школа":
					return "Школа", f"{arr[1]}"
				elif arr[0] == "Войсковая часть":
					return "Войсковая часть", f"{arr[1]}"
				elif arr[0] == "Полит. предпочтения":
					return "Полит предпочтения", f"{arr[1]}"
				elif arr[0] == "Главное в людях":
					return "Главное в людях", f"{arr[1]}"
				elif arr[0] == "Главное в жизни":
					return "Главное в жизни", f"{arr[1]}"
				elif arr[0] == "Отн. к курению":
					return "Отнош. к курению", f"{arr[1]}"
				elif arr[0] == "Отн. к алкоголю":
					return "Отнош. к алкоголю", f"{arr[1]}"
				elif arr[0] == "Вдохновляют":
					return "Вдохновляют", f"{arr[1]}"
				elif arr[0] == "Мировоззрение":
					return "Мировоззрение", f"{arr[1]}"
				elif arr[0] == "Деятельность":
					return "Деятельность", f"{arr[1]}"
				elif arr[0] == "Интересы":
					return "Интересы", f"{arr[1]}"
				elif arr[0] == "Любимая музыка":
					return "Любимая музыка", f"{arr[1]}"
				elif arr[0] == "Любимые фильмы":
					return "Любимые фильмы", f"{arr[1]}"
				elif arr[0] == "Любимые телешоу":
					return "Любимые телешоу", f"{arr[1]}"
				elif arr[0] == "Любимые книги":
					return "Любимые книги", f"{arr[1]}"
				elif arr[0] == "Любимые игры":
					return "Любимые игры", f"{arr[1]}"
				elif arr[0] == "Любимые цитаты":
					return "Любимые цитаты", f"{arr[1]}"
				elif arr[0] == "О себе":
					return "О себе", f"{arr[1]}"
				elif arr[0] == "Группы":
					return "Группы", f"{arr[1]}"

			else:
				return str( string )

	else:
		return "NULL"


def check_counter(counter):
	# функция разбора и возврата данных профиля

	if counter:
		label = counter.select_one(".label").text
		count = counter.select_one(".count").text

		if label == "общий друг" or label == "общих друга" or label == "общих друзей":
			return "Общих друзей", f"{count}"

		elif label == "друг" or label == "друга" or label == "друзей":
			return "Друзей", f"{count}"

		elif label == "подписчик" or label == "подписчика" or label == "подписчиков":
			return "Подписок", f"{count}"

		elif label == "запись" or label == "записи" or label == "записей":
			return "Постов", f"{count}"

		elif label == "фотография" or label == "фотографии" or label == "фотографий":
			return "Фотографий", f"{count}"

		elif label == "отметка" or label == "отметки" or label == "отметок":
			return "Отметок", f"{count}"

		elif label == "статья" or label == "статьи" or label == "статей":
			return "Статей", f"{count}"

		elif label == "видеозапись" or label == "видеозаписи" or label == "видеозаписей":
			return "Видеозаписей", f"{count}"

		elif label == "подарок" or label == "подарка" or label == "подарков":
			return "Подарков", f"{count}"

	else:
		return "NULL"


def printer( key, value, file ):
	if conf_fn_db:
		pass

	if conf_fn_file:
		if key == "void":
			file.write( "\n" )
		else:
			file.write( str(f"{key:20}" ) + " | " + str( value ) + "\n" )

	if conf_fn_log:
		if key == "void":
			print()
		else:
			print( f"{key:20} | {value}" )
