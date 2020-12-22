# DB


## === Data block ========================

**data_rieltors**

Таблица спарпасенных риелторов с реестра РГР.

| name       | type         |
|:-----------|:-------------|
| id         | increment    |
| name       | varchar(100) |
| lastname   | varchar(100) |
| patronymic | varchar(100) |
| company    | varchar(300) |
| city       | varchar(300) |
| raiting    | decimal(8,4) |
| attestat   | varchar(100) |
| date       | date         |


**data_organizations**

Таблица спрасенных организаций с реестра РГР.

| name     | type         |
|:---------|:-------------|
| id       | increment    |
| name     | varchar(300) |
| city     | varchar(300) |
| raiting  | decimal(8,4) |
| attestat | varchar(100) |
| date     | date         |
