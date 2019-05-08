import yaml
import datetime
import os

pl_yaml=open(r'/etc/ecs_planner/planner_cfg.yaml')
dict_yaml=yaml.load(pl_yaml)
#print(dict_yaml)
start_time=datetime.datetime.strptime(dict_yaml['Start_time'], "%H:%M")
stop_time=datetime.datetime.strptime(dict_yaml['Stop_time'], "%H:%M")
start_cron = str(start_time.minute) + ' ' + str(start_time.hour) + ' ' + '*' + ' ' + '*' + ' ' + dict_yaml['week_day'] + ' ' + '.' + ' ' + '/etc/ecs_planner/cloud_env;/usr/local/bin/nova start ' + dict_yaml['ECS_names'] + ' | /usr/bin/ts >> /var/log/ecs_planner.log'
stop_cron = str(stop_time.minute) + ' ' + str(stop_time.hour) + ' ' + '*' + ' ' + '*' + ' ' + dict_yaml['week_day'] + ' ' + '.' + ' ' + '/etc/ecs_planner/cloud_env;/usr/local/bin/nova stop ' + dict_yaml['ECS_names'] + ' | /usr/bin/ts >> /var/log/ecs_planner.log'
print(start_cron)
print(stop_cron)
cron_f=open('/etc/ecs_planner/planner_cron','w')
cron_f.write(start_cron + '\n')
cron_f.write(stop_cron + '\n')
cron_f.close()
if os.system('crontab /etc/ecs_planner/planner_cron') == 0:
    print('success')
else:
    print('failed')

