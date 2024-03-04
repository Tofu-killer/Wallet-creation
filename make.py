#!/usr/bin/python3
import os,time


avail_secret = {
    "bian hao": "si yao"
}


for key in avail_secret.keys():
    #创建目录，copy文件
    os.system("mkdir /tank1/avail-{0}".format(key))
    os.system("cp /tank1/avail-3/avail-3 /tank1/avail-{0}/avail-{0}".format(key))
    os.system("cp /tank1/avail-3/config.yaml /tank1/avail-{0}/".format(key))
    os.system("cp /tank1/avail-3/identity.toml /tank1/avail-{0}/".format(key))

    #修改配置文件
    os.system("sed -i 's/avail_secret_seed_phrase.*$/avail_secret_seed_phrase = \"{0}\"/g' /tank1/avail-{1}/identity.toml ".format(avail_secret.get(key),key))
    os.system("sed -i 's/http_server_port.*$/http_server_port = {0}/g' /tank1/avail-{1}/config.yaml ".format(int(key) + 7000,key))
    os.system("sed -i 's/port.*$/port = {0}/g' /tank1/avail-{1}/config.yaml ".format(int(key) + 37000,key))
    os.system("sed -i 's/full_node_ws.*$/full_node_ws = [\"ws:\/\/127.0.0.1:{0}\"]/g' /tank1/avail-{1}/config.yaml ".format(int(key) + 10000, key))
    os.system("sed -i 's/app_id.*$/app_id = {0}/g' /tank1/avail-{0}/config.yaml ".format(key))

    #启动程序
    os.system("cd /tank1/avail-{0}/ ; nohup /tank1/avail-{0}/avail-{0} --network goldberg --port {1} --config /tank1/avail-{0}/config.yaml &".format(key,int(key) + 20000))

    #打印序号
    print("编号：{0}已经启动~~".format(key))
    time.sleep(1)