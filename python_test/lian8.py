#coding:utf-8
#################
# 习题8:打印，打印
#################
# 前言
#
# 巩固练习打印
#

formatter = "%r %r %r %r"

print (formatter % (1,2,3,4))
print (formatter % ("one","two","three","four"))
print (formatter % (True,False,False,True))
print (formatter % (formatter,formatter,formatter,formatter))
print (formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))
# 笔记
# 可以用数字、布尔值、变量、字符串替换
# 1.%r的原理是：代表的字符串中有“‘”，就自动加““”
# 2.这一章我学到：可以一个全是格式化字符串的字符串，来规范输出格式，
# 3.如果输出的是中文请用%s,不要用%r,请把下面的代码输出
print (formatter % ("我","是","小","寒"))
# 我输入的时候未做修改，可以直接运行，并且中文打印正常
# 但是还是需要注意和小心
