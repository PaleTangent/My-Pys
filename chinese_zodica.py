# 生肖，根据年份判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
a = input("请输入出生年份 The year that you was born:")
b = chinese_zodiac[int(a) % 12]
print(b)
