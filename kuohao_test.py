# coding=utf-8
'''
作者：林海峰
日期：2024年03月06日20:15
'''

str1 = input()
#用字典接收输入，以确定是哪一个左括号没有被右括号匹配
dict = {}

#将输入作为字典的值，t作为字典的键，来标记输入的每一个字符的位置
t = 0
for i in str1:
    dict[t] = i
    t += 1

#用栈来装入左括号
stack = []

#用来存储输入字符对应是？还是x，或者是空白
str2 = []
n = 0
for k, v in dict.items():
    #默认该输入字符对应符号为空白
    str2.append(' ')
    #如果该输入字符为左括号，则装入栈
    if v == '(':
        stack.append(k)
    elif v == ')':
    #如果该输入字符为右括号，判断栈中是否有左括号，如果没有，该字符对应符号为问号
        if(len(stack) == 0):
            str2[n] = '?'
        else:
            #如果栈中有左括号，则弹出
            stack.pop()
    n += 1

#找出栈中留下的左括号是哪一个输入字符的，并把该输入字符下面对应为×
for i in stack:
    str2[i] = 'x'
print(str1)
print("".join(str2))


