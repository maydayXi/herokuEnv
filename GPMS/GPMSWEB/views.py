from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json                                     # Json 套件
from GPMSWEB.main import main                   # 自建主程式類別
from GPMSWEB.DBService import DBService         # 自建資料庫類別
from GPMSWEB.TableService import TableService   # 自建資料表類別
from GPMSWEB.dataAnaly import dataAnaly         # 資料分析類別

# Create your views here.

# 初始所有類別物件   全域
db = DBService()                            # 資料庫物件
analy = dataAnaly()                         # 資料分析物件
table = TableService()                      # 表格資料物件
table_name_lst = table.getAllTableName()

# 找出有問題的站點
def Main(requests):
    x = main()
    x.getInitData()
    x.getAirValue()
    x.dbHandle()
    result = x.analy()

    return render(requests, "test2.html", {"result":result})

def index(requests):
    error = db.readErrorData('2017_10_31')

    return render(requests, "index.html", locals())

def data(requests):
    temp = db.readSiteData()        # 測站暫存空氣資料
    site_lst = []                   # 測站串列
    air_data_lst = []               # 空氣資料串列
    data = {}                       # 過去空氣資料字典

    analy.getAreaId(table_name_lst[-1][8:])             # 取得鄰近測站資料  ID
    area = analy.getAreaSite()                          # 取得鄰近站點資料名稱

    for item in temp:
        air_data = db.readAirDataByNote(table_name_lst[-1],item[3])
        if air_data != None:                                            # 如果沒有測站資料
            site_lst.append([item[0],item[3]])                          # (id,stNote)
            air_data_lst.append([air_data[1], air_data[2],              # (pm2.5, pm10,
                                air_data[3], air_data[4]])              # 溫度, 濕度)

    if(len(requests.GET) == 0):
        row = 0
    else:
        row = int(requests.GET['selectedIndex'])

    data[site_lst[row][1]] = {"12":[], "6":[], "1":[], "area":[]}

    data[site_lst[row][1]] = {"12":[],"6":[],"1":[],"area":[]}
    time_lst,pm25_lst = table.getXYAxis(table_name_lst,site_lst[row][0],interval=60)
    data[site_lst[row][1]]["12"] = pm25_lst
    time_lst,pm25_lst = table.getXYAxis(table_name_lst,site_lst[row][0],interval=30)
    data[site_lst[row][1]]["6"] = pm25_lst
    time_lst,pm25_lst = table.getXYAxis(table_name_lst,site_lst[row][0],interval=5)
    data[site_lst[row][1]]["1"] = pm25_lst
    data[site_lst[row][1]]["area"] = area[row]

            # if not item[3] in data:
            #     key = item[3]
            #     data[key] = {"12":[],"6":[],"1":[],"area":[]}
            # else:
            #     key = item[3] + '-1'
            #     data[key] = {"12":[],"6":[],"1":[],"area":[]}
            #
            #
            # for i in range(3):
            #     if i == 0:
            #         time_lst,pm25_lst = table.getXYAxis(
            #             table_name_lst,item[0],interval = 60)
            #         data[key]["12"] = pm25_lst
            #
            #     elif i == 1:
            #         time_lst,pm25_lst = table.getXYAxis(
            #             table_name_lst,item[0],interval = 30)
            #         data[key]["6"] = pm25_lst
            #
            #     elif i == 2:
            #         time_lst, pm25_lst = table.getXYAxis(
            #             table_name_lst,item[0],interval = 5)
            #         data[key]["1"] = pm25_lst
            #
            # data[key]["area"] = area[count]
            # count += 1

    # data = HttpResponse(json.dumps(data),content_type="application/json")

    return render(requests, "data.html", locals())

def wronglist(requests):
    error = db.readErrorData('2017_10_31')

    stLat = 24.1492789
    stLon = 120.68338

    if len(requests.GET) == 3:
        stLat = requests.GET['stLat']
        stLon = requests.GET['stLon']

    return render(requests, "wrongList.html", locals())
