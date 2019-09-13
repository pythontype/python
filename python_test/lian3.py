# coding:utf-8
################
#练习3:数字与数学计算
################

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成
# 5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高
# 于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：条件语句的运用，if else


bonus1 = 100000*0.1
bonus2 = bonus1 + 100000 * 0.075
bonus3 = bonus2 + 200000 * 0.05
bonus4 = bonus3 + 200000 * 0.03
bonus5 = bonus4 + 400000 * 0.015

mon = int(input (" 请输入月利润：\n "))
if mon >= 1000000:
    bonus = (mon - 1000000) * 0.01 + bonus5
else:
    if mon >= 600000:
        bonus = (mon - 600000) * 0.015 + bonus4
    else:
        if mon >= 400000:
            bonus = (mon - 400000) * 0.03 + bonus3
        else:
            if mon >= 200000:
                bonus = (mon - 200000) * 0.05 + bonus2
            else:
                if mon >= 100000:
                    bonus = (mon - 100000) * 0.075 + bonus1
                else:
                    if mon  < 100000:
                        bonus = mon * 0.1
print( bonus)


#input获取的数据是字符串，无法直接进行比较比较，需要先将字符串转换为整数
