
import requests
from PIL import Image
from io import BytesIO
import  pandas  as pd
import os 

#方法一：默认读取第一个表单
df=pd.read_excel('check.xlsx',names=["homeworkId","image","lessonId","lesson_title","mode1","stepId"])#这个会直接默认读取到这个Excel的第一个表单
data=df.image#默认读取前5行 的数据
for index in range(len(data)):
    image = data[index]
    mode = df.mode1[index]
    if str(mode) != 'nan' or mode =='':
        continue
    print(index)
    # if str(background_url)!='nan':
    #     response = requests.get(background_url)
    #     response = response.content
    #     BytesIOObj = BytesIO()
    #     BytesIOObj.write(response)
    #     img = Image.open(BytesIOObj)
    #     df.loc[index,'background_mode'] = img.mode
    #     del BytesIOObj
    #     del img
    #     del response
    if str(image) != 'nan':
        try:
            response = requests.get(image)
            response = response.content
            BytesIOObj = BytesIO()
            BytesIOObj.write(response)
            img = Image.open(BytesIOObj)
            df.loc[index,'mode'] = img.mode
            del img
            del BytesIOObj
            del response
        except IOError:
            print('error image')
df.to_excel('excel_output.xlsx',sheet_name='biubiu')


