while True:
    try:
        temp = input('BYTE YOUR TEMP(F OR C)')
        temp_type = temp[-1]
        temp_value = float(temp[0:-1])
        if temp_type in ['F', 'f']:
            temp_out = ((temp_value - 32) / 1.8)
            print(temp_out)
        elif temp_value in ['C', 'c']:
            pass
        elif temp_type == 'q':
            break
        else:
            print('error')
    except KeyboardInterrupt:
        print('\n用户已通过快捷键结束程序.')
        break
    except Exception as e:
        print('未知错误', e)
