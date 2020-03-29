-- phpMyAdmin SQL Dump
-- version *******
-- https://www.phpmyadmin.net/
--
-- Anamakine: ***********
-- Üretim Zamanı: 29 Mar 2020, 15:17:34
-- Sunucu sürümü: ********
-- PHP Sürümü: ********

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `dhcpserver`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `dhcpclients`
--

DROP TABLE IF EXISTS `dhcpclients`;
CREATE TABLE IF NOT EXISTS `dhcpclients` (
  `ipAddress` varchar(20) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `Mac` varchar(20) NOT NULL,
  PRIMARY KEY (`ipAddress`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `dhcpclients`
--

INSERT INTO `dhcpclients` (`ipAddress`, `startTime`, `endTime`, `Mac`) VALUES
('192.168.42.5', '2020-01-30 08:02:54', '2020-04-08 08:02:54', '00:50:04:53:D5:57'),
('192.168.42.4', '2020-01-30 08:02:54', '2020-04-08 08:02:54', '00:50:04:53:D5:57'),
('192.168.42.3', '2020-01-30 08:02:54', '2020-04-08 08:02:54', '00:50:04:53:D5:57'),
('192.168.42.2', '2020-01-30 08:02:54', '2020-04-08 08:02:54', '00:50:04:53:D5:57'),
('192.168.42.1', '2020-01-30 08:02:54', '2020-04-04 08:02:54', '00:50:04:53:D5:57'),
('192.168.42.88', '2020-01-30 08:02:54', '2020-04-08 08:02:54', '00:50:04:53:D5:57');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
