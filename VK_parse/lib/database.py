import pymysql
from config import *


class MySQL:
	con = pymysql.connect(host = "localhost", user = "root", password = "root", database = "vk_parse")
