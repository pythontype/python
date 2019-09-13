################################
# 练习5：更多的变量和打印
################################
#
# f是“格式化”（format）的意思
# 格式为 f、引号、{}，例如f“Hello {somevar}”
#
# 格式化字符串主要作用是：
#
# %d 输出数字
# %s 输出字符串

my_name = "XiaoMing"
my_age =10
my_height = 170 
my_weight = 60
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

print(f" let't talk about { my_name }.")
print(f" He's { my_height } inches tall.")
print(f" He's { my_weight } pounds heavy.")
print(" Actually that's not too heavy.")
print(f" He's got { my_eyes } eyes and { my_hair} hair. ")
print(f" His teeth are ususlly { my_teeth } depending on the coffee.")


#this line is tricky,try to get it exactly right
total = my_age + my_height + my_weight
print (f" If i add { my_age } , { my_weight } i get { total }.")