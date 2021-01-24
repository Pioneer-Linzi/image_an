
import requests
from PIL import Image
from io import BytesIO
import  pandas  as pd
import os 
import json



#方法一：默认读取第一个表单
df=pd.read_excel('homework_cmyk.xlsx',names=["lessonId","lesson_title","stepId","homeworkId","content","images","mode"])#这个会直接默认读取到这个Excel的第一个表单
data=df.images#默认读取前5行 的数据
new_df = pd.DataFrame()

for index in range(len(data)):
    images = data[index]
    lessonId = df.lessonId[index]
    lesson_title = df.lesson_title[index]
    stepId = df.stepId[index]
    homeworkId = df.homeworkId[index]
    images = images.replace('[','')
    images = images.replace(']','')
    images = images.split(',')
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
    if str(images) != 'nan' and images !='':
        for item in images:
            item = item.replace("\'",'')
            print(item)
            if item!='':
                new_df = new_df.append({"lessonId": lessonId,"lesson_title": lesson_title,"stepId": stepId,"homeworkId": homeworkId,"image": item,"mode":''},ignore_index=True)

print(new_df)
new_df.to_excel('mode_output.xlsx',sheet_name='biubiu')


