######################
#练习4：变量和命名
######################

#1、在每一行的上面写一条注释，给自己解释一下这一行的作用
#2、倒着读自己的代码
#3、朗读自己的代码，将每个字符都读出来

#创建一个变量“cars”,赋值100
cars = 100
#创建一个变量“space_in_a_car”，赋值 4.0
space_in_a_car = 4.0
#创建一个变量“drivers”,赋值30
drivers = 30
#创建一个变量“passengers”，赋值90
passengers = 90

#创建一个变量“cars_not_driver”，将变量 "cars"与"drivers"的差赋值给“cars_not_driver”
cars_not_driven = cars - drivers
#将“drivers”赋值给新变量“cars_drivers”
cars_driver = drivers
#将变量“cars_driven”与变量“space_in_a_car”的乘积赋值给新变量“carpool_capacity”
carpool_capacity = cars_driver * space_in_a_car
#将变量“passengers ”与变量“passengers ”的商赋值给新变量“average_passengers_per_car”
average_passengers_per_car = passengers / cars_driver

#输出“cars”的值
print ("there are ", cars,"cars available.")
#输出“drivers”的值
print ("there are only",drivers,"drivers available.")
#输出“cars_not_driven”的值
print ("there will be", cars_not_driven,"empty cars today.")
#输出“carpool_capacity”的值
print ("we can transport",carpool_capacity,"people today.")
#输出“passengers”的值
print("we have", passengers,"to carpool today.")
#输出“average_passengers_per_car”的值
print("we need to put about", average_passengers_per_car ,"in each car.")