
import requests
from PIL import Image
from io import BytesIO
import  pandas  as pd
import os 

#方法一：默认读取第一个表单
df=pd.read_excel('excel_output.xlsx',names=["homeworkId","image","lessonId","lesson_title","mode1","stepId"])#这个会直接默认读取到这个Excel的第一个表单
data=df.mode1#默认读取前5行 的数据
for index in range(len(data)):
    background_url = df.image[index]
    background_url_mode = data[index]
    print(index)
    if str(background_url)!='nan' and (background_url_mode =='CMYK' or background_url_mode =='P'):
        lessonId = df.lessonId[index]
        dialogId = df.homeworkId[index]
        response = requests.get(background_url)
        response = response.content
        BytesIOObj = BytesIO()
        BytesIOObj.write(response)
        img = Image.open(BytesIOObj)
        image = img.convert('RGB')
        image.save('images/'+str(int(lessonId))+'_'+str(dialogId)+'.jpg')
        del BytesIOObj
        del img
        del response



