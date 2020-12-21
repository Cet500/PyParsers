CREATE TABLE vk_users (
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
vk_id INT NOT NULL UNIQUE,
access CHAR (1) NOT NULL,
datetime_last_login VARCHAR (60) NOT NULL,
alias VARCHAR (60) NOT NULL,
date_of_birth DATE NOT NULL,
city VARCHAR (100) NOT NULL,
family_position VARCHAR (100) NOT NULL,
education VARCHAR (100) NOT NULL,
place_education VARCHAR (100) NOT NULL,
site VARCHAR (100) NOT NULL,
languages VARCHAR (100) NOT NULL,
telephone VARCHAR (20) NOT NULL,
add_telephone VARCHAR (20) NOT NULL,
place_work VARCHAR (100) NOT NULL,
university VARCHAR (100) NOT NULL,
faculty VARCHAR (100) NOT NULL,
speciality VARCHAR (100) NOT NULL,
form_education VARCHAR (100) NOT NULL,
status VARCHAR (100) NOT NULL,
school VARCHAR (100) NOT NULL,
army_part VARCHAR (200) NOT NULL,
political_preferences VARCHAR (100) NOT NULL)
COMMENT = 'Пользователи ВК';

CREATE TABLE vk_families (
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
id_vk_user INT NOT NULL,
id_vk_relative INT NOT NULL,
id_vk_relative_type INT NOT NULL)
COMMENT = 'Построение родственных связей';

CREATE TABLE vk_relative_types (
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
relative_type VARCHAR (50) NOT NULL)
COMMENT = 'Типы родственных связей';

CREATE TABLE vk_links (
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL)
COMMENT = 'Ссылки на другие соцсети';