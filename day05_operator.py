'''
    operator:(运算符)
        运算符的分类：
            赋值运算符
            算数运算符
            关系运算符
            逻辑运算符
            位运算符
'''
'''
    1、赋值运算符：
        = , += , -= , *= , /= , %= , **=, //=
'''
name = '张三'
# id():为查看 变量的内存地址。
print(id(name), name)
name = 123
print(id(name), name)
name1 = name
print(id(name1), name1)
name2 = name1
print(id(name2), name2)
print(name1 == name)
print(name2 == name)
name3 = 123
print(id(name3), name3)
print(name == name3)
name1 = 'name'
print(id(name1), name1)
print(name1 == name)
a = 5
a += 1
print(a)
b = 'py'
b += 'thon'#字符串链接符
print(b)

print('*' * 1)# 输出50个*号 *(*在字符串后出现，并且有常量， 常量的值就是输出多少字符串)

c = 2
c **= 10# ** 计算次幂
print(c)

d = 11.1
d //= 10 # // 除数取整，舍去小数保留整数
print(d)

a = -123
a %= 10
print(a)
print('123')