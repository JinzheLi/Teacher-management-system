/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.25 : Database - teacher_qualified
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`teacher_qualified` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `teacher_qualified`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `no` char(8) NOT NULL COMMENT '用户名',
  `password` char(32) NOT NULL COMMENT '密码',
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `admin` */

insert  into `admin`(`no`,`password`) values ('1','c4ca4238a0b923820dcc509a6f75849b'),('admin','21232f297a57a5a743894a0e4a801fc3'),('root','63a9f0ea7bb98050796b649e85481845');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2019-12-31 01:48:14.649918'),(2,'auth','0001_initial','2019-12-31 01:48:16.101807'),(3,'admin','0001_initial','2019-12-31 01:48:21.797580'),(4,'admin','0002_logentry_remove_auto_add','2019-12-31 01:48:22.659814'),(5,'admin','0003_logentry_add_action_flag_choices','2019-12-31 01:48:22.706688'),(6,'admin','0004_auto_20190420_1102','2019-12-31 01:48:22.735610'),(7,'admin','0005_auto_20190703_2210','2019-12-31 01:48:22.762538'),(8,'contenttypes','0002_remove_content_type_name','2019-12-31 01:48:23.358375'),(9,'auth','0002_alter_permission_name_max_length','2019-12-31 01:48:23.729221'),(10,'auth','0003_alter_user_email_max_length','2019-12-31 01:48:24.517468'),(11,'auth','0004_alter_user_username_opts','2019-12-31 01:48:24.557368'),(12,'auth','0005_alter_user_last_login_null','2019-12-31 01:48:24.951392'),(13,'auth','0006_require_contenttypes_0002','2019-12-31 01:48:24.991446'),(14,'auth','0007_alter_validators_add_error_messages','2019-12-31 01:48:25.021354'),(15,'auth','0008_alter_user_username_max_length','2019-12-31 01:48:25.528000'),(16,'auth','0009_alter_user_last_name_max_length','2019-12-31 01:48:26.120829'),(17,'auth','0010_alter_group_name_max_length','2019-12-31 01:48:26.618275'),(18,'auth','0011_update_proxy_permissions','2019-12-31 01:48:26.647197'),(19,'auth','0012_auto_20190420_1102','2019-12-31 01:48:27.160659'),(20,'auth','0013_auto_20190703_2210','2019-12-31 01:48:28.082684'),(21,'sessions','0001_initial','2019-12-31 01:48:28.306712');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('ilvpii8i5njh6yyyorw8q9abl62q26g7','NzA5ZDU2OWQwNDllNmMyZWRkZjg5ZWFkZjM2YjFmZDNhNjYxZTdlMjp7Imd0X3NlcnZlcl9zdGF0dXMiOjEsInVzZXJfaWQiOiJ0ZXN0IiwidmVyaWZ5Y29kZSI6IjQ0NjUiLCJhZG1pbnVzZXIiOnsibm8iOiJyb290IiwicGFzc3dvcmQiOiI2M2E5ZjBlYTdiYjk4MDUwNzk2YjY0OWU4NTQ4MTg0NSJ9fQ==','2020-01-20 02:33:34.648538'),('xfauy1uy2xk8sqmjmz6c99mg6rqtc0un','NGFhMmJjY2ViNzVhY2FjZjA4ZjBlYTkwMThhZmFkOTU3NWJjM2IxYzp7InZlcmlmeWNvZGUiOiI4NDk1In0=','2020-01-20 02:33:12.769845');

/*Table structure for table `faculty` */

DROP TABLE IF EXISTS `faculty`;

