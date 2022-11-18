TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER sys_config_insert_set_user BEFORE INSERT on sys_config FOR EACH ROW BEGIN IF NEW.set_by IS NULL THEN SET NEW.set_by = USER(); END IF; END' 'CREATE DEFINER=`root`@`localhost` TRIGGER sys_config_update_set_user BEFORE UPDATE on sys_config FOR EACH ROW BEGIN IF NEW.set_by IS NULL THEN SET NEW.set_by = USER(); END IF; END'
sql_modes=0 0
definers='root@localhost' 'root@localhost'
client_cs_names='utf8' 'utf8'
connection_cl_names='utf8_general_ci' 'utf8_general_ci'
db_cl_names='utf8_general_ci' 'utf8_general_ci'
created=166877140065 166877140067
