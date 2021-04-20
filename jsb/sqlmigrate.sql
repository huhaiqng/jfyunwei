--
ALTER TABLE `project_host` ADD COLUMN `password` varchar(200) DEFAULT '123456' NOT NULL;
ALTER TABLE `project_host` ALTER COLUMN `password` DROP DEFAULT;
--
-- Add field user to host
--
ALTER TABLE `project_host` ADD COLUMN `user` varchar(200) DEFAULT 'root' NOT NULL;
ALTER TABLE `project_host` ALTER COLUMN `user` DROP DEFAULT;


ALTER TABLE `project_host` ADD CONSTRAINT `project_host_inside_ip_cloud_user_a170097e_uniq` UNIQUE (`inside_ip`, `cloud_user`);
