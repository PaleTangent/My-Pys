import re
from dateutil import parser

pattern = re.compile(r'^\d{4}-[0|1][0-9]-[0123][0-9]$')
while True:
    try:
        c = input('请输入一个日期（格式yyyy-mm-dd）或按q退出程序:')
        if c == 'q':
            print('用户已结束程序.')
            break
        elif pattern.search(c):
            d = parser.parse(c)
            x = d.strftime('%j')
            y = str(x)
            print(d, '是一年中的第', y, '天.')
        else:
            print('错误！输入内容非有效日期，请尝试重新输入.')
    except parser.ParserError:
        print('错误！日期超出当月最大值，请尝试重新输入.')
    except KeyboardInterrupt:
        print('\n用户已通过快捷键结束程序.')
        break
    except Exception as e:
        print('未知错误', e)
