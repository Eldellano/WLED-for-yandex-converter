#!/usr/bin/python3
import requests
import json
import cgi, cgitb


#cgitb.enable()
def brig_stat(ip_lamp):
    #url = 'http://192.168.0.20/json/state'
    url = 'http://192.168.0.' + ip_lamp + '/json/state'
    req = requests.get(url)
    dict = json.loads(req.text) #dict = req.json()
    dict_new = {}
    for key, value in dict.items():
        if key == 'bri':
            dict_new['value'] = round(value / 2.55)
            print()
            print(json.dumps(dict_new))
            break

def on_off_stat(ip_lamp):
    url = 'http://192.168.0.' + ip_lamp + '/json/state'
    req = requests.get(url)
    dict = json.loads(req.text) #dict = req.json()
    dict_new = {}
    for key, value in dict.items():
        if key == 'on':
            if value == True:
                dict_new['value'] = round(dict['bri'] / 2.55)
                print()
                print(json.dumps(dict_new))
                break
            elif value == False:
                dict_new['value'] = '0'
                print()
                print(json.dumps(dict_new))
                break

def brig_set(ip_lamp,val):
    dict_new = {}
    dict_new['value'] = val  #кладем установленную яркость в словарь для возврата статуса
    val = round(float(val) * 2.55)
    url = 'http://192.168.0.' + ip_lamp + '/win&A=' + str(val)
    req = requests.get(url)
    print()
    print(json.dumps(dict_new))

def route_def():  #читаем параметры запроса, направляем в нужную функцию
    form = cgi.FieldStorage()
    ip = form.getvalue('ip')  #получение ip нужного устройства из переданных параметров
    command = form.getvalue('command')
    val = form.getvalue('val')
    if command == 'brig_stat':
        #brig_stat(ip)
        on_off_stat(ip)
    elif command == 'on_off_stat':
        on_off_stat(ip)
    elif command == 'brig_set':
        brig_set(ip, val)

#on_off_stat()
#brig_stat()
route_def()
