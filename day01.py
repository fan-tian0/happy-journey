'''
#type函数显示数据的类型

   标识符规范：
        由 数字 _ 组成，不能是数字开头
        严格区分大小写
        不能是python关键字

    标识符的命名规则:
        驼峰式：    getName payMoney
            如果一个名字是由多个单词组成的，则除第一个
            单词之外以后的没一个单词的首字母大写
        建议：类名：GetName 如果定义类名，每个单词的首字母大写

        下划线式：
            Python 中的变量，函数命名：
                get_name(python推荐)
                pay_money(python推荐)
'''

'''
    python 查看关键字：
        1、导包：import keyword
        2、print（keyword.kwlist）
'''

import keyword
a = 12
A = 89
print(a, type(a))
print(A, type(A))
print('a',type('a'))
print("a",type("a"))

print(keyword.kwlist)
