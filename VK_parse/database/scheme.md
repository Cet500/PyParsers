# DB


## === VK block ========================

**vk_users**

Таблица спарпасенных пользователей соцсети ВК.

| name                  | a | ky | type         |
|:----------------------|:-:|:--:|:-------------|
| id                    | A | PK | increment    |
| vk_id                 | A |    | int          |
| access                | A |    | char(1)      |
| datetime_last_login   |   |    | varchar(100) |
| alias                 |   |    | varchar(60)  |
| date_of_birth         |   |    | date         |
| city                  |   |    | varchar(100) |
| family_position       |   |    | varchar(100) |
| education             |   |    | varchar(100) |
| place_education       |   |    | varchar(100) |
| site                  |   |    | varchar(200) |
| telefon               |   |    | varchar(40)  |
| add_telefon           |   |    | varchar(40)  |
| native_city           |   |    | varchar(100) |
| status                |   |    | varchar(300) |
| political_preferences |   |    | varchar(150) |
| main_in_people        |   |    | varchar(150) |
| main_in_life          |   |    | varchar(150) |
| attitude_to_smoking   |   |    | varchar(150) |
| attitude_to_alcohol   |   |    | varchar(150) |
| inspire               |   |    | varchar(150) |
| worldview             |   |    | varchar(150) |
| activity              |   |    | text         |
| like_music            |   |    | text         |
| like_films            |   |    | text         |
| like_teleshow         |   |    | text         |
| like_books            |   |    | text         |
| like_games            |   |    | text         |
| like_quotes           |   |    | text         |
| about_myself          |   |    | text         |
| groups                |   |    | text         |
| count_subscribes      |   |    | int          |
| count_posts           |   |    | int          |
| count_photos          |   |    | int          |
| count_marks           |   |    | int          |
| datetime_add          | A |    | datetime     |


**vk_families**

Таблица для построения родственных связей между юзерами.

| name                | a | ky | type      |
|:--------------------|:-:|:--:|:----------|
| id                  | A | PK | increment |
| id_vk               | A | FK | int       |
| id_vk_user          | A | FK | int       |
| id_vk_relative      | A | FK | int       |
| id_vk_relative_type | A | FK | int       |


**vk_relative_types**

Таблица со списком типов родственных связей.

| name          | a | ky | type        |
|:--------------|:-:|:--:|:------------|
| id            | A | PK | increment   |
| relative_type | A |    | varchar(50) |


**vk_links**

Таблица со ссылками на другие соцсети.

| name               | a | ky | type         |
|:-------------------|:-:|:--:|:-------------|
| id                 | A | PK | increment    |
| id_vk              | A | FK | int          |
| id_social_net_type | A | FK | int          |
| link               | A |    | varchar(100) |


**vk_schools**

Таблица со списком школ, пользователей ВК.

| name   | a | ky | type         |
|:-------|:-:|:--:|:-------------|
| id     | A | PK | increment    |
| id_vk  | A | FK | int          |
| school | A |    | varchar(200) |


**vk_armies_parts**

Таблица со списком армейских частей, служащих в ВК.

| name      | a | ky | type         |
|:----------|:-:|:--:|:-------------|
| id        | A | PK | increment    |
| id_vk     | A | FK | int          |
| army_part | A |    | varchar(200) |


**vk_places_work**

Таблица с местами работы.

| name       | a | ky | type         |
|:-----------|:-:|:--:|:-------------|
| id         | A | PK | increment    |
| id_vk      | A | FK | int          |
| place_work | A |    | varchar(200) |


**vk_universities**

Таблица с высшим образованием.

| name           | a | ky | type         |
|:---------------|:-:|:--:|:-------------|
| id             | A | PK | increment    |
| id_vk          | A | FK | int          |
| university     | A |    | varchar(100) |
| faculty        | A |    | varchar(100) |
| speciality     | A |    | varchar(100) |
| form_education | A |    | varchar(100) |


**vk_languages**

Таблица с языками, которыми владеют пользователи.

| name     | a | ky | type        |
|:---------|:-:|:--:|:------------|
| id       | A | PK | increment   |
| id_vk    | A | FK | int         |
| language |   |    | varchar(50) |
