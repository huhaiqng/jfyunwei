INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (1, '我的日报', 'index', '/daily/index', 10, 1, 18, 1);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (2, '查看日报', 'report', '/daily/report', 11, 0, NULL, 1);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (3, '用户', 'user', '/auth-permission/user', 10, 1, NULL, 2);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (4, '组', 'group', '/auth-permission/group', 10, 1, NULL, 2);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (5, 'Gitlab 项目', 'group', '/gitlab/group', 10, 1, NULL, 3);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (6, 'Gainhon666', 'gainhon666', '/domain/gainhon666', 10, 1, NULL, 4);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (7, 'lingfannao', 'lingfannao', '/domain/lingfannao', 10, 1, NULL, 4);
INSERT INTO `auth_permission_l2menu`(`id`, `title`, `path`, `component`, `order`, `is_model`, `name_id`, `parent_id`) VALUES (8, '定时任务', 'taskresult', '/project/taskresult', 10, 0, NULL, 5);
