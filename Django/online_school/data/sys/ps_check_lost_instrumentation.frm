TYPE=VIEW
query=select `information_schema`.`global_status`.`VARIABLE_NAME` AS `variable_name`,`information_schema`.`global_status`.`VARIABLE_VALUE` AS `variable_value` from `information_schema`.`global_status` where ((`information_schema`.`global_status`.`VARIABLE_NAME` like \'perf%lost\') and (`information_schema`.`global_status`.`VARIABLE_VALUE` > 0))
md5=7c242cd85620e15d0610d24ace9167ab
updatable=0
algorithm=2
definer_user=root
definer_host=localhost
suid=0
with_check_option=0
timestamp=2022-11-18 11:36:40
create-version=1
source=SELECT variable_name, variable_value FROM information_schema.global_status WHERE variable_name LIKE \'perf%lost\' AND variable_value > 0
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select `information_schema`.`global_status`.`VARIABLE_NAME` AS `variable_name`,`information_schema`.`global_status`.`VARIABLE_VALUE` AS `variable_value` from `information_schema`.`global_status` where ((`information_schema`.`global_status`.`VARIABLE_NAME` like \'perf%lost\') and (`information_schema`.`global_status`.`VARIABLE_VALUE` > 0))