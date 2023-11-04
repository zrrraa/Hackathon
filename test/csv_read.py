import tkinter as tk
import csv

def load_data(file_path):
    data = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)  # 获取标题行
        for row in reader:
            title = row[0]  # 获取第一列标题
            values = [float(value) for value in row[1:]]  # 转换后面九列的数据为浮点数
            data[title] = values
    return data

def search_data(data, title):
    if title in data:
        return data[title]
    else:
        return None

def search_button_click():
    search_title = title_entry.get()
    result = search_data(data, search_title)
    if result:
        result_label.config(text='查询结果：{}'.format(result))
    else:
        result_label.config(text='未找到匹配的标题。')

file_path = '2/SNP_R605.csv'  # 替换成您的CSV文件的路径
data = load_data(file_path)

window = tk.Tk()
window.title('CSV查询')
window.geometry('400x200')

title_label = tk.Label(window, text='请输入要查询的标题：')
title_label.pack()

title_entry = tk.Entry(window)
title_entry.pack()

search_button = tk.Button(window, text='查询', command=search_button_click)
search_button.pack()

result_label = tk.Label(window, text='')
result_label.pack()

window.mainloop()