#print()的用法
#1、用法
print('hello world')
name = '小小'
print(name)

#2、用法：print(name,age,gender)
age = 18
gender = 'boy'
#3、用法print(value,value,value，...sep = ' ' ,end = '\n')
print(name,age,gender) #sep(separation:分割)默认的分割是空格
print(name,age,gender,sep='_')#sep='&' sep = '%'
#print()后面默认跟两个sep（分割）空格，end（换行）\n
#转义字符：\n 换行
print('hello \n world')#每个print后面跟一个end='\n'
print('AAA',end = ' ')
print('BBB',end = ' ')
print('CCC',end = ' ')

#练习： 亲爱的xxx：
    #   请点击练级激活用户：激活用户
print()
print('亲爱的xxx \n\t请点击链接激活用户：\n\t\t激活用户')

#pyton中 "''"   '""' 允许双引号嵌套单引号，也允许单引号嵌套双引号
print("乔治说：'他想看小金鱼'")
print('乔治说： "他想睡觉"')
#\r：覆盖\r前内容输出\r后面的内容
print('\r hello\rworld')
# r 后面跟字符串,r后面的字符串中即使有转移字符也不会输出，但sep，end除外
print(r'hello\py\tworld',r'123\r345')#r'':rew 原样输出字符的内容，即使由转移字符也不会发生转义
print(age)
#help查看print的用法
help(print)
'''
    单词：
help        帮助
Function    函数
Built-in(builtins) 内置
Module      模块
Value       置
Stream      流
denault     默认的
format      格式化
digit       数字    %d
Required    需要，必须
Raise       抛出，  

'''