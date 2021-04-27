-- 20210427
DROP TABLE `report_daily` CASCADE;

CREATE TABLE `project_account` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `use` varchar(255) NOT NULL UNIQUE, `username` varchar(200) NOT NULL, `password` varchar(200) NOT NULL, `addr` varchar(200) NULL, `remark` varchar(255) NOT NULL, `created` datetime(6) NOT NULL);

ALTER TABLE `project_account` CHANGE `use` `name` varchar(255) NOT NULL;
