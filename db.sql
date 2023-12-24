/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - mockinter
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mockinter` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `mockinter`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add chat',7,'add_chat'),
(26,'Can change chat',7,'change_chat'),
(27,'Can delete chat',7,'delete_chat'),
(28,'Can view chat',7,'view_chat'),
(29,'Can add company',8,'add_company'),
(30,'Can change company',8,'change_company'),
(31,'Can delete company',8,'delete_company'),
(32,'Can view company',8,'view_company'),
(33,'Can add guide',9,'add_guide'),
(34,'Can change guide',9,'change_guide'),
(35,'Can delete guide',9,'delete_guide'),
(36,'Can view guide',9,'view_guide'),
(37,'Can add login',10,'add_login'),
(38,'Can change login',10,'change_login'),
(39,'Can delete login',10,'delete_login'),
(40,'Can view login',10,'view_login'),
(41,'Can add questions',11,'add_questions'),
(42,'Can change questions',11,'change_questions'),
(43,'Can delete questions',11,'delete_questions'),
(44,'Can view questions',11,'view_questions'),
(45,'Can add vaccancy',12,'add_vaccancy'),
(46,'Can change vaccancy',12,'change_vaccancy'),
(47,'Can delete vaccancy',12,'delete_vaccancy'),
(48,'Can view vaccancy',12,'view_vaccancy'),
(49,'Can add vac_qn',13,'add_vac_qn'),
(50,'Can change vac_qn',13,'change_vac_qn'),
(51,'Can delete vac_qn',13,'delete_vac_qn'),
(52,'Can view vac_qn',13,'view_vac_qn'),
(53,'Can add user',14,'add_user'),
(54,'Can change user',14,'change_user'),
(55,'Can delete user',14,'delete_user'),
(56,'Can view user',14,'view_user'),
(57,'Can add upload',15,'add_upload'),
(58,'Can change upload',15,'change_upload'),
(59,'Can delete upload',15,'delete_upload'),
(60,'Can view upload',15,'view_upload'),
(61,'Can add tip',16,'add_tip'),
(62,'Can change tip',16,'change_tip'),
(63,'Can delete tip',16,'delete_tip'),
(64,'Can view tip',16,'view_tip'),
(65,'Can add test_result',17,'add_test_result'),
(66,'Can change test_result',17,'change_test_result'),
(67,'Can delete test_result',17,'delete_test_result'),
(68,'Can view test_result',17,'view_test_result'),
(69,'Can add test',18,'add_test'),
(70,'Can change test',18,'change_test'),
(71,'Can delete test',18,'delete_test'),
(72,'Can view test',18,'view_test'),
(73,'Can add review',19,'add_review'),
(74,'Can change review',19,'change_review'),
(75,'Can delete review',19,'delete_review'),
(76,'Can view review',19,'view_review'),
(77,'Can add guideline',20,'add_guideline'),
(78,'Can change guideline',20,'change_guideline'),
(79,'Can delete guideline',20,'delete_guideline'),
(80,'Can view guideline',20,'view_guideline'),
(81,'Can add doubt',21,'add_doubt'),
(82,'Can change doubt',21,'change_doubt'),
(83,'Can delete doubt',21,'delete_doubt'),
(84,'Can view doubt',21,'view_doubt'),
(85,'Can add complaint',22,'add_complaint'),
(86,'Can change complaint',22,'change_complaint'),
(87,'Can delete complaint',22,'delete_complaint'),
(88,'Can view complaint',22,'view_complaint'),
(89,'Can add app_req',23,'add_app_req'),
(90,'Can change app_req',23,'change_app_req'),
(91,'Can delete app_req',23,'delete_app_req'),
(92,'Can view app_req',23,'view_app_req'),
(93,'Can add answer_details',24,'add_answer_details'),
(94,'Can change answer_details',24,'change_answer_details'),
(95,'Can delete answer_details',24,'delete_answer_details'),
(96,'Can view answer_details',24,'view_answer_details'),
(97,'Can add complaint_table',22,'add_complaint_table'),
(98,'Can change complaint_table',22,'change_complaint_table'),
(99,'Can delete complaint_table',22,'delete_complaint_table'),
(100,'Can view complaint_table',22,'view_complaint_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(24,'interview','answer_details'),
(23,'interview','app_req'),
(7,'interview','chat'),
(8,'interview','company'),
(22,'interview','complaint_table'),
(21,'interview','doubt'),
(9,'interview','guide'),
(20,'interview','guideline'),
(10,'interview','login'),
(11,'interview','questions'),
(19,'interview','review'),
(18,'interview','test'),
(17,'interview','test_result'),
(16,'interview','tip'),
(15,'interview','upload'),
(14,'interview','user'),
(13,'interview','vac_qn'),
(12,'interview','vaccancy'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-12-01 07:21:49.228766'),
(2,'auth','0001_initial','2023-12-01 07:21:49.525699'),
(3,'admin','0001_initial','2023-12-01 07:21:49.588103'),
(4,'admin','0002_logentry_remove_auto_add','2023-12-01 07:21:49.588103'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-12-01 07:21:49.603783'),
(6,'contenttypes','0002_remove_content_type_name','2023-12-01 07:21:49.650694'),
(7,'auth','0002_alter_permission_name_max_length','2023-12-01 07:21:49.681833'),
(8,'auth','0003_alter_user_email_max_length','2023-12-01 07:21:49.713188'),
(9,'auth','0004_alter_user_username_opts','2023-12-01 07:21:49.713188'),
(10,'auth','0005_alter_user_last_login_null','2023-12-01 07:21:49.744464'),
(11,'auth','0006_require_contenttypes_0002','2023-12-01 07:21:49.744464'),
(12,'auth','0007_alter_validators_add_error_messages','2023-12-01 07:21:49.760033'),
(13,'auth','0008_alter_user_username_max_length','2023-12-01 07:21:49.791241'),
(14,'auth','0009_alter_user_last_name_max_length','2023-12-01 07:21:49.822497'),
(15,'auth','0010_alter_group_name_max_length','2023-12-01 07:21:49.838107'),
(16,'auth','0011_update_proxy_permissions','2023-12-01 07:21:49.838107'),
(17,'auth','0012_alter_user_first_name_max_length','2023-12-01 07:21:49.885036'),
(18,'interview','0001_initial','2023-12-01 07:21:50.697548'),
(19,'sessions','0001_initial','2023-12-01 07:21:50.713164'),
(20,'interview','0002_rename_complaint_complaint_table','2023-12-12 06:57:05.507875');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('q1jcwj8zue7459xxn0xx0t4imzrfqcqr','eyJnaWQiOjQsImNpZCI6NDU2fQ:1rCwzb:cRcBMN9RQoJIWQkcEkP4MiHyzFgJFQNS05mA4n5iwHA','2023-12-26 07:15:47.536017');

/*Table structure for table `interview_answer_details` */

DROP TABLE IF EXISTS `interview_answer_details`;

CREATE TABLE `interview_answer_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ans` varchar(60) NOT NULL,
  `emot` varchar(60) NOT NULL,
  `date` date NOT NULL,
  `oans` varchar(60) NOT NULL,
  `user_id` bigint NOT NULL,
  `vac_qn_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_answer_details_user_id_cf7ec9cb_fk_interview_user_id` (`user_id`),
  KEY `interview_answer_det_vac_qn_id_164a0bbc_fk_interview` (`vac_qn_id`),
  CONSTRAINT `interview_answer_det_vac_qn_id_164a0bbc_fk_interview` FOREIGN KEY (`vac_qn_id`) REFERENCES `interview_vac_qn` (`id`),
  CONSTRAINT `interview_answer_details_user_id_cf7ec9cb_fk_interview_user_id` FOREIGN KEY (`user_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_answer_details` */

/*Table structure for table `interview_app_req` */

DROP TABLE IF EXISTS `interview_app_req`;

CREATE TABLE `interview_app_req` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(60) NOT NULL,
  `USER_id` bigint NOT NULL,
  `vaccancy_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_app_req_USER_id_58416952_fk_interview_user_id` (`USER_id`),
  KEY `interview_app_req_vaccancy_id_00516e4e_fk_interview_vaccancy_id` (`vaccancy_id`),
  CONSTRAINT `interview_app_req_USER_id_58416952_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`),
  CONSTRAINT `interview_app_req_vaccancy_id_00516e4e_fk_interview_vaccancy_id` FOREIGN KEY (`vaccancy_id`) REFERENCES `interview_vaccancy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_app_req` */

/*Table structure for table `interview_chat` */

DROP TABLE IF EXISTS `interview_chat`;

CREATE TABLE `interview_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `from_id` varchar(60) NOT NULL,
  `To_id` varchar(60) NOT NULL,
  `date` varchar(60) NOT NULL,
  `message` varchar(60) NOT NULL,
  `time` time(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_chat` */

/*Table structure for table `interview_company` */

DROP TABLE IF EXISTS `interview_company`;

CREATE TABLE `interview_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `place` varchar(60) NOT NULL,
  `phone` bigint NOT NULL,
  `Email` varchar(60) NOT NULL,
  `Wedsite` varchar(60) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_company_LOGIN_id_5635ef6c_fk_interview_login_id` (`LOGIN_id`),
  CONSTRAINT `interview_company_LOGIN_id_5635ef6c_fk_interview_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `interview_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_company` */

insert  into `interview_company`(`id`,`name`,`place`,`phone`,`Email`,`Wedsite`,`LOGIN_id`) values 
(27,'Abhishek ','cvb',987654321,'fgh','ikj',27),
(29,'ayana','vhh',1234567890,'nnh','fytg',29);

/*Table structure for table `interview_complaint_table` */

DROP TABLE IF EXISTS `interview_complaint_table`;

CREATE TABLE `interview_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Complaint` varchar(60) NOT NULL,
  `Date` date NOT NULL,
  `Reply` varchar(60) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_complaint_USER_id_2715c937_fk_interview_user_id` (`USER_id`),
  CONSTRAINT `interview_complaint_USER_id_2715c937_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=457 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_complaint_table` */

insert  into `interview_complaint_table`(`id`,`Complaint`,`Date`,`Reply`,`USER_id`) values 
(1,'bvcf','2023-12-20','545te5t',1234),
(124,'bsdhj','2024-01-04','great',125),
(456,'jfsj','2023-12-06','super',1234);

/*Table structure for table `interview_doubt` */

DROP TABLE IF EXISTS `interview_doubt`;

CREATE TABLE `interview_doubt` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(60) NOT NULL,
  `reply` varchar(60) NOT NULL,
  `date` date NOT NULL,
  `GUIDE_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_doubt_GUIDE_id_e49dfbb5_fk_interview_guide_id` (`GUIDE_id`),
  KEY `interview_doubt_USER_id_f2131e4e_fk_interview_user_id` (`USER_id`),
  CONSTRAINT `interview_doubt_GUIDE_id_e49dfbb5_fk_interview_guide_id` FOREIGN KEY (`GUIDE_id`) REFERENCES `interview_guide` (`id`),
  CONSTRAINT `interview_doubt_USER_id_f2131e4e_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_doubt` */

/*Table structure for table `interview_guide` */

DROP TABLE IF EXISTS `interview_guide`;

CREATE TABLE `interview_guide` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `First_name` varchar(60) NOT NULL,
  `Last_name` varchar(60) NOT NULL,
  `Address` varchar(60) NOT NULL,
  `Phone` bigint NOT NULL,
  `Email` varchar(60) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_guide_LOGIN_id_027a7902_fk_interview_login_id` (`LOGIN_id`),
  CONSTRAINT `interview_guide_LOGIN_id_027a7902_fk_interview_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `interview_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_guide` */

insert  into `interview_guide`(`id`,`First_name`,`Last_name`,`Address`,`Phone`,`Email`,`LOGIN_id`) values 
(6,'sdff','ghjk','bvhgfu',1234,'fghgv',15),
(7,'','','',9876543,' fghj',17),
(8,'','','',-987,'nm,',18),
(9,'','','',987654,'fvbnm',19),
(10,'','','',8157595599,'abhishek456@gmail.com',20),
(11,'','','',78965412,'gyg',27),
(12,'','','',1234567890,'hgjgujh',28),
(13,'','','',1234567890,'hgjgujh',29);

/*Table structure for table `interview_guideline` */

DROP TABLE IF EXISTS `interview_guideline`;

CREATE TABLE `interview_guideline` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `guidelines` varchar(60) NOT NULL,
  `details` varchar(60) NOT NULL,
  `COMPANY_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_guideline_COMPANY_id_ab00298a_fk_interview_company_id` (`COMPANY_id`),
  CONSTRAINT `interview_guideline_COMPANY_id_ab00298a_fk_interview_company_id` FOREIGN KEY (`COMPANY_id`) REFERENCES `interview_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_guideline` */

/*Table structure for table `interview_login` */

DROP TABLE IF EXISTS `interview_login`;

CREATE TABLE `interview_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `type` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_login` */

insert  into `interview_login`(`id`,`username`,`password`,`type`) values 
(3,'bvf','567','guide'),
(4,'bvf','bvf','guide'),
(5,'yuio','098','guide'),
(6,'nbgh','nbgh','guide'),
(7,'vcgf','123','user'),
(8,' nmn ',' 567','guide'),
(9,'adminhhhhhh','hh','guide'),
(10,'jjjjj','78','user'),
(15,';nknk','465','user'),
(16,'admin','123','admin'),
(17,'123','123','company'),
(18,'','mm','company'),
(19,'','00','pending'),
(20,'','59888','pending'),
(21,'','123','pending'),
(22,'','12345ty','pending'),
(23,'','12345ty','pending'),
(24,'','12345ty','pending'),
(25,'','12345ty','pending'),
(26,'','12345ty','pending'),
(27,'','123','company'),
(28,'','','company'),
(29,'','1234','block');

/*Table structure for table `interview_questions` */

DROP TABLE IF EXISTS `interview_questions`;

CREATE TABLE `interview_questions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Question` varchar(60) NOT NULL,
  `option1` varchar(60) NOT NULL,
  `option2` varchar(60) NOT NULL,
  `option3` varchar(60) NOT NULL,
  `option4` varchar(60) NOT NULL,
  `Answer` varchar(60) NOT NULL,
  `TEST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_questions_TEST_id_dc892f71_fk_interview_test_id` (`TEST_id`),
  CONSTRAINT `interview_questions_TEST_id_dc892f71_fk_interview_test_id` FOREIGN KEY (`TEST_id`) REFERENCES `interview_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_questions` */

/*Table structure for table `interview_review` */

DROP TABLE IF EXISTS `interview_review`;

CREATE TABLE `interview_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review` varchar(60) NOT NULL,
  `date` date NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_review_LOGIN_id_b0ce9e09_fk_interview_login_id` (`LOGIN_id`),
  KEY `interview_review_USER_id_999c70c4_fk_interview_user_id` (`USER_id`),
  CONSTRAINT `interview_review_LOGIN_id_b0ce9e09_fk_interview_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `interview_login` (`id`),
  CONSTRAINT `interview_review_USER_id_999c70c4_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_review` */

insert  into `interview_review`(`id`,`review`,`date`,`LOGIN_id`,`USER_id`) values 
(1,'dfg','2023-11-30',4,125);

/*Table structure for table `interview_test` */

DROP TABLE IF EXISTS `interview_test`;

CREATE TABLE `interview_test` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Exam_name` varchar(60) NOT NULL,
  `date` varchar(60) NOT NULL,
  `GUIDE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_test_GUIDE_id_98c3b2dc_fk_interview_guide_id` (`GUIDE_id`),
  CONSTRAINT `interview_test_GUIDE_id_98c3b2dc_fk_interview_guide_id` FOREIGN KEY (`GUIDE_id`) REFERENCES `interview_guide` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_test` */

/*Table structure for table `interview_test_result` */

DROP TABLE IF EXISTS `interview_test_result`;

CREATE TABLE `interview_test_result` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `res` varchar(60) NOT NULL,
  `ans` varchar(60) NOT NULL,
  `USER_id` bigint NOT NULL,
  `quetion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_test_result_USER_id_7aedb3c9_fk_interview_user_id` (`USER_id`),
  KEY `interview_test_resul_quetion_id_f3a8e203_fk_interview` (`quetion_id`),
  CONSTRAINT `interview_test_resul_quetion_id_f3a8e203_fk_interview` FOREIGN KEY (`quetion_id`) REFERENCES `interview_questions` (`id`),
  CONSTRAINT `interview_test_result_USER_id_7aedb3c9_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_test_result` */

/*Table structure for table `interview_tip` */

DROP TABLE IF EXISTS `interview_tip`;

CREATE TABLE `interview_tip` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tips` varchar(60) NOT NULL,
  `details` varchar(60) NOT NULL,
  `GUIDE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_tip_GUIDE_id_22119123_fk_interview_guide_id` (`GUIDE_id`),
  CONSTRAINT `interview_tip_GUIDE_id_22119123_fk_interview_guide_id` FOREIGN KEY (`GUIDE_id`) REFERENCES `interview_guide` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_tip` */

/*Table structure for table `interview_upload` */

DROP TABLE IF EXISTS `interview_upload`;

CREATE TABLE `interview_upload` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cv` varchar(60) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_upload_USER_id_e5b81d02_fk_interview_user_id` (`USER_id`),
  CONSTRAINT `interview_upload_USER_id_e5b81d02_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_upload` */

/*Table structure for table `interview_user` */

DROP TABLE IF EXISTS `interview_user`;

CREATE TABLE `interview_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `First_name` varchar(60) NOT NULL,
  `Last_name` varchar(60) NOT NULL,
  `gender` varchar(60) NOT NULL,
  `place` varchar(60) NOT NULL,
  `post` varchar(60) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(60) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_user_LOGIN_id_65969405_fk_interview_login_id` (`LOGIN_id`),
  CONSTRAINT `interview_user_LOGIN_id_65969405_fk_interview_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `interview_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1235 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_user` */

insert  into `interview_user`(`id`,`First_name`,`Last_name`,`gender`,`place`,`post`,`pin`,`phone`,`email`,`LOGIN_id`) values 
(124,'sfsf','sdfsdf','sdfs','fsf','fsdf',789,789,'hgjg',7),
(125,'dfg','dlkfj','jdslkf','flsdkj','dlf',9869,5566,'ggdg',10),
(1234,'spjjj','po','dfg','jakfks','hakfk ',785,8662,'snsdb',4);

/*Table structure for table `interview_vac_qn` */

DROP TABLE IF EXISTS `interview_vac_qn`;

CREATE TABLE `interview_vac_qn` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Question` longtext NOT NULL,
  `Answer` varchar(500) NOT NULL,
  `vaccancy_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_vac_qn_vaccancy_id_7b6ce06e_fk_interview_vaccancy_id` (`vaccancy_id`),
  CONSTRAINT `interview_vac_qn_vaccancy_id_7b6ce06e_fk_interview_vaccancy_id` FOREIGN KEY (`vaccancy_id`) REFERENCES `interview_vaccancy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_vac_qn` */

/*Table structure for table `interview_vaccancy` */

DROP TABLE IF EXISTS `interview_vaccancy`;

CREATE TABLE `interview_vaccancy` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `job` varchar(600) NOT NULL,
  `vaccancy` varchar(60) NOT NULL,
  `qualification` varchar(60) NOT NULL,
  `exp` varchar(60) NOT NULL,
  `salary` varchar(60) NOT NULL,
  `details` varchar(700) NOT NULL,
  `COMPANY_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_vaccancy_COMPANY_id_e683c8bd_fk_interview_company_id` (`COMPANY_id`),
  CONSTRAINT `interview_vaccancy_COMPANY_id_e683c8bd_fk_interview_company_id` FOREIGN KEY (`COMPANY_id`) REFERENCES `interview_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_vaccancy` */

insert  into `interview_vaccancy`(`id`,`job`,`vaccancy`,`qualification`,`exp`,`salary`,`details`,`COMPANY_id`) values 
(1,'developers ','gghj','bca','8','52','lkjhgf',27);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
