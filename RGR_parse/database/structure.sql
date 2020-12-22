-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Дек 22 2020 г., 14:37
-- Версия сервера: 8.0.20
-- Версия PHP: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `rgr_parse`
--
CREATE DATABASE IF NOT EXISTS `rgr_parse` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `rgr_parse`;

-- --------------------------------------------------------

--
-- Структура таблицы `data_organizations`
--
-- Создание: Дек 22 2020 г., 03:28
--

CREATE TABLE `data_organizations` (
  `id` int NOT NULL,
  `name` varchar(300) NOT NULL,
  `city` varchar(300) NOT NULL,
  `raiting` decimal(8,4) NOT NULL,
  `attestat` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- ССЫЛКИ ТАБЛИЦЫ `data_organizations`:
--

-- --------------------------------------------------------

--
-- Структура таблицы `data_rieltors`
--
-- Создание: Дек 22 2020 г., 01:39
-- Последнее обновление: Дек 22 2020 г., 02:03
--

CREATE TABLE `data_rieltors` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `patronymic` varchar(100) NOT NULL,
  `company` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `city` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `raiting` decimal(8,4) NOT NULL,
  `attestat` varchar(100) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- ССЫЛКИ ТАБЛИЦЫ `data_rieltors`:
--

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `data_organizations`
--
ALTER TABLE `data_organizations`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `data_rieltors`
--
ALTER TABLE `data_rieltors`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `data_organizations`
--
ALTER TABLE `data_organizations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `data_rieltors`
--
ALTER TABLE `data_rieltors`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
