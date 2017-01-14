-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 09, 2016 at 03:59 
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.5.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `beasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add bio data', 7, 'add_biodata'),
(20, 'Can change bio data', 7, 'change_biodata'),
(21, 'Can delete bio data', 7, 'delete_biodata'),
(22, 'Can add bio data', 8, 'add_biodata'),
(23, 'Can change bio data', 8, 'change_biodata'),
(24, 'Can delete bio data', 8, 'delete_biodata'),
(25, 'Can add rekapitulasi', 9, 'add_rekapitulasi'),
(26, 'Can change rekapitulasi', 9, 'change_rekapitulasi'),
(27, 'Can delete rekapitulasi', 9, 'delete_rekapitulasi');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$24000$Dwb2icHjpkCE$vfCbE6ixPjYL73wBqpd6MZNphTax/BAzEXlUAgAfUqE=', '2016-06-08 13:06:36', 1, 'admin', '', '', 'fikrikhaidir@gmail.com', 1, 1, '2016-06-02 14:59:21');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `biodata_mhs`
--

CREATE TABLE `biodata_mhs` (
  `id` int(11) NOT NULL,
  `nama_lengkap` varchar(35) NOT NULL,
  `fakultas` varchar(40) NOT NULL,
  `prodi` varchar(40) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `alamat` tinytext NOT NULL,
  `ttl` tinytext NOT NULL,
  `semester` int(1) NOT NULL,
  `ipk` float NOT NULL,
  `tan` int(1) NOT NULL,
  `pot` float NOT NULL,
  `pre` float NOT NULL,
  `org` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `biodata_mhs`
--

INSERT INTO `biodata_mhs` (`id`, `nama_lengkap`, `fakultas`, `prodi`, `nim`, `alamat`, `ttl`, `semester`, `ipk`, `tan`, `pot`, `pre`, `org`) VALUES
(1, 'fikri khaidir', 'Komunikasi dan Informatika', 'Teknik Informatika', 'L200130058', 'jl kebangkitan adik kecil', 'pontianak 11 juli 1995', 6, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2016-06-03 14:19:10', '1', 'm', 1, 'Added.', 7, 1),
(2, '2016-06-08 13:17:35', '4', 'Fikri', 1, 'Added.', 7, 1),
(3, '2016-06-08 13:52:07', '6', 'test', 1, 'Added.', 7, 1),
(4, '2016-06-08 14:04:20', '10', 'arman', 1, 'Added.', 7, 1),
(5, '2016-06-08 14:05:26', '11', 'adi', 1, 'Added.', 7, 1),
(6, '2016-06-08 21:08:59', '10', 'Fikri', 1, 'Added.', 8, 1),
(7, '2016-06-08 21:17:27', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(8, '2016-06-08 21:18:06', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(9, '2016-06-08 21:22:06', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(10, '2016-06-08 21:22:21', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(11, '2016-06-08 21:24:33', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(12, '2016-06-08 21:25:07', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(13, '2016-06-08 21:25:30', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(14, '2016-06-08 21:26:23', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(15, '2016-06-08 21:27:27', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(16, '2016-06-08 21:28:49', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(17, '2016-06-08 21:29:16', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(18, '2016-06-08 21:31:14', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(19, '2016-06-09 03:43:27', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(20, '2016-06-09 03:45:33', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(21, '2016-06-09 03:46:12', '11', 'tes | tes', 1, 'Added.', 8, 1),
(22, '2016-06-09 03:50:43', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(23, '2016-06-09 03:52:48', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(24, '2016-06-09 03:53:14', '11', 'tes | tes', 2, 'No fields changed.', 8, 1),
(25, '2016-06-09 03:55:16', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(26, '2016-06-09 03:56:58', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(27, '2016-06-09 03:58:16', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(28, '2016-06-09 04:10:02', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(29, '2016-06-09 04:17:48', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(30, '2016-06-09 04:18:39', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(31, '2016-06-09 04:19:03', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(32, '2016-06-09 04:22:10', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(33, '2016-06-09 04:28:04', '10', 'Fikri | L200130058', 2, 'No fields changed.', 8, 1),
(34, '2016-06-09 04:41:17', '10', 'Fikri | L200130058', 2, 'Changed semester, ipk, tan, pot and pre.', 8, 1),
(35, '2016-06-09 04:45:39', '11', 'tes | tes', 3, '', 8, 1),
(36, '2016-06-09 05:07:27', '10', 'Fikri | L200130058 | 0.0', 2, 'No fields changed.', 8, 1),
(37, '2016-06-09 05:08:09', '10', 'Fikri | L200130058 | 0.0', 2, 'No fields changed.', 8, 1),
(38, '2016-06-09 05:20:28', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(39, '2016-06-09 05:23:52', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(40, '2016-06-09 05:24:19', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'Changed rekomendasi.', 8, 1),
(41, '2016-06-09 05:29:04', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'Changed rekomendasi.', 8, 1),
(42, '2016-06-09 05:29:38', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(43, '2016-06-09 05:30:44', '12', 'achmad | L200130059 | 2.8', 1, 'Added.', 8, 1),
(44, '2016-06-09 05:41:21', '10', 'Fikri | L200130058 | 0.0', 2, 'No fields changed.', 8, 1),
(45, '2016-06-09 05:41:41', '10', 'Fikri | L200130058 | 0.0', 2, 'No fields changed.', 8, 1),
(46, '2016-06-09 05:42:21', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(47, '2016-06-09 05:43:46', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(48, '2016-06-09 05:52:40', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(49, '2016-06-09 06:07:02', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(50, '2016-06-09 08:56:38', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(51, '2016-06-09 09:04:10', '10', 'Fikri | L200130058 | 3.17009230769', 2, 'No fields changed.', 8, 1),
(53, '2016-06-09 12:02:49', '13', 'Yusuf Zainuddin | L200130013 | 2.8', 1, 'Added.', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'forminput', 'biodata'),
(8, 'formulir', 'biodata'),
(9, 'formulir', 'rekapitulasi'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2016-06-02 14:52:17'),
(2, 'auth', '0001_initial', '2016-06-02 14:52:26'),
(3, 'admin', '0001_initial', '2016-06-02 14:52:28'),
(4, 'admin', '0002_logentry_remove_auto_add', '2016-06-02 14:52:28'),
(5, 'contenttypes', '0002_remove_content_type_name', '2016-06-02 14:52:29'),
(6, 'auth', '0002_alter_permission_name_max_length', '2016-06-02 14:52:29'),
(7, 'auth', '0003_alter_user_email_max_length', '2016-06-02 14:52:30'),
(8, 'auth', '0004_alter_user_username_opts', '2016-06-02 14:52:30'),
(9, 'auth', '0005_alter_user_last_login_null', '2016-06-02 14:52:31'),
(10, 'auth', '0006_require_contenttypes_0002', '2016-06-02 14:52:31'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2016-06-02 14:52:31'),
(12, 'sessions', '0001_initial', '2016-06-02 14:52:31'),
(13, 'forminput', '0001_initial', '2016-06-03 13:52:39'),
(14, 'formulir', '0001_initial', '2016-06-08 17:30:14'),
(15, 'formulir', '0002_coba_rekapitulasi', '2016-06-08 20:52:16'),
(16, 'formulir', '0003_auto_20160609_0354', '2016-06-09 03:54:51'),
(17, 'formulir', '0004_biodata_rekomendasi', '2016-06-09 05:01:44'),
(18, 'formulir', '0005_auto_20160609_0510', '2016-06-09 05:11:04'),
(19, 'formulir', '0006_auto_20160609_0525', '2016-06-09 11:52:22'),
(20, 'formulir', '0007_rekapitulasi', '2016-06-09 11:52:22');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3tzx6ys2ywa61trud3okobk8s5y4f5re', 'YWU4ZTMyYzhiMjA0MjdhMDE1MzI2YzJhM2Y1MTAxNzVhZTliYWY0MTp7Il9hdXRoX3VzZXJfaGFzaCI6ImVlYjY2YzE4MDhlYWQ1MDE5OWNiNTkwZmFjZjg5NmMxMmIxODE1ODQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-06-16 15:00:15'),
('zziia28dn1nm8i3ztkbpsjnwtvc9n0oc', 'OWNjY2MzMGEyNTVjNjg1ZjJjYWIxZGRmOWZmNjMxZmE2OTkxOTA0MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImJiY2I4NmFhMjExZDFlYWM1OGI2MDc5NTJmYzUxYWY0NzUxN2VmZTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-06-22 13:06:36');

-- --------------------------------------------------------

--
-- Table structure for table `forminput_biodata`
--

CREATE TABLE `forminput_biodata` (
  `id` int(11) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `fakultas` varchar(40) NOT NULL,
  `prodi` varchar(40) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `alamat` varchar(300) NOT NULL,
  `TanggalLahir` date NOT NULL,
  `semester` int(1) NOT NULL,
  `ipk` float NOT NULL,
  `tan` int(2) NOT NULL,
  `pot` int(11) NOT NULL,
  `pre` int(1) NOT NULL,
  `org` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `formulir_biodata`
--

CREATE TABLE `formulir_biodata` (
  `id` int(11) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `fakultas` varchar(40) NOT NULL,
  `prodi` varchar(40) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `alamat` varchar(300) NOT NULL,
  `TanggalLahir` date NOT NULL,
  `semester` int(11) NOT NULL,
  `ipk` float NOT NULL,
  `tan` int(11) NOT NULL,
  `pot` int(11) NOT NULL,
  `pre` int(11) NOT NULL,
  `org` int(11) NOT NULL,
  `rekomendasi` float
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `formulir_biodata`
--

INSERT INTO `formulir_biodata` (`id`, `nama`, `fakultas`, `prodi`, `nim`, `alamat`, `TanggalLahir`, `semester`, `ipk`, `tan`, `pot`, `pre`, `org`, `rekomendasi`) VALUES
(10, 'Fikri', 'FKI', 'Teknik Informatika', 'L200130058', 'jalan kebenaran', '2016-06-08', 6, 3.5, 3, 2000000, 2, 1, 0),
(12, 'achmad', 'fki', 'ti', 'L200130059', 'jalan kebangkitan adik kecil', '2016-06-09', 6, 3.5, 2, 2000000, 3, 3, 0),
(13, 'Yusuf Zainuddin', 'Kedokteran', 'Kedokteran Gigi', 'L200130013', 'Dimana saja saya suka', '2016-06-09', 6, 3.33, 3, 2000000, 3, 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `formulir_rekapitulasi`
--

CREATE TABLE `formulir_rekapitulasi` (
  `id` int(11) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `ipk` double NOT NULL,
  `pot` int(11) NOT NULL,
  `pre` int(11) NOT NULL,
  `org` int(11) NOT NULL,
  `rekomendasi` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `formulir_rekapitulasi`
--

INSERT INTO `formulir_rekapitulasi` (`id`, `nim`, `nama`, `ipk`, `pot`, `pre`, `org`, `rekomendasi`) VALUES
(1, 'L200130099', 'Aji Ngambek', 3.25, 2000000, 3, 3, 3.133),
(2, 'L200130013', 'Yusuf Zainuddin', 3.33, 2000000, 3, 3, 2.8);

-- --------------------------------------------------------

--
-- Table structure for table `hasil`
--

CREATE TABLE `hasil` (
  `norules` int(11) NOT NULL,
  `min` float NOT NULL,
  `rekomendasi` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hasil`
