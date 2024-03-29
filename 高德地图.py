import requests
import json
import openpyxl

# 1.通过读取Excel的列获取景区名称
wb = openpyxl.load_workbook('高德地图.xlsx')
sheet = wb['Sheet1']
# 获取第一列的数据
cols = sheet['A']
# 将第一列的数据存入列表
scenic_spot = []
for col in cols:
    scenic_spot.append(col.value)

# 2.通过高德地图API获取景区经纬度并把经纬度以Excel的形式存储
# 2.1 创建Excel文件
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '景区经纬度'
sheet['A1'] = '景区名称'
sheet['B1'] = '经度'
sheet['C1'] = '纬度'
# 2.2 通过高德地图API获取经纬度
for i in range(len(scenic_spot)):
    url = 'https://restapi.amap.com/v3/place/text?key={{添加你的token}}&keywords={}&types=&children=1&offset=1&page=1&extensions=all'.format(
        scenic_spot[i])
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    #如果没有获取到经纬度，就跳过
    if data['count'] == '0':
        continue
    # 获取经纬度
    location = data['pois'][0]['location']
    # print(location)
    # 将经纬度以Excel的形式存储
    sheet['A{}'.format(i + 2)] = scenic_spot[i]
    sheet['B{}'.format(i + 2)] = location.split(',')[0]
    sheet['C{}'.format(i + 2)] = location.split(',')[1]
    #清空data
    data = None
# 2.3 保存Excel文件
wb.save('景区经纬度.xlsx')

