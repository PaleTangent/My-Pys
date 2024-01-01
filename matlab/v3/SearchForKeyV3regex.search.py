"""
配合./pickle_os/sis-sen.dll使用

"""
import pickle
import re
from colorama import init  # 显示颜色控件模块


init(autoreset=True)


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = ".*?".join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in suggestions]


def search_str(search_key, tick1):  # 解决输入关键字中带有　* -　程序退出问题
    return_result = []
    for text in tick1:
        if search_key in text:
            return_result.append(text)

    return return_result


try:

    pickle_file = open("sis-sen.dll", "rb")
except FileNotFoundError as e:
    print("没有找到数据库,请检查数据是否存在！", "[#错误代码", e, "]")
    exit()
my_wen = pickle.load(pickle_file)

pickle_file.close()

tick = my_wen.split("-" * 75)
select_result = []
# print(type(tick))
while True:
    try:
        print("+", "=" * 74, "+")
        print("|", " " * 74, "|")
        print(f"|", ' ' * 31, "\033[1;31;40m关键字查询\033[0m", " " * 32, "|")
        print("|", " " * 74, "|")
        print("+", "=" * 74, "+")
        print(f'\033[1;32;40m改进版，可以查询公式如：y=2*x-3\n\033[0m')
        print(f'\033[1;31;40m请输入要查询的关键字，输入“q”退出：\033[0m', end="")
        select_text = input()
        if select_text in ["q", "Q"]:
            break
        elif select_text == "":
            print("重新查询")
            continue

        reg_flag = True
        for str_search in select_text:
            if str_search in ["*", "+", ".", "?"]:
                reg_flag = False
                select_result = search_str(select_text, tick)

        if reg_flag:
            select_result = fuzzyfinder(select_text, tick)

        line_count = 0
        # a 为引入的辅助变量,用以解决line69过长的问题
        a = '\n与　"\033[1;36;40m{}\033[0m" 相关的信息，共找到　\033[1;35m{} \033[0m个结果。'
        if len(select_result) != 0:
            print(a.format(select_text,
                           len(select_result)))
            i = 1
            for out_text in select_result:

                if line_count < 8:
                    line_count += 1
                    print(out_text)
                    print("{:-^120}".format(
                        "\033[0;32;40m'\033[1;32;40m" + select_text + "\033[0;32;40m' 共找到\033[1;32;40m" + str(
                            len(select_result)) + "\033[0;32;40m个结果，这是第\033[1;32;40m" + str(i) + "个\033[0m"))
                    i += 1
                else:
                    line_count = 1
                    print(f'\033[1;32;40m后面还有，请按回车键继续！\033[0m', end="")
                    a = input()
                    print(out_text)
                    print("{:-^120}".format(
                        "\033[0;32;40m'\033[1;32;40m" + select_text + "\033[0;32;40m' 共找到\033[1;32;40m" + str(
                            len(select_result)) + "\033[0;32;40m个结果，这是第\033[1;32;40m" + str(i) + "个\033[0m"))
                    i += 1
        else:
            print('\n\033[1;36;40m没找到“{}”的信息，请重新输入！\033[0m\n'.format(select_text))
        select_result.clear()
    except KeyboardInterrupt:
        print('\n用户已通过快捷键结束程序.')
        break
