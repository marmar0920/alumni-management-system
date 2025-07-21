-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: alumnidb
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
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `addressID` int NOT NULL,
  `alumniID` int NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  `zipCode` varchar(10) DEFAULT NULL,
  `activeYN` char(1) DEFAULT NULL,
  `primaryYN` char(1) DEFAULT NULL,
  PRIMARY KEY (`addressID`),
  KEY `alumniID` (`alumniID`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`alumniID`) REFERENCES `alumni` (`alumniID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (100,201,'123 Peachtree St NW','Atlanta','GA','30303','Y','Y'),(101,202,'456 Magnolia Ave','Savannah','GA','31401','Y','Y'),(102,203,'789 River Rd','Augusta','GA','30901','Y','Y'),(103,204,'101 Dogwood Dr','Macon','GA','31201','Y','Y'),(104,205,'234 Oak St','Athens','GA','30601','Y','Y'),(105,207,'567 Maple Ave','Columbus','GA','31901','Y','Y'),(106,208,'890 Pine St','Albany','GA','31701','Y','Y'),(107,209,'111 Cedar Ln','Valdosta','GA','31601','Y','Y'),(108,210,'222 Elm St','Gainesville','GA','30501','Y','Y'),(109,211,'333 Walnut Ave','Rome','GA','30161','Y','Y'),(110,212,'444 Cherry St','Dalton','GA','30720','Y','Y'),(111,213,'555 Birch Dr','Warner Robins','GA','31088','Y','Y'),(112,214,'666 Willow Rd','Johns Creek','GA','30005','Y','Y'),(113,215,'777 Spruce St','Sandy Springs','GA','30328','Y','Y'),(114,216,'888 Sycamore Dr','Roswell','GA','30075','Y','Y'),(115,217,'999 Hickory Ave','Alpharetta','GA','30004','Y','Y'),(116,218,'1212 Cedarwood Ln','Marietta','GA','30008','Y','Y'),(117,219,'1313 Birchwood Dr','Smyrna','GA','30080','Y','Y'),(118,220,'1414 Oakwood Ave','Brookhaven','GA','30319','Y','Y'),(119,229,'1515 Elmwood Dr','Dunwoody','GA','30338','Y','Y'),(120,231,'1616 Maplewood St','Peachtree Corners','GA','30092','Y','Y'),(121,233,'1717 Pinecrest Ave','East Point','GA','30344','Y','Y'),(122,234,'1818 Dogwood Rd','Mableton','GA','30126','Y','Y'),(123,235,'1919 Birchwood Dr','Milton','GA','30004','Y','Y'),(124,236,'2020 Sycamore Ln','Lawrenceville','GA','30043','Y','Y'),(125,237,'2121 Cedarwood Ave','Tucker','GA','30084','Y','Y'),(126,238,'2222 Oakwood Dr','Duluth','GA','30096','Y','Y'),(127,239,'2323 Maple St','Kennesaw','GA','30144','Y','Y'),(128,240,'2424 Willow Ave','Decatur','GA','30030','Y','Y'),(129,241,'2525 Hickory St','Woodstock','GA','30188','Y','Y'),(130,242,'2626 Elmwood Ln','Canton','GA','30114','Y','Y'),(131,243,'2727 Birchwood Dr','Acworth','GA','30101','Y','Y'),(132,245,'2828 Pinecrest St','Cartersville','GA','30120','Y','Y'),(133,246,'2929 Dogwood Rd','Union City','GA','30291','Y','Y'),(134,247,'3030 Cedar Ln','Suwanee','GA','30024','Y','Y'),(135,248,'3131 Oakwood Ave','Forest Park','GA','30297','Y','Y'),(136,249,'3232 Sycamore Dr','Lithia Springs','GA','30122','Y','Y'),(137,250,'3333 Maplewood Rd','Buford','GA','30518','Y','Y'),(138,251,'3434 Willow St','Snellville','GA','30039','Y','Y'),(139,252,'3535 Hickory Ave','Stockbridge','GA','30281','Y','Y'),(140,253,'3636 Elmwood Dr','Conyers','GA','30012','Y','Y'),(141,254,'3737 Pinecrest Ave','Fayetteville','GA','30214','Y','Y'),(142,255,'3838 Birchwood Ln','Covington','GA','30014','Y','Y'),(143,256,'3939 Cedarwood Ave','Loganville','GA','30052','Y','Y'),(144,257,'4040 Oakwood Rd','McDonough','GA','30252','Y','Y'),(145,258,'4141 Maple Ave','Sugar Hill','GA','30518','Y','Y'),(146,259,'4242 Willow Dr','Norcross','GA','30071','Y','Y'),(147,260,'4343 Sycamore St','Fairburn','GA','30213','Y','Y'),(148,261,'4444 Cedar Ln','Hampton','GA','30228','Y','Y'),(149,262,'4545 Elmwood Ave','Doraville','GA','30340','Y','Y'),(150,263,'4646 Pinecrest Dr','Braselton','GA','30517','Y','Y'),(151,264,'4747 Birchwood Rd','Villa Rica','GA','30180','Y','Y'),(152,265,'4848 Dogwood Ave','Buford','GA','30518','Y','Y'),(153,266,'4949 Hickory St','Lithonia','GA','30038','Y','Y'),(154,268,'5050 Oakwood Dr','Dacula','GA','30019','Y','Y'),(155,269,'5151 Maplewood Ave','Holly Springs','GA','30115','Y','Y'),(156,270,'5252 Willow Rd','Austell','GA','30106','Y','Y'),(157,274,'5353 Sycamore Ln','Jefferson','GA','30549','Y','Y'),(158,275,'5454 Cedarwood St','Palmetto','GA','30268','Y','Y'),(159,276,'5555 Elmwood Ave','Flowery Branch','GA','30542','Y','Y'),(160,277,'5656 Pinecrest Dr','Dallas','GA','30132','Y','Y'),(161,278,'5757 Birchwood Rd','Loganville','GA','30052','Y','Y'),(162,279,'5858 Dogwood Ave','Grayson','GA','30017','Y','Y'),(163,280,'5959 Hickory St','Braselton','GA','30517','Y','Y'),(164,282,'6060 Oakwood Dr','Buford','GA','30518','Y','Y'),(165,283,'6161 Maplewood Ave','Cumming','GA','30041','Y','Y'),(166,284,'6262 Willow Rd','Gainesville','GA','30506','Y','Y'),(167,285,'6363 Sycamore Ln','Jefferson','GA','30549','Y','Y'),(168,286,'6464 Cedarwood St','Dacula','GA','30019','Y','Y'),(169,288,'6565 Elmwood Ave','Flowery Branch','GA','30542','Y','Y'),(170,289,'6666 Pinecrest Dr','Dallas','GA','30132','Y','Y'),(171,290,'6767 Birchwood Rd','Loganville','GA','30052','Y','Y'),(172,291,'6868 Dogwood Ave','Grayson','GA','30017','Y','Y'),(173,293,'6969 Hickory St','Braselton','GA','30517','Y','Y'),(174,294,'7070 Oakwood Dr','Buford','GA','30518','Y','Y'),(175,295,'7171 Maplewood Ave','Cumming','GA','30041','Y','Y'),(176,296,'7272 Willow Rd','Gainesville','GA','30506','Y','Y'),(177,297,'7373 Sycamore Ln','Jefferson','GA','30549','Y','Y'),(178,299,'7474 Cedarwood St','Dacula','GA','30019','Y','Y'),(179,300,'7575 Elmwood Ave','Flowery Branch','GA','30542','Y','Y'),(180,301,'7676 Pinecrest Dr','Dallas','GA','30132','Y','Y'),(181,303,'7777 Birchwood Rd','Loganville','GA','30052','Y','Y'),(182,304,'7878 Dogwood Ave','Grayson','GA','30017','Y','Y'),(183,305,'7979 Hickory St','Braselton','GA','30517','Y','Y'),(184,306,'8080 Oakwood Dr','Buford','GA','30518','Y','Y'),(185,307,'8181 Maplewood Ave','Cumming','GA','30041','Y','Y'),(186,308,'8282 Willow Rd','Gainesville','GA','30506','Y','Y'),(187,309,'8383 Sycamore Ln','Jefferson','GA','30549','Y','Y'),(188,310,'8484 Cedarwood St','Dacula','GA','30019','Y','Y'),(189,311,'8585 Elmwood Ave','Flowery Branch','GA','30542','Y','Y'),(190,312,'456 Magnolia Ave','Savannah','GA','31401','Y','Y'),(191,313,'789 River Rd','Augusta','GA','30901','Y','Y'),(192,314,'101 Dogwood Dr','Macon','GA','31201','Y','Y'),(193,315,'234 Oak St','Athens','GA','30601','Y','Y'),(194,320,'567 Maple Ave','Columbus','GA','31901','Y','Y'),(195,321,'890 Pine St','Albany','GA','31701','Y','Y'),(196,322,'111 Cedar Ln','Valdosta','GA','31601','Y','Y'),(197,323,'222 Elm St','Gainesville','GA','30501','Y','Y'),(198,324,'333 Walnut Ave','Rome','GA','30161','Y','Y');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-21 16:44:59
