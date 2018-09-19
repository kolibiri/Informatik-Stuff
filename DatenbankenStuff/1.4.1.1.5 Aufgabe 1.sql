-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Sep 2018 um 09:19
-- Server-Version: 10.1.21-MariaDB
-- PHP-Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `schüler`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `liste`
--

CREATE TABLE `liste` (
  `Vorname` text NOT NULL,
  `Nachname` text NOT NULL,
  `Geburtsdatum` date NOT NULL,
  `LK1` text NOT NULL,
  `LK2` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `liste`
--

INSERT INTO `liste` (`Vorname`, `Nachname`, `Geburtsdatum`, `LK1`, `LK2`) VALUES
('Justin', 'Svrakic', '2002-06-26', 'Biologie', 'Informatik'),
('Johannes', 'Maagk', '2001-08-25', 'Englisch', 'Informatik'),
('Jonas', 'Bremer', '2002-11-03', 'Chemie', 'Informatik');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
