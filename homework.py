
import requests
from PIL import Image
from io import BytesIO
import  pandas  as pd
import os 
import re
# #方法一：默认读取第一个表单
df=pd.read_excel('homework.xlsx',names=["lessonId","lesson_title","stepId","homeworkId","content","images"])#这个会直接默认读取到这个Excel的第一个表单
data=df.content#默认读取前5行 的数据
i = 0
pattern = re.compile('https?:\/\/(?:(?:[a-zA-Z0-9_-])+(?:\.)?)*(?::\d+)?(?:\/(?:(?:\.)?(?:\?)?=?&?[a-zA-Z0-9_-](?:\?)?)*)*\.jpg',re.S)
for index in range(len(data)):
    contentjson = df.content[index]
    m = re.findall(pattern,contentjson)
    i+=len(m)
    print(index)
    df.loc[index,'images'] = str(m)

print(i)
df.to_excel('homework_output.xlsx',sheet_name='biubiu')