--

INSERT INTO `hasil` (`norules`, `min`, `rekomendasi`) VALUES
(1, 3.17009, ''),
(2, 0.25, ''),
(3, 0.25, ''),
(4, 0.25, ''),
(5, 0.25, ''),
(6, 0.25, ''),
(7, 0.25, ''),
(8, 0, ''),
(9, 0, ''),
(10, 0, ''),
(11, 0, ''),
(12, 50.5, ''),
(13, 3.17009, ''),
(14, 3.17009, '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `biodata_mhs`
--
ALTER TABLE `biodata_mhs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `forminput_biodata`
--
ALTER TABLE `forminput_biodata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `formulir_biodata`
--
ALTER TABLE `formulir_biodata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `formulir_rekapitulasi`
--
ALTER TABLE `formulir_rekapitulasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hasil`
--
ALTER TABLE `hasil`
  ADD PRIMARY KEY (`norules`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `biodata_mhs`
--
ALTER TABLE `biodata_mhs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `forminput_biodata`
--
ALTER TABLE `forminput_biodata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `formulir_biodata`
--
ALTER TABLE `formulir_biodata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `formulir_rekapitulasi`
--
ALTER TABLE `formulir_rekapitulasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `hasil`
--
ALTER TABLE `hasil`
  MODIFY `norules` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
