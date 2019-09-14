#coding:utf-8
#################
# 习题7:更多打印
#################
# 前言
#
# 巩固练习输出
#

print ("Mary had a little lamb")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
# “.”输出了十次
print ("*" * 10 )

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma(逗号) at the end. try removing it to see what happens
# 在下面一行加逗号输出结果：在一行，中间用一个空格隔开
# 不加逗号的结果：分别输出在两行
print ("end1 + end2 + end3 + end4 + end5 + end6,\n")
print ("end7 + end8 + end9 +\nend10 + end11 + end12")


# 运行报了两次错误
# 1、
#  print ("Its fleece was white as %s.") % 'snow'
# TypeError: unsupported operand type(s) for %: 'NoneType' and 'str'  # %不支持的操作数类型:'NoneType'和'str'
#
# 把需要替换的字符串放入括号中
#  print ("Its fleece was white as %s." % 'snow'）
##############################################################################################################
#2、
#   print (end1 + end2 + end3 + end4 + end5 + end6,)\n
#                                                    ^
#SyntaxError: unexpected character after line continuation character  # 行连续字符之后的意外字符
#
#需要把字符放入括号中，并且需要双引号引起来
#print ("end1 + end2 + end3 + end4 + end5 + end6,\n")
