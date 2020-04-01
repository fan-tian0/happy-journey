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

'''
    2、比较运算符：bi
        ==
        !=
        >=
        <=
        >
        <
        is
        is not

        返回True 或者 False

'''

n1 = (int(input('请输入第一个数：')))
n2 = (int(input('请输入第二个数：')))

result = n1 > n2
print('n1 > n2 ',result)

m1 = 'hello'
m2 = 'hello'
result = m1 == m2
print('m1 == m2',result)

#is 对象（变量）的地址进行比较 (判断两个数的内存是否一样) 
age = 10
age1 = 10
print(age is age1) #判断两个内存地址是否一样
print(id(age))  #打印两个变量的内存地址
print(id(age1))
#在终端中，有小整数池(定义：-5~256)这些数是提前建立好的不会被回收的。
#在大整数池中，没执行一次就创建一次。

'''
    3、逻辑运算符
        and 逻辑与  
        or  逻辑或
        not 逻辑非  
    
    逻辑运算符返回的结果是：Ture / False
'''
print(False and True)   #and 两边都是 true, 结果就是true
print(True and True)    #and 一边是False ，结果就是False
print(False and False)

print(False or True) # or 一边为True ，就是True
print(False or False)# or 两边是False，结果就是False
print(True or True)

print(not False) #not 取反 
print(not True)

'''
    4、位运算
        & 
        | 
        ! 
        ^
        ~
        <<
        >>

    位运算操作的是二进制    1： 是True      0： False
'''
print(1 & 2)
print(1 | 5)    #结论： 1 | 奇数 结果就是奇数本身
print(1 | 10)   #       1 | 偶数 结果就是偶数本身加1

print(1 ^ 3)
print(1 << 2)   #左移一位就是乘与一个2
print(1 >> 2)   #右移一位就是除以一个2
print(bin(~2))
a = 15
print(bin(a)) #bin() 输出二进制数
a = 0b1111 #0b 开头是二进制
print(int(a)) # 转换成是十进制输出

a = -5
print(bin(a)) #负数

a = 0o6351  #0o开头是八进制
print(bin(a))
print(a)

a = 0xfae #0x开头的是十六进制
print(a)
print(bin(a))

'''
    5、三目运算符：
        结果 if 表达式 else 结果

    1、中间为条件判断表达式
    2、结果是真True 就返回左边的结果
    3、结果是False 就返回右边的结果
'''

a = 12
b = 10
result = (( a + b ) if (a > b) else (a - b))
print(result)
print(True)