#java :中变量使用final声明的变量为常量
# python 中的常量命名规范
# python 命名常量的时候，名字是大写。
# 没有强制规则。注意：可以随时改变常量的值
NAME = '小红'
print(NAME)

# ''' ''' 三单引号：1、保留格式字符串使用。 2、多行注释

hello_python = '''
    你好：
        我是java学习者，我同时来学习python

       Java写；     python收；
'''
print(hello_python)
person = '大圣'
address = '北京市海港区'
phone = '12345'
#这个是字符串拼接
print('订单的收件人是:' + person + ',收货地址:' + address + ',联系电话:' + phone)
#格式化输出
print('订单的收货人是:%s,收货人是:%s,练习电话是:%s' % (person, address, phone))
'''
    %
    %f(浮点型)  整数可以强制转换成浮点数
    %d(整型)    浮点数可以强制转换成整型  
    %s(字符串)  混合输出是使用，%s是输出字符串和变量的混合
'''
age = 1
b = 1.23
char = 'A'
print('age=%f,b=%s,a=%s' % (age,b,char))

# %d  ----->取整数
year = 2020.0 
print('今年是：%d'% year)

#%f  ------>输出整数后小数点的全部位数。
#%.2f ----->可以强制保留小数点后的位数：（.2）表示保留两位小数
#保留位数用四舍五入的方式保留
salary = 123.123
print('我的薪资：%f' % salary)
salary = 123.155
print('我的薪资：%.2f' % salary)
salary = 123.154
print('我的薪资：%.2f' % salary)

#格式化练习题（）
movie = '大偵探皮卡丘'
ticket = 59.2
count = 35
total = ticket * count 

message = '''
电影： %s
人数：%d
单价：%.1f
总价：%.1f
''' % (movie , count , ticket , total)
print(message)

#字符串的格式化输出
#方式：1、使用占位符
#     2、使用format（格式）
age = 2
mseeage = '乔治说：我今年{}岁了！'.format(age)
print(mseeage)