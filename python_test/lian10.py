#coding:utf-8
#################
# 习题10:那是什么
#################
# 前言
#
# 这里主要理解：转义字符的作用
#

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# \t：水平制表符
# \n：换行
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print( tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

# 试试运行下面的代码
#while True:
#    for i in ["/","-","|","\\","|"]:
#	print "%s\r" % i,