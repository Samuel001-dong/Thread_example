""""
exercise for the operation of write/read file
图片读取需要使用'rb',读取二进制的格式
正常的文本可以使用'rt',即它的默认格式
"""
# f = open('data.txt')
# print(f.readable())
# print(f.readlines())
# f.close()
# 采用with语句块，在打开文件之后操作完毕会自动关闭，不必再用f.close()
# with open('data.txt') as f:
#     print(f.readlines())
# with语句块，可以将文件打开之后，操作完毕，自动关闭这个文件
with open('data.txt') as d:
    while True:
        line = d.readline()       # 读取一行内容
        if line:
            print(line)
        else:
            break
print(f'请输入一个值：')
i = input()
print(f'输入的值：{i}')