CREATE TABLE `faculty` (
  `no` char(8) NOT NULL COMMENT '编号',
  `name` char(10) NOT NULL COMMENT '学院名',
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `faculty` */

insert  into `faculty`(`no`,`name`) values ('01','理学院'),('02','机电与车辆工程学院'),('03','建筑与城市规划学院'),('04','土木与交通工程学院'),('05','环境与能源工程学院'),('06','电气与信息工程学院'),('07','经济与管理工程学院'),('08','测绘与城市空间信息学'),('09','文法学院'),('10','马克思主义学院'),('11','体育教研部'),('12','继续教育学院'),('13','国际教育学院'),('14','创新创业教育学院');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `no` char(20) NOT NULL COMMENT '编号',
  `name` char(10) NOT NULL COMMENT '姓名',
  `score` float NOT NULL COMMENT '学分',
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `subject` */

insert  into `subject`(`no`,`name`,`score`) values ('20821038','中国近现代史纲要',2),('20921008','常微分方程',2),('20921051','数学分析（3）',3),('20921092','数学分析（1）',5),('20921093','数学分析（2）',5),('20926112','专业英语',1.5),('20926134','C程序设计',3),('20926136','数据结构与算法',2.5),('20927011','面向对象程序设计',2);

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `no` char(20) NOT NULL COMMENT '教师号',
  `faculty` char(8) NOT NULL COMMENT '学院号',
  `password` char(32) NOT NULL COMMENT '密码',
  `name` char(20) NOT NULL COMMENT '姓名',
  `age` smallint(3) unsigned NOT NULL COMMENT '年龄',
  `sex` char(2) NOT NULL COMMENT '性别',
  `position` char(10) NOT NULL COMMENT '职称',
  `degree` char(6) NOT NULL COMMENT '学历',
  `phone` char(11) DEFAULT NULL COMMENT '电话',
  PRIMARY KEY (`no`),
  KEY `FK_teacher_faculty` (`faculty`),
  CONSTRAINT `FK_teacher_faculty` FOREIGN KEY (`faculty`) REFERENCES `faculty` (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `teacher` */

insert  into `teacher`(`no`,`faculty`,`password`,`name`,`age`,`sex`,`position`,`degree`,`phone`) values ('124708030481','11','670b14728ad9902aecba32e22fa4f6bd','张三丰',80,'1','副教授','博士研究生','13691111111'),('145204152419','01','670b14728ad9902aecba32e22fa4f6bd','莱昂纳多·迪·皮耶罗·达·芬奇',42,'1','教授','博士研究生','13697893142'),('178039451287','01','670b14728ad9902aecba32e22fa4f6bd','让·巴普蒂斯·约瑟夫·傅里叶',55,'1','教授','本科','13691111367'),('178908010125','01','670b14728ad9902aecba32e22fa4f6bd','柯西',60,'1','教授','博士研究生','13691785111'),('181805053687','10','670b14728ad9902aecba32e22fa4f6bd','卡尔·海因里希·马克思',43,'1','教授','硕士研究生','13641671342'),('187302231486','09','670b14728ad9902aecba32e22fa4f6bd','梁启超',25,'1','讲师','本科','13699753342'),('191206230571','01','670b14728ad9902aecba32e22fa4f6bd','Alan Mathison Turing',36,'1','副教授','博士研究生','13691451342'),('195510282017','13','670b14728ad9902aecba32e22fa4f6bd','威廉·亨利·盖茨三世',58,'1','教授','硕士研究生','13691971257'),('195808163741','13','670b14728ad9902aecba32e22fa4f6bd','Madonna Ciccone',25,'0','副教授','本科','13691753190'),('201705126874','03','670b14728ad9902aecba32e22fa4f6bd','张胜男',30,'0','讲师','博士研究生','13697777777');

/*Table structure for table `teaching` */

DROP TABLE IF EXISTS `teaching`;

CREATE TABLE `teaching` (
  `no` char(20) NOT NULL COMMENT '教师',
  `subject` char(20) DEFAULT NULL,
  `class` char(50) DEFAULT NULL,
  PRIMARY KEY (`no`),
  KEY `subject` (`subject`),
  CONSTRAINT `teaching_ibfk_1` FOREIGN KEY (`no`) REFERENCES `teacher` (`no`),
  CONSTRAINT `teaching_ibfk_2` FOREIGN KEY (`subject`) REFERENCES `subject` (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `teaching` */

insert  into `teaching`(`no`,`subject`,`class`) values ('181805053687','20821038','基础楼A座-西侧23(大兴校区)'),('195510282017','20927011','基础楼C座-423(大兴校区)');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
