# DB


## === VK block ========================

**vk_users**

Таблица спарпасенных пользователей соцсети ВК.

| name                  | type         |
|:----------------------|:-------------|
| id                    | increment    |
| vk_id                 | int          |
| access                | char(1)      |
| datetime_last_login   | varchar(100) |
| alias                 | varchar(60)  |
| date_of_birth         | date         |
| city                  | varchar(100) |
| family_position       | varchar(100) |
| education             | varchar(100) |
| place_education       | varchar(100) |
| site                  | varchar(200) |
| telefon               | varchar(40)  |
| add_telefon           | varchar(40)  |
| native_city           | varchar(100) |
| status                | varchar(300) |
| political_preferences | varchar(150) |
| main_in_people        | varchar(150) |
| main_in_life          | varchar(150) |
| attitude_to_smoking   | varchar(150) |
| attitude_to_alcohol   | varchar(150) |
| inspire               | varchar(150) |
| worldview             | varchar(150) |
| activity              | text         |
| like_music            | text         |
| like_films            | text         |
| like_teleshow         | text         |
| like_books            | text         |
| like_games            | text         |
| like_quotes           | text         |
| about_myself          | text         |
| groups                | text         |
| count_subscribes      | int          |
| count_posts           | int          |
| count_photos          | int          |
| count_marks           | int          |
| datetime_add          | datetime     |


**vk_families**

Таблица для построения родственных связей между пользователями ВК.

| name                     | type      |
|:-------------------------|:----------|
| id                       | increment |
| id_vk                    | int       |
| id_vk_user               | int       |
| id_vk_user_relative      | int       |
| id_vk_user_relative_type | int       |


**vk_relative_types**

Таблица со списком типов родственных связей.

| name          | type        |
|:--------------|:------------|
| id            | increment   |
| relative_type | varchar(50) |


**vk_links**

Таблица со ссылками на другие соцсети.

| name            | type         |
|:----------------|:-------------|
| id              | increment    |
| id_vk           | int          |
| link            | varchar(100) |
| social_net_type | int          |


**vk_schools**

Таблица со списком школ, пользователей ВК.

| name   | type         |
|:-------|:-------------|
| id     | increment    |
| id_vk  | int          |
| school | varchar(200) |


**vk_armies_parts**

Таблица со списком армейских частей, служащих в ВК.

| name      | type         |
|:----------|:-------------|
| id        | increment    |
| id_vk     | int          |
| army_part | varchar(200) |


**vk_places_work**

Таблица с местами работы.

| name       | type         |
|:-----------|:-------------|
| id         | increment    |
| id_vk      | int          |
| place_work | varchar(200) |


**vk_universities**

Таблица с высшим образованием.

| name           | type         |
|:---------------|:-------------|
| id             | increment    |
| id_vk          | int          |
| university     | varchar(100) |
| faculty        | varchar(100) |
| speciality     | varchar(100) |
| form_education | varchar(100) |


**vk_languages**

Таблица с языками, которыми владеют пользователи.

| name     | type        |
|:---------|:------------|
| id       | increment   |
| id_vk    | int         |
| language | varchar(50) |
