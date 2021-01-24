# 递归打印解析节点及路径
import os
import  pandas  as pd
def recursion(node_dict):
    if len(node_dict) == 0:
        print(node_dict)
    else:
        for i in node_dict:
            recursion(i.get('subNodes'))


df=pd.read_json('json.json')#这个会直接默认读取到这个Excel的第一个表单
print(df)
recursion(df)