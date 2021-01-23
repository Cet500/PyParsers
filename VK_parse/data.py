from bs4 import BeautifulSoup as bf
import requests
import datetime
import os
from lib.functions import check_data, check_counter, check_null, printer
from config import *


now = datetime.datetime.now()
file = open(f"data/data-{now.strftime('%Y-%m-%d')}.txt", "a")
file.write( f"=================== {now.strftime('%H:%M:%S')} ===================\n\n" )


for i in range(conf_sc_amount):
	base = "https://vk.com/id"
	link = base + str(conf_sc_start + i)

	markup = requests.get(link)

	soup = bf( markup.text, "lxml" )

	printer( "ID", f"{link}", file )

	if soup.select_one(".message_page_body"):
		printer( "Фамилия и имя", "ХЗ", file )
		printer( "Доступность", "Не существует", file )

	elif soup.select_one("#login_blocked_img"):
		printer( "Фамилия и имя", "ХЗ", file )
		printer( "Доступность", "Заблокирован", file )

	elif soup.select_one("#page_current_info"):
		if soup.select_one("#page_current_info").text == "Страница скрыта":
			printer( "Фамилия и имя", f"{soup.select_one('.page_name').text}", file )
			printer( "Доступность", "Скрыта", file )

	else:
		printer("Фамилия и имя", f"{soup.select_one('.page_name').text.rstrip()}", file)
		printer("Доступность", "Открыта", file)
		printer("Время входа", f"{check_null(soup.select_one('.profile_online_lv').text)}", file)

		data = soup.select(".profile_info_row")

		for dat in data:
			info = check_data(dat.text)
			if info != "NULL":
				printer( info[0], info[1], file )

		counters = soup.select(".page_counter")

		for counter in counters:
			count = check_counter(counter)
			if count != "NULL":
				printer( count[0], count[1], file )

	printer( "void", "void", file )


file.close()
