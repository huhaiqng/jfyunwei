--
-- Add field used to project
--
ALTER TABLE `project_project` ADD COLUMN `used` bool DEFAULT b'1' NOT NULL;
ALTER TABLE `project_project` ALTER COLUMN `used` DROP DEFAULT;


--
-- Create model ProjectModule
--
CREATE TABLE `project_projectmodule` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `module` varchar(255) NOT NULL, `pkg_name` varchar(255) NOT NULL, `pkg_type` varchar(255) NOT NULL, `port` integer NOT NULL, `deploy_dir` varcha
r(255) NOT NULL, `logfile` varchar(255) NOT NULL, `project_id` integer NOT NULL);
ALTER TABLE `project_projectmodule` ADD CONSTRAINT `project_projectmodule_project_id_module_0ad610a6_uniq` UNIQUE (`project_id`, `module`);
ALTER TABLE `project_projectmodule` ADD CONSTRAINT `project_projectmodule_project_id_38bd49b5_fk_project_project_id` FOREIGN KEY (`project_id`) REFERENCES `project_project` (`id`);


INSERT INTO `auth_permission`(`id`, `name`, `content_type_id`, `codename`) VALUES (201, 'Can add 项目模块', 48, 'add_projectmodule');
INSERT INTO `auth_permission`(`id`, `name`, `content_type_id`, `codename`) VALUES (202, 'Can change 项目模块', 48, 'change_projectmodule');
INSERT INTO `auth_permission`(`id`, `name`, `content_type_id`, `codename`) VALUES (203, 'Can delete 项目模块', 48, 'delete_projectmodule');
INSERT INTO `auth_permission`(`id`, `name`, `content_type_id`, `codename`) VALUES (204, 'Can view 项目模块', 48, 'view_projectmodule');

INSERT INTO `django_content_type`(`id`, `app_label`, `model`) VALUES (48, 'project', 'projectmodule');