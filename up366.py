import re
import sys
import tkinter as tk
from tkinter import font

# 打开page1.js文件
# 若无法打开，返回错误并终止程序
try:
    with open('page1.js', 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("文件名错误或文件不存在")
    sys.exit(1)
except:
    print("未知错误")

# 使用正则表达式匹配"answer_text"和"knowledge"之间的部分
# 若文件内不存在该元素，警报并退出程序
try:
    pattern = r'"answer_text"(.*?)"knowledge"'
    matches = re.findall(pattern, content, re.DOTALL)
except NameError:
    print("未抓取到answer，请检查文件是否正确")
    sys.exit(1)

# 截取的部分存储在Answers列表中
Answers = []
for match in matches:
    Answers.append(match.strip())
    
# 处理Answers列表
Outs = []
for answer in Answers:
    # 提取最先出现的A、B、C、D中的一个
    option = re.search(r'[A-D]', answer).group()
    # 在同元素中找到完全相同的字母，并提取其后的内容
    pattern = r'"id":"{}"(.*?)"content":"(.*?)"'.format(option)
    match = re.search(pattern, answer)
    if match:
        Outs.append(match.group(2))

# 创建一个简单的GUI窗口
window = tk.Tk()
window.title("天学网分析")

# 使tk窗口置于屏幕顶部
window.attributes("-topmost", True)

# 定义一个函数来将内容显示在文本框中
def display_output(content):
    output_text.insert(tk.END, content + "\n")

# 创建一个宋体字体对象
custom_font = font.Font(family="宋体", size=12)

# 创建一个文本框用于显示输出内容
output_text = tk.Text(window)
output_text.pack()

# 设置文本框的字体
output_text.configure(font=custom_font)

for out in Outs:
    index = Outs.index(out) + 1
    show = str(index) + " " + out
    display_output(show)

# 运行主循环
window.mainloop()
