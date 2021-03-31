#导入必要的模块  
import numpy as np  
import matplotlib.pyplot as plt
import re 

file = open("C://Users//WANGFEN//Desktop//idkp1-10.txt","r")
list = file.readlines()#每一行数据写入到list中
print(list)
lists = []
#将txt文件转换成数组形式保存
for fields in list:
    fields=fields.strip();#fields.strip()用来删除字符串两端的空白字符。
    fields=fields.strip("\n");    # fields.strip("[]")用来删除字符串两端方括号。
    fields=fields.split(","); # fields.split(",")的作用是以逗号为分隔符，将字符串进行分隔。
    print(fields)
    lists.append(fields)

tracks = np.array(lists)
boxes = tracks[:,2:6]#读入边界框坐标
print(boxes)

#产生测试数据  
x = list        
y = x  
fig = plt.figure()  
ax1 = fig.add_subplot(111)  
#设置标题  
ax1.set_title('Scatter Plot')  
#设置X轴标签  
plt.xlabel('X')  
#设置Y轴标签  
plt.ylabel('Y')  
#画散点图  
ax1.scatter(x,y,c = 'r',marker = 'o')  
#设置图标  
plt.legend('x1')  
#显示所画的图  
plt.show() 

