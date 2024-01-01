import pickle
import re


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = ".*?".join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]


pickle_file = open("sis-sen.dll", "rb")
my_wen = pickle.load(pickle_file)

pickle_file.close()

tick = my_wen.split("-" * 75)
select_result = []
# print(type(tick))
while True:
    print("+", "=" * 74, "+")
    print("|", " " * 74, "|")
    print("|", ' ' * 31, "关键字查询", " " * 31, "|")
    print("|", " " * 74, "|")
    print("+", "=" * 74, "+")
    select_text = input("请输入要查询的文本，输入“q”退出：")
    if select_text in ["q", "Q", ""]:
        break
    select_result = fuzzyfinder(select_text, tick)
    line_count = 0
    if len(select_result) != 0:
        print(len(select_result))
        for out_text in select_result:
            if line_count < 10:
                line_count += 1
                print(out_text)
                print("-" * 75)
            else:
                line_count = 0
                a = input("按回车键继续！")
    else:
        print("输入的查询关键字有误，请重新输入！")
    select_result.clear()
