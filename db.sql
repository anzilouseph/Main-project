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
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(25,'Can add company',7,'add_company'),
(26,'Can change company',7,'change_company'),
(27,'Can delete company',7,'delete_company'),
(28,'Can view company',7,'view_company'),
(29,'Can add guide',8,'add_guide'),
(30,'Can change guide',8,'change_guide'),
(31,'Can delete guide',8,'delete_guide'),
(32,'Can view guide',8,'view_guide'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add questions',10,'add_questions'),
(38,'Can change questions',10,'change_questions'),
(39,'Can delete questions',10,'delete_questions'),
(40,'Can view questions',10,'view_questions'),
(41,'Can add vaccancy',11,'add_vaccancy'),
(42,'Can change vaccancy',11,'change_vaccancy'),
(43,'Can delete vaccancy',11,'delete_vaccancy'),
(44,'Can view vaccancy',11,'view_vaccancy'),
(45,'Can add vac_qn',12,'add_vac_qn'),
(46,'Can change vac_qn',12,'change_vac_qn'),
(47,'Can delete vac_qn',12,'delete_vac_qn'),
(48,'Can view vac_qn',12,'view_vac_qn'),
(49,'Can add user',13,'add_user'),
(50,'Can change user',13,'change_user'),
(51,'Can delete user',13,'delete_user'),
(52,'Can view user',13,'view_user'),
(53,'Can add upload',14,'add_upload'),
(54,'Can change upload',14,'change_upload'),
(55,'Can delete upload',14,'delete_upload'),
(56,'Can view upload',14,'view_upload'),
(57,'Can add tip',15,'add_tip'),
(58,'Can change tip',15,'change_tip'),
(59,'Can delete tip',15,'delete_tip'),
(60,'Can view tip',15,'view_tip'),
(61,'Can add test_result',16,'add_test_result'),
(62,'Can change test_result',16,'change_test_result'),
(63,'Can delete test_result',16,'delete_test_result'),
(64,'Can view test_result',16,'view_test_result'),
(65,'Can add test',17,'add_test'),
(66,'Can change test',17,'change_test'),
(67,'Can delete test',17,'delete_test'),
(68,'Can view test',17,'view_test'),
(69,'Can add review',18,'add_review'),
(70,'Can change review',18,'change_review'),
(71,'Can delete review',18,'delete_review'),
(72,'Can view review',18,'view_review'),
(73,'Can add guideline',19,'add_guideline'),
(74,'Can change guideline',19,'change_guideline'),
(75,'Can delete guideline',19,'delete_guideline'),
(76,'Can view guideline',19,'view_guideline'),
(77,'Can add doubt',20,'add_doubt'),
(78,'Can change doubt',20,'change_doubt'),
(79,'Can delete doubt',20,'delete_doubt'),
(80,'Can view doubt',20,'view_doubt'),
(81,'Can add complaint_table',21,'add_complaint_table'),
(82,'Can change complaint_table',21,'change_complaint_table'),
(83,'Can delete complaint_table',21,'delete_complaint_table'),
(84,'Can view complaint_table',21,'view_complaint_table'),
(85,'Can add chat',22,'add_chat'),
(86,'Can change chat',22,'change_chat'),
(87,'Can delete chat',22,'delete_chat'),
(88,'Can view chat',22,'view_chat'),
(89,'Can add app_req',23,'add_app_req'),
(90,'Can change app_req',23,'change_app_req'),
(91,'Can delete app_req',23,'delete_app_req'),
(92,'Can view app_req',23,'view_app_req'),
(93,'Can add answer_details',24,'add_answer_details'),
(94,'Can change answer_details',24,'change_answer_details'),
(95,'Can delete answer_details',24,'delete_answer_details'),
(96,'Can view answer_details',24,'view_answer_details');

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
(22,'interview','chat'),
(7,'interview','company'),
(21,'interview','complaint_table'),
(20,'interview','doubt'),
(8,'interview','guide'),
(19,'interview','guideline'),
(9,'interview','login'),
(10,'interview','questions'),
(18,'interview','review'),
(17,'interview','test'),
(16,'interview','test_result'),
(15,'interview','tip'),
(14,'interview','upload'),
(13,'interview','user'),
(12,'interview','vac_qn'),
(11,'interview','vaccancy'),
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
(1,'contenttypes','0001_initial','2023-12-29 06:57:08.203819'),
(2,'auth','0001_initial','2023-12-29 06:57:08.755049'),
(3,'admin','0001_initial','2023-12-29 06:57:08.886358'),
(4,'admin','0002_logentry_remove_auto_add','2023-12-29 06:57:08.888626'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-12-29 06:57:08.888626'),
(6,'contenttypes','0002_remove_content_type_name','2023-12-29 06:57:09.008186'),
(7,'auth','0002_alter_permission_name_max_length','2023-12-29 06:57:09.048055'),
(8,'auth','0003_alter_user_email_max_length','2023-12-29 06:57:09.061486'),
(9,'auth','0004_alter_user_username_opts','2023-12-29 06:57:09.061486'),
(10,'auth','0005_alter_user_last_login_null','2023-12-29 06:57:09.130451'),
(11,'auth','0006_require_contenttypes_0002','2023-12-29 06:57:09.139095'),
(12,'auth','0007_alter_validators_add_error_messages','2023-12-29 06:57:09.141071'),
(13,'auth','0008_alter_user_username_max_length','2023-12-29 06:57:09.193998'),
(14,'auth','0009_alter_user_last_name_max_length','2023-12-29 06:57:09.251402'),
(15,'auth','0010_alter_group_name_max_length','2023-12-29 06:57:09.267604'),
(16,'auth','0011_update_proxy_permissions','2023-12-29 06:57:09.267604'),
(17,'auth','0012_alter_user_first_name_max_length','2023-12-29 06:57:09.315533'),
(18,'interview','0001_initial','2023-12-29 06:57:10.665389'),
(19,'sessions','0001_initial','2023-12-29 06:57:10.699478'),
(20,'interview','0002_auto_20240110_1302','2024-01-10 07:32:25.761921');

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
('3z63rf0alw71sz8xgetbalblwqfuz49y','eyJsaWQiOjQsImdpZCI6MywiY2lkIjoxfQ:1rQ1Pq:GdcnEDQmkSsh_Xqj4yGqTlIMidCfJs6MdcduWr0TB40','2024-01-31 08:36:54.613382');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_app_req` */

insert  into `interview_app_req`(`id`,`date`,`status`,`USER_id`,`vaccancy_id`) values 
(1,'2024-01-10','fghjk',1,1);

/*Table structure for table `interview_chat` */

DROP TABLE IF EXISTS `interview_chat`;

CREATE TABLE `interview_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(1000) NOT NULL,
  `fromid_id` bigint NOT NULL,
  `toid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_chat_fromid_id_bbae6827_fk_interview_login_id` (`fromid_id`),
  KEY `interview_chat_toid_id_06203e8b_fk_interview_login_id` (`toid_id`),
  CONSTRAINT `interview_chat_fromid_id_bbae6827_fk_interview_login_id` FOREIGN KEY (`fromid_id`) REFERENCES `interview_login` (`id`),
  CONSTRAINT `interview_chat_toid_id_06203e8b_fk_interview_login_id` FOREIGN KEY (`toid_id`) REFERENCES `interview_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_chat` */

insert  into `interview_chat`(`id`,`date`,`message`,`fromid_id`,`toid_id`) values 
(1,'2023-12-29','hi',2,3),
(2,'2023-12-29','hlo',3,2);

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_company` */

insert  into `interview_company`(`id`,`name`,`place`,`phone`,`Email`,`Wedsite`,`LOGIN_id`) values 
(1,'infosys','Ekm',987654343213,'infosys@gmail.com','www.infosys.com',2),
(2,'amal','calicut',787899099,'amal@gmail.com','',9);

/*Table structure for table `interview_complaint_table` */

DROP TABLE IF EXISTS `interview_complaint_table`;

CREATE TABLE `interview_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Complaint` varchar(60) NOT NULL,
  `Date` date NOT NULL,
  `Reply` varchar(60) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_complaint_table_USER_id_4abac489_fk_interview_user_id` (`USER_id`),
  CONSTRAINT `interview_complaint_table_USER_id_4abac489_fk_interview_user_id` FOREIGN KEY (`USER_id`) REFERENCES `interview_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_complaint_table` */

insert  into `interview_complaint_table`(`id`,`Complaint`,`Date`,`Reply`,`USER_id`) values 
(1,'fgdfg','2024-01-10','dfg',1);

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_doubt` */

insert  into `interview_doubt`(`id`,`doubt`,`reply`,`date`,`GUIDE_id`,`USER_id`) values 
(1,'dfgh','jyfj','2024-01-10',1,1);

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_guide` */

insert  into `interview_guide`(`id`,`First_name`,`Last_name`,`Address`,`Phone`,`Email`,`LOGIN_id`) values 
(1,'ayana','k',' calicut',78945621232,'ayana@gmail.com',4);

/*Table structure for table `interview_guideline` */

DROP TABLE IF EXISTS `interview_guideline`;

CREATE TABLE `interview_guideline` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `guidelines` varchar(60) NOT NULL,
  `details` varchar(60) NOT NULL,
  `GUIDE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_guideline_GUIDE_id_3cd30da5_fk_interview_guide_id` (`GUIDE_id`),
  CONSTRAINT `interview_guideline_GUIDE_id_3cd30da5_fk_interview_guide_id` FOREIGN KEY (`GUIDE_id`) REFERENCES `interview_guide` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_guideline` */

insert  into `interview_guideline`(`id`,`guidelines`,`details`,`GUIDE_id`) values 
(1,'ktyui','ghj',1),
(2,'dwdwq','DWD',1),
(3,'rtyu','ghjk',1);

/*Table structure for table `interview_login` */

DROP TABLE IF EXISTS `interview_login`;

CREATE TABLE `interview_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `type` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_login` */

insert  into `interview_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'company','123','company'),
(3,'user','123','user'),
(4,'guide','123','guide'),
(5,'nghmg','123','guide'),
(6,'nghmg','123','guide'),
(8,'','','guide'),
(9,'amal','amal','pending');

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_questions` */

insert  into `interview_questions`(`id`,`Question`,`option1`,`option2`,`option3`,`option4`,`Answer`,`TEST_id`) values 
(1,'jmb','n','ddg','daff','dafdfhd','dhd',3),
(3,'abcd','bcda','jkl','isl','sjfl','iwyeuf',3),
(7,'rtui','r','u','y','t','k',3);

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_review` */

insert  into `interview_review`(`id`,`review`,`date`,`LOGIN_id`,`USER_id`) values 
(2,'super','2024-01-08',3,1);

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_test` */

insert  into `interview_test`(`id`,`Exam_name`,`date`,`GUIDE_id`) values 
(3,'final','2023-12-29 14:09:11.769114',1),
(5,'midterm','2024-01-01 20:10:32.702073',1);

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_tip` */

insert  into `interview_tip`(`id`,`tips`,`details`,`GUIDE_id`) values 
(1,'','',1),
(2,'dfgh','ertyu',1),
(3,'rtyui','fghj',1),
(4,'ghj','ghjk',1),
(5,'tyu','hjk',1),
(6,'abcdef','fedddd',1);

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
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_user_LOGIN_id_65969405_fk_interview_login_id` (`LOGIN_id`),
  CONSTRAINT `interview_user_LOGIN_id_65969405_fk_interview_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `interview_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_user` */

insert  into `interview_user`(`id`,`First_name`,`Last_name`,`gender`,`place`,`post`,`pin`,`phone`,`email`,`photo`,`LOGIN_id`) values 
(1,'Abhinav','A S','Male','Calicut','Calicut',654321,9876543212,'abhi@gmail.com','(NULL)Adsfws',3);

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
  `Vaccancy` varchar(60) NOT NULL,
  `qualification` varchar(60) NOT NULL,
  `exp` varchar(60) NOT NULL,
  `salary` varchar(60) NOT NULL,
  `details` varchar(700) NOT NULL,
  `COMPANY_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interview_vaccancy_COMPANY_id_e683c8bd_fk_interview_company_id` (`COMPANY_id`),
  CONSTRAINT `interview_vaccancy_COMPANY_id_e683c8bd_fk_interview_company_id` FOREIGN KEY (`COMPANY_id`) REFERENCES `interview_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `interview_vaccancy` */

insert  into `interview_vaccancy`(`id`,`job`,`Vaccancy`,`qualification`,`exp`,`salary`,`details`,`COMPANY_id`) values 
(1,'testr5','yh','+2','2 year','12300','hghjk',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
