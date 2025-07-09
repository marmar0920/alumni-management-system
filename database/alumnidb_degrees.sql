-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: alumnidb
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `degrees`
--

DROP TABLE IF EXISTS `degrees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `degrees` (
  `degreeID` int NOT NULL,
  `alumniID` int NOT NULL,
  `major` varchar(50) NOT NULL,
  `minor` varchar(50) DEFAULT NULL,
  `graduationDT` date DEFAULT NULL,
  `university` varchar(100) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  PRIMARY KEY (`degreeID`),
  KEY `alumniID` (`alumniID`),
  CONSTRAINT `degrees_ibfk_1` FOREIGN KEY (`alumniID`) REFERENCES `alumni` (`alumniID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `degrees`
--

LOCK TABLES `degrees` WRITE;
/*!40000 ALTER TABLE `degrees` DISABLE KEYS */;
INSERT INTO `degrees` VALUES (100,201,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(101,202,'MIS','Accounting','2023-12-09','Kennesaw State University','Kennesaw','GA'),(102,203,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(103,204,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(104,205,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(105,207,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(106,208,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(107,209,'MIS','Management','2022-05-10','Kennesaw State University','Kennesaw','GA'),(108,210,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(109,211,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(110,212,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(111,213,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(112,214,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(113,215,'MIS','','2021-12-11','Kennesaw State University','Kennesaw','GA'),(114,216,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(115,217,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(116,218,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(117,218,'MBA','','2023-12-09','Georgia State University','Atlanta','GA'),(118,219,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(119,220,'MIS','','2021-12-11','Kennesaw State University','Kennesaw','GA'),(120,229,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(121,231,'MIS','Marketing','2021-12-11','Kennesaw State University','Kennesaw','GA'),(122,233,'MIS','Marketing','2021-12-11','Kennesaw State University','Kennesaw','GA'),(123,234,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(124,235,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(125,236,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(126,237,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(127,238,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(128,239,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(129,240,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(130,241,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(131,242,'MIS','Management','2021-12-11','Kennesaw State University','Kennesaw','GA'),(132,243,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(133,245,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(134,246,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(135,247,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(136,248,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(137,249,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(138,250,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(139,251,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(140,252,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(141,253,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(142,254,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(143,255,'MIS','Marketing','2020-05-12','Kennesaw State University','Kennesaw','GA'),(144,256,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(145,257,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(146,258,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(147,259,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(148,260,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(149,261,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(150,262,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(151,263,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(152,264,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(153,265,'MIS','Marketing','2020-12-12','Kennesaw State University','Kennesaw','GA'),(154,266,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(155,268,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(156,269,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(157,270,'MIS','Accounting','2021-05-11','Kennesaw State University','Kennesaw','GA'),(158,274,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(159,275,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(160,276,'MIS','','2021-12-11','Kennesaw State University','Kennesaw','GA'),(161,277,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(162,278,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(163,279,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(164,280,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(165,282,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(166,283,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(167,284,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(168,285,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(169,286,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(170,288,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(171,289,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(172,290,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(173,291,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(174,293,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(175,294,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(176,295,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(177,296,'MIS','','2022-05-10','Kennesaw State University','Kennesaw','GA'),(178,297,'MIS','Marketing','2023-05-09','Kennesaw State University','Kennesaw','GA'),(179,299,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(180,300,'MIS','','2021-05-11','Kennesaw State University','Kennesaw','GA'),(181,301,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(182,303,'MIS','','2020-12-12','Kennesaw State University','Kennesaw','GA'),(183,304,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(184,305,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(185,306,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(186,307,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(187,308,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(188,309,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(189,310,'MIS','','2021-12-11','Kennesaw State University','Kennesaw','GA'),(190,311,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA'),(191,312,'MIS','Accounting','2020-12-12','Kennesaw State University','Kennesaw','GA'),(192,313,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(193,314,'MIS','','2020-05-12','Kennesaw State University','Kennesaw','GA'),(194,315,'MIS','','2021-12-11','Kennesaw State University','Kennesaw','GA'),(195,320,'MIS','','2024-05-08','Kennesaw State University','Kennesaw','GA'),(196,321,'MIS','','2022-12-10','Kennesaw State University','Kennesaw','GA'),(197,322,'MIS','','2023-12-09','Kennesaw State University','Kennesaw','GA'),(198,323,'MIS','Marketing','2022-05-10','Kennesaw State University','Kennesaw','GA'),(199,324,'MIS','','2023-05-09','Kennesaw State University','Kennesaw','GA');
/*!40000 ALTER TABLE `degrees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-08 11:01:50
