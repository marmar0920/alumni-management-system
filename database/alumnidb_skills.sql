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
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `SID` int NOT NULL,
  `alumniID` int NOT NULL,
  `skill` varchar(50) NOT NULL,
  `proficiency` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`SID`),
  KEY `alumniID` (`alumniID`),
  CONSTRAINT `skills_ibfk_1` FOREIGN KEY (`alumniID`) REFERENCES `alumni` (`alumniID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (100,204,'Figma','Beginner',''),(101,204,'Excel','Intermediate',''),(102,207,'Agile Methodologies','Intermediate',''),(103,208,'JavaScript','Beginner',''),(104,209,'Mobile Application Development','Intermediate',''),(105,210,'Java','Beginner',''),(106,211,'Data Analytics','Intermediate',''),(107,212,'Tableau','Beginner',''),(108,213,'Programming','Beginner',''),(109,214,'Agile Methodologies','Intermediate',''),(110,215,'Figma','Intermediate',''),(111,215,'SQL','Advance',''),(112,215,'Python','Beginner',''),(113,218,'Java','Beginner',''),(114,219,'User Experience 	(UX) Design','Beginner',''),(115,220,'Project Management','Intermediate',''),(116,229,'C#','Beginner',''),(117,231,'Power BI','Intermediate',''),(118,233,'AWS','Intermediate',''),(119,234,'React JS','Advance',''),(120,235,'Project Management','Intermediate',''),(121,236,'React JS','Intermediate',''),(122,237,'JavaScript','Beginner',''),(123,238,'AWS','Advance',''),(124,240,'Agile Methodologies','Advance',''),(125,241,'AWS','Advance',''),(126,242,'Power BI','Beginner',''),(127,243,'CSS','Advance',''),(128,245,'C#','Intermediate',''),(129,246,'Excel','Advance',''),(130,246,'AWS','Beginner',''),(131,246,'Network Administration','Beginner',''),(132,246,'Power BI','Advance',''),(133,250,'CSS','Intermediate',''),(134,251,'Figma','Intermediate',''),(135,252,'MongoDB','Intermediate',''),(136,253,'SQL','Beginner',''),(137,255,'Figma','Intermediate',''),(138,256,'Node JS','Beginner',''),(139,257,'Project Management','Intermediate',''),(140,258,'Azure','Intermediate',''),(141,259,'Excel','Advance',''),(142,260,'encryption techniques','Intermediate',''),(143,261,'Systems Analysis and Design','Intermediate',''),(144,262,'Agile Methodologies','Beginner',''),(145,263,'Tableau','Advance',''),(146,264,'Data analysis','Advance',''),(147,265,'MongoDB','Intermediate',''),(148,266,'Programming','Beginner',''),(149,268,'Data analysis','Intermediate',''),(150,269,'Mobile Application Development','Intermediate',''),(151,270,'Python','Beginner',''),(152,274,'Systems Analysis and Design','Intermediate',''),(153,276,'MySQL','Beginner',''),(154,277,'AWS','Beginner',''),(155,277,'MongoDB','Advance',''),(156,279,'React JS','Beginner',''),(157,279,'AWS','Intermediate',''),(158,282,'Figma','Advance',''),(159,283,'Systems Analysis and Design','Advance',''),(160,284,'Figma','Advance',''),(161,285,'Tableau','Intermediate',''),(162,285,'Systems Analysis and Design','Intermediate',''),(163,288,'Information Security','Beginner',''),(164,289,'Power BI','Intermediate',''),(165,290,'Java','Advance',''),(166,291,'JavaScript','Intermediate',''),(167,293,'Google Cloud','Advance',''),(168,294,'Mobile Application Development','Advance',''),(169,295,'Data analysis','Advance',''),(170,296,'Programming','Beginner',''),(171,297,'Project Management','Intermediate',''),(172,297,'Web Development','Beginner',''),(173,300,'User Experience 	(UX) Design','Advance',''),(174,303,'MongoDB','Intermediate',''),(175,304,'Systems Analysis and Design','Advance',''),(176,305,'Figma','Intermediate',''),(177,306,'Business Intelligence','Advance',''),(178,308,'Business Intelligence','Advance',''),(179,309,'Power BI','Intermediate',''),(180,310,'MongoDB','Intermediate',''),(181,310,'Web Development','Intermediate',''),(182,310,'Python','Intermediate',''),(183,313,'Data analysis','Beginner',''),(184,314,'Web Development','Intermediate',''),(185,320,'Database Management','Intermediate',''),(186,321,'encryption techniques','Advance',''),(187,322,'Business Intelligence','Beginner',''),(188,323,'JavaScript','Beginner',''),(189,323,'Azure','Beginner','');
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-19 20:52:33
