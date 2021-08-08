/*
 Navicat Premium Data Transfer

 Source Server         : My SQL
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : scoremanage

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 26/09/2020 10:20:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'studentManage', '0001_initial', '2019-12-18 22:24:42.418544');
INSERT INTO `django_migrations` VALUES (2, 'studentManage', '0002_auto_20200111_1442', '2020-01-11 14:43:33.594258');

-- ----------------------------
-- Table structure for studentmanage_choosesub
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_choosesub`;
CREATE TABLE `studentmanage_choosesub`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subjectID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `studentID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `isChoose` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_choosesub
-- ----------------------------
INSERT INTO `studentmanage_choosesub` VALUES (1, '1', 's001', 0);
INSERT INTO `studentmanage_choosesub` VALUES (2, '2', 's001', 0);
INSERT INTO `studentmanage_choosesub` VALUES (3, '3', 's001', 0);
INSERT INTO `studentmanage_choosesub` VALUES (7, '4', 's001', 0);
INSERT INTO `studentmanage_choosesub` VALUES (8, '5', 's001', 0);
INSERT INTO `studentmanage_choosesub` VALUES (9, '6', 's001', 0);

-- ----------------------------
-- Table structure for studentmanage_class
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_class`;
CREATE TABLE `studentmanage_class`  (
  `classID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `className` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`classID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_class
-- ----------------------------
INSERT INTO `studentmanage_class` VALUES ('0193217521', '软件一班');

-- ----------------------------
-- Table structure for studentmanage_score
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_score`;
CREATE TABLE `studentmanage_score`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `subjectID` int(11) NOT NULL,
  `classID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score` double NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_score
-- ----------------------------
INSERT INTO `studentmanage_score` VALUES (2, 's001', 2, '0193217521', 0);
INSERT INTO `studentmanage_score` VALUES (3, 's001', 3, '0193217521', 0);
INSERT INTO `studentmanage_score` VALUES (4, 's001', 4, '0193217521', 0);
INSERT INTO `studentmanage_score` VALUES (11, 's001', 5, '0193217521', 0);
INSERT INTO `studentmanage_score` VALUES (13, 's001', 6, '0193217521', 0);
INSERT INTO `studentmanage_score` VALUES (16, 's001', 1, '0193217521', 0);

-- ----------------------------
-- Table structure for studentmanage_student
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_student`;
CREATE TABLE `studentmanage_student`  (
  `studentID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `classID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`studentID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_student
-- ----------------------------
INSERT INTO `studentmanage_student` VALUES ('s001', '0193217521', '张三');

-- ----------------------------
-- Table structure for studentmanage_subject
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_subject`;
CREATE TABLE `studentmanage_subject`  (
  `subjectID` int(11) NOT NULL,
  `subjectName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacherID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`subjectID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_subject
-- ----------------------------
INSERT INTO `studentmanage_subject` VALUES (1, 'Python', 't001');
INSERT INTO `studentmanage_subject` VALUES (2, '大学英语', 't002');
INSERT INTO `studentmanage_subject` VALUES (3, 'C语言', 't003');
INSERT INTO `studentmanage_subject` VALUES (4, 'Android', 't004');
INSERT INTO `studentmanage_subject` VALUES (5, 'Java', 't005');
INSERT INTO `studentmanage_subject` VALUES (6, '网络安全', 't006');

-- ----------------------------
-- Table structure for studentmanage_teacher
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_teacher`;
CREATE TABLE `studentmanage_teacher`  (
  `teacherID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `classID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `isHeadmaster` tinyint(1) NOT NULL,
  PRIMARY KEY (`teacherID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_teacher
-- ----------------------------
INSERT INTO `studentmanage_teacher` VALUES ('t001', '王老师', '0193217521', 1);
INSERT INTO `studentmanage_teacher` VALUES ('t002', '李老师', '', 0);
INSERT INTO `studentmanage_teacher` VALUES ('t003', '汪老师', '', 0);

-- ----------------------------
-- Table structure for studentmanage_user
-- ----------------------------
DROP TABLE IF EXISTS `studentmanage_user`;
CREATE TABLE `studentmanage_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nickname` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `birthday` date NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roleID` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of studentmanage_user
-- ----------------------------
INSERT INTO `studentmanage_user` VALUES (1, 'admin', 'admin', '管理员', 0, '1997-11-08', '17762411423', '重庆', 0);
INSERT INTO `studentmanage_user` VALUES (2, 's001', '123456', '张三', 0, '1996-01-01', '12345678910', '湖北', 2);
INSERT INTO `studentmanage_user` VALUES (3, 't001', '666666', '王老师', 0, '1980-01-01', '12345678910', '湖北', 1);
INSERT INTO `studentmanage_user` VALUES (4, 's002', '123456', '王五', 0, '1997-01-01', '12345678910', '湖北', 2);

SET FOREIGN_KEY_CHECKS = 1;
