-- 20210323
ALTER TABLE `project_host` ADD COLUMN `hostname` varchar(200) DEFAULT '' NOT NULL;
ALTER TABLE `project_host` ALTER COLUMN `hostname` DROP DEFAULT;

# 未执行
-- 20210415
ALTER TABLE `auth_permission_userinfo` DROP COLUMN `department_id`;
ALTER TABLE `auth_permission_userinfo` DROP COLUMN `position_id`;
