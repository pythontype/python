#coding:utf-8
#################
# 习题6:字符串和文本
#################
# 前言
#
# 输出文本的时候，最好用到用变量去代替，这样会省下很多工作
#

x = "There are %d typs of people." % 10
binary  = "binary"
do_not = "dot't"
y = "Those who know %s and those who %s" % ( binary,do_not)

print (x) 
print (y)

print ("I said: %r" % x)
print ("I also said: '%s'." % y)

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of....."
e = "a string with a right side."

print (w + e)

# 笔记
#
# %r和%s的区别
# %r会显示原始数据，用来调试
# %s会直接替换
