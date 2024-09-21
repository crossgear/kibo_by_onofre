CREATE DATABASE  IF NOT EXISTS `proyecto_grupal_bd` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `proyecto_grupal_bd`;
-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: proyecto_grupal_bd
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'TVs','2023-03-08','2023-03-08'),(2,'Speakers','2023-03-08','2023-03-08'),(3,'Monitor','2023-03-09','2023-03-09'),(4,'Smartphones','2023-03-12','2023-03-12'),(5,'Auriculares','2023-03-14','2023-03-14'),(6,'Notebooks','2023-03-16','2023-03-16'),(7,'Webcams','2023-03-19','2023-03-19');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas`
--

DROP TABLE IF EXISTS `marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marcas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas`
--

LOCK TABLES `marcas` WRITE;
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` VALUES (1,'Xiaomi','2023-03-08','2023-03-08'),(2,'Samsung','2023-03-08','2023-03-08'),(3,'HP','2023-03-08','2023-03-08'),(4,'LG','2023-03-09','2023-03-09'),(5,'JBL','2023-03-10','2023-03-10'),(6,'DELL','2023-03-15','2023-03-15'),(7,'Redragon ','2023-03-19','2023-03-19');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `descuento` tinyint(4) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `stock_ideal` int(11) DEFAULT NULL,
  `stock_disponible` int(11) DEFAULT NULL,
  `stock_minimo` int(11) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  `marca_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_productos_marcas1_idx` (`marca_id`),
  KEY `fk_productos_categorias1_idx` (`categoria_id`),
  CONSTRAINT `fk_productos_categorias1` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_marcas1` FOREIGN KEY (`marca_id`) REFERENCES `marcas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Xiaomi Mi TV Smart Q1 75” UHD','Procesador y almacenamiento\r\n\r\nMediaTek MT9611\r\nCPU: CPU: Cuatro núcleos, hasta 1,5 GHz\r\nGPU: Mali G52 MP2\r\nRAM: 2GB\r\nStorage: 32GB',12200000,25,'/static/files/1.jpg',5,1,3,'2023-03-08','2023-04-16',1,1),(2,'Speaker Jbl Flip 5 Azul','12 horas de música continua.\r\n\r\nCertificado IPX7.\r\n\r\nBatería mejorada 4800 mAh.\r\n\r\nPuerto USB-C.\r\n\r\nResiste al agua y flota',745000,14,'/static/files/2.jpg',10,10,4,'2023-03-10','2023-04-16',1,2),(3,'Samsung Galaxy A04 SM-A045M/DS Dual 64 GB - Black','Tamaño de pantalla: 6.5\" PLS LCD\r\nResolución: 720 x 1600\r\nCámara principal: Dual 50MP + 2MP\r\nCámara frontal: 5MP',954980,0,'/static/files/3.jpg',3,2,2,'2023-03-12','2023-04-12',2,4),(4,'Xiaomi Redmi Note 10S Dual 128 GB - Azul','Tamaño de Pantalla: 6.43\'\'\r\nResolución: 1080 x 2400\r\nCámara principal: Cuádruple 64MP + 8MP + 2MP + 2MP\r\nCámara frontal: 13MP\r\nMemoria interna: 128 GB',1500177,5,'/static/files/4.jpg',6,5,2,'2023-03-12','2023-04-10',1,1),(5,'Auricular JBL T110','El auricular JBL T110 es ligero, cómodo y compacto. Debajo de la carcasa duradera del auricular, un par de controladores de 9 mm que reproducen el sonido JBL Pure Bass que enfatiza los graves profundos. Además, el control remoto de un solo botón en un cable plano sin enredos le permite controlar la reproducción de música, así como llamadas sobre la marcha con un micrófono incorporado.',48000,12,'/static/files/5.jpg',5,5,3,'2023-03-14','2023-04-16',5,5),(6,'Xiaomi Poco M5 Dual','La nueva Xiaomi Poco M5 con la pantalla 6.58\'\', cuenta con cámara principal triple de 50MP + 2MP + 2MP y la cámara frontal de 5MP, su diseño súper elegante se fusiona en total armonía con su potente rendimiento. Batería de 5.000mAh.',1355000,0,'/static/files/6.jpg',7,7,4,'2023-03-16','2023-04-10',1,4),(7,'Auricular Xiaomi 1More HSEJ03JY','El auricular Xiaomi Mi 1More HSEJ03JY es compacto y brinda versatilidad al usuario. Se puede usar con diferentes dispositivos: como computadoras portátiles, teléfonos inteligentes, reproductores de MP3, tabletas, entre otros. Tiene un diseño moderno y cómodo y se puede usar mientras hace ejercicio o simplemente escucha música mientras estudia o trabaja.',40000,1,'/static/files/7.jpg',10,2,5,'2023-03-16','2023-04-16',1,1),(8,'Speaker Xiaomi MDZ-36-DB','El speaker Xiaomi Mi Portable MDZ-36-DB cuenta con diseño compacto y resistente. A pesar de su tamaño cuenta con una potencia de 16 W ideal para campamentos o aventuras al aire libre. Posee conectividad bluetooth 5.0, Jack 3.5 mm y la tecnología TWS, a través de la cual es posible conectar otro speaker con TWS y aumentar la potencia sonora.',284000,0,'/static/files/8.jpg',15,15,8,'2023-03-16','2023-04-10',1,2),(9,'Monitor LED Samsung LT24H315HLB 24\" HD','Samsung TH315S cuenta con una plataforma Smart Hub, una portal muy avanzado a través de la cual puedes explorar una gran variedad de aplicaciones, videoclips, programas de televisión y publicaciones sociales. Con ella, el acceso a tus medios favoritos es más rápido y sencillo.',1442648,0,'/static/files/9.jpg',15,14,6,'2023-03-16','2023-04-10',2,3),(10,'Monitor LED LG UltraGear 32GN600 31.5\"','El monitor LG UltraGear 32GN600 para juegos tiene un diseño elegante con una velocidad ultrarrápida de 165Hz les permite a los jugadores ver rápidamente el próximo cuadro y hace que la imagen aparezca con fluidez con resolución QHD de 2560 x 1440 para brindar la mejor experiencia de juego.',2920000,0,'/static/files/10.jpg',6,4,2,'2023-03-16','2023-04-10',4,3),(11,'Notebook Dell Inspiron 15 3501 15.6\"','La notebook Dell Inspiron 15 3501 tiene una pantalla de 15.6\" con resolución HD (1366 x 768 p) que ofrece imágenes más nítidas y colores más brillantes. El dispositivo está equipado con un procesador Intel Core i3 de undécima generación para un rendimiento excepcional. Incorpora 1 TB de almacenamiento HDD y 4 GB de RAM DDR4.',3850000,5,'/static/files/11.jpg',7,7,2,'2023-03-16','2023-04-10',6,6),(12,'Notebook HP ProBook 635 G8 13.3\"','La notebook HP ProBook 635 Aero G8 tiene una pantalla IPS de 13.3\" con resolución Full HD (1920 x 1080p) que ofrece imágenes nítidas y colores vivos. Está equipada con un procesador AMD Ryzen 5 5600U Hexa-Core para un rendimiento superior, memoria de almacenamiento SSD M.2 NVMe de 256 GB y memoria RAM de 16 GB DDR4, ideal para trabajar, estudiar o divertirse.',5302000,0,'/static/files/12.jpg',10,10,5,'2023-03-16','2023-04-10',3,6),(13,'Notebook HP 15Z-EF2000 15.6\"','La notebook HP 15Z-EF2000 tiene una pantalla IPS de 15.6\" con resolución Full HD (1920 x 1080p) que ofrece imágenes nítidas y colores más vivos. Está equipado con un procesador AMD Ryzen 7 5700U para un rendimiento superior, 512 GB de almacenamiento SSD M.2 NVMe y 12 GB de RAM, ideal para trabajar, estudiar o jugar. ',5752000,15,'/static/files/13.jpg',20,20,5,'2023-03-16','2023-04-10',3,6),(14,'Notebook Dell Latitude 5430 14\"','La notebook Latitude 5430 de 14\" de Dell ofrece a los profesionales y estudiantes una herramienta de rendimiento de alto nivel. Está equipada con un procesador Intel Core i7-1265U de 10 núcleos, 16 GB de memoria RAM DDR4 de 3200 MHz y 256 GB de almacenamiento en una unidad de estado sólido M.2. ',10178000,5,'/static/files/14.jpg',12,12,4,'2023-03-16','2023-04-10',6,1),(15,'Televisor Smart LED LG 43LM6370','Los televisores LG Full HD ofrecen imágenes más precisas con una resolución sorprendente y colores vivos.Los televisores LG FHD están hechos para impresionar con una calidad de imagen clara que es dos veces mejor que la HD. Y con Dynamic Color y Active HDR, todo su contenido favorito será más realista y vibrante.',2256000,12,'/static/files/15.jpg',5,2,1,'2023-03-16','2023-04-10',4,1),(16,'Monitor LED LG 24MP400B 24\"','Cuenta con colores auténticos desde cualquier ángulo. El panel IPS de LG ofrece colores más claros y más auténticos. El tiempo de respuesta se ha reducido, la reproducción del color ha mejorado y los usuarios pueden ver la pantalla desde prácticamente cualquier ángulo.',1053000,10,'/static/files/16.jpg',5,4,2,'2023-03-16','2023-04-10',4,3),(17,'Webcam Redragon Fobos GW600-1','Destinada a aquellos entusiastas que demandan alta calidad de transmisión, una webcam práctica de nivel profesional con imágenes claras, colores nítidos, con calidad de video de hasta 720p. Con funciones de enfoque fijo y corrección de luz, que mantendrán siempre tus transmisiones en la calidad que deseas, sin importar las condiciones de iluminación.',265000,0,'/static/files/17.jpg',10,2,4,'2023-03-19','2023-04-10',7,7),(18,'Xiaomi Poco X4 GT 5G Dual','La nueva Xiaomi Poco X4 GT con la pantalla 6.6\", cuenta con cámara principal triple 64MP + 8MP + 2MP y la cámara frontal 16MP, su diseño elegante se fusiona en total armonía con su potente rendimiento. Batería de 5080 mAh.',2805000,0,'/static/files/18.jpg',5,0,2,'2023-04-10','2023-04-10',1,4);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_favoritos`
--

DROP TABLE IF EXISTS `productos_favoritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos_favoritos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` date DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `producto_id` (`producto_id`),
  CONSTRAINT `productos_favoritos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `productos_favoritos_ibfk_2` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_favoritos`
--

LOCK TABLES `productos_favoritos` WRITE;
/*!40000 ALTER TABLE `productos_favoritos` DISABLE KEYS */;
/*!40000 ALTER TABLE `productos_favoritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `nivel` tinyint(4) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'German','González','german.gonzalez@gmail.com','$2b$12$r9J6hlahNbPXEcxzCzlTZe5keYud4Ggdk.M/6GHIQaRmzYOpTeKxK','Calle Jaime San Just','0992843527',0,'2023-03-14','2023-03-14'),(2,'Tadeo','Molinas','tadeo25.molinas@gmail.com','$2b$12$cFlwN7IwLlFA8vyuYaCdLeeCNA8dn8YU18NVqOWOZuwAnhpnVT/Kq','Calle Caacupe','0992843527',1,'2023-03-14','2023-03-19'),(3,'Marcelo','Ocampos','marceloc@gmail.com','$2b$12$vz0/XfDTSYZ2BsBaSF411.o6LceNvpn.JizxgalIK4jPx5MM8INfO','Calle Las Vegas','0992125432',0,'2023-03-19','2023-03-19'),(4,'Tomas','Molas','tamc935@gmail.com','$2b$12$42.iSsEM82O1UOrK102YvO9aQxxSWeCEmsZOR8YIFVP7IeOoC/uju','Calle Mcal. Estigarribia','0975286512',0,'2023-04-15','2023-04-15');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_cab`
--

DROP TABLE IF EXISTS `ventas_cab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ventas_cab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `total` varchar(45) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_VentasCab_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_VentasCab_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_cab`
--

LOCK TABLES `ventas_cab` WRITE;
/*!40000 ALTER TABLE `ventas_cab` DISABLE KEYS */;
INSERT INTO `ventas_cab` VALUES (1,'2023-03-12 12:34:17','2444980',1),(2,'2023-03-14 08:37:10','2654960',1),(3,'2023-03-14 09:04:56','1500177',1),(4,'2023-03-14 21:49:29','1644177',1),(5,'2023-03-15 21:16:14','48000',1),(6,'2023-03-15 21:27:45','48000',1),(7,'2023-03-16 12:16:56','364000',1),(8,'2023-03-17 08:04:39','1923000',1),(9,'2023-03-18 09:49:46','1569368',1),(10,'2023-03-18 16:29:18','765180',1),(11,'2023-03-18 17:33:17','7941120',1),(12,'2023-03-18 17:55:34','284000',1),(13,'2023-03-19 15:18:15','4146048',1),(14,'2023-03-19 15:22:15','265000',1),(15,'2023-03-19 15:24:57','40000',3),(16,'2023-03-20 16:12:56','612240',1),(17,'2023-03-20 16:23:31','307240',1),(18,'2023-03-20 16:46:52','682940',1),(19,'2023-03-20 19:25:01','4065000',1),(20,'2023-04-09 09:52:13','1420000',1),(21,'2023-04-14 09:23:03',NULL,1),(22,'2023-04-14 09:24:53',NULL,1),(23,'2023-04-14 09:27:03','39600',1),(24,'2023-04-14 09:28:07',NULL,1),(25,'2023-04-14 09:30:10','2920000',1),(26,'2023-04-14 09:31:00','39600',1),(27,'2023-04-15 18:54:49','2805000',4),(28,'2023-04-16 09:02:02','124080',4),(29,'2023-04-16 09:44:45','640700',1),(30,'2023-04-16 09:47:31','1060000',4),(31,'2023-04-16 09:48:52','947700',4);
/*!40000 ALTER TABLE `ventas_cab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_det`
--

DROP TABLE IF EXISTS `ventas_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ventas_det` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) DEFAULT NULL,
  `subtotal` int(11) DEFAULT NULL,
  `producto_id` int(11) NOT NULL,
  `venta_cab_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_VentaDet_productos1_idx` (`producto_id`),
  KEY `fk_VentaDet_VentaCab1_idx` (`venta_cab_id`),
  CONSTRAINT `fk_VentaDet_VentaCab1` FOREIGN KEY (`venta_cab_id`) REFERENCES `ventas_cab` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_VentaDet_productos1` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_det`
--

LOCK TABLES `ventas_det` WRITE;
/*!40000 ALTER TABLE `ventas_det` DISABLE KEYS */;
INSERT INTO `ventas_det` VALUES (1,2,1490000,2,1),(2,1,954980,3,1),(3,1,745000,2,2),(4,2,1909960,3,2),(5,1,1500177,4,3),(6,3,144000,5,4),(7,1,1500177,4,4),(8,1,48000,5,5),(9,1,48000,5,6),(10,2,80000,7,7),(11,1,284000,8,7),(12,1,1355000,6,8),(13,2,568000,8,8),(14,1,1442648,9,9),(15,3,126720,5,9),(16,1,40000,7,10),(17,1,640700,2,10),(18,2,84480,5,10),(19,4,7941120,15,11),(20,1,284000,8,12),(21,2,1281400,2,13),(22,1,1425168,4,13),(23,2,84480,5,13),(24,1,1355000,6,13),(25,1,265000,17,14),(26,1,40000,7,15),(27,2,530000,17,16),(28,1,40000,7,16),(29,1,42240,5,16),(30,1,265000,17,17),(31,1,42240,5,17),(32,1,640700,2,18),(33,1,42240,5,18),(34,3,4065000,6,19),(35,5,1420000,8,20),(36,4,11220000,18,21),(37,1,39600,7,22),(38,1,39600,7,23),(39,1,2920000,10,24),(40,1,2920000,10,25),(41,1,39600,7,26),(42,1,2805000,18,27),(43,1,39600,7,28),(44,2,84480,5,28),(45,1,640700,2,29),(46,4,1060000,17,30),(47,1,947700,16,31);
/*!40000 ALTER TABLE `ventas_det` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-16  9:53:23
