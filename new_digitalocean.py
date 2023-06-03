import requests
import json
import random
import time
from digitalocean import Droplet
token = "aaaaa"#输入token
dataset=['nyc1','nyc3','ams3','sfo3','sgp1','lon1','fra1','tor1','blr1','syd1']

#创建服务器（大约需要四~五分钟）
def createserver():
    droplet = Droplet(token=token,
                      name='xxx',
                      region=dataset[random.randint(0, 9)],
                      image='ubuntu-20-04-x64',
                      size_slug='s-1vcpu-1gb',
                      backups=False)
    droplet.create()
    print(f"成功创建服务器：{droplet.name},它的id为：{droplet.id},它的地区为：{dataset[random.randint(0, 9)]}")
    time.sleep(55)
    droplet.load()
    ip = droplet.ip_address
    if ip == None:
        time.sleep(10)
        droplet.load()
        ip = droplet.ip_address
    # print(ip)
    return ip, droplet.id

def breakserver(SUBID):
    droplet = Droplet(token=token, id=SUBID)
    droplet.destroy()
    print(f"已成功删除 ID: {SUBID}")


for i in range(0,15):
    try:
        ip1, SUBID1 = createserver()  # 创建服务器并返回ip和SUBID
    except:
        print("创建失败，跳过！")
        continue

    while True:
        try:
            breakserver(SUBID1)
        except:
            print("等待20s再试一次")
            time.sleep(20)