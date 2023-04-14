import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("计划表软件")

# 添加待办事项列表
tasks = []

# 创建待办事项标签和输入框
tk.Label(root, text="待办事项").grid(row=0, column=0)
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=1)

# 创建添加按钮
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
add_button = tk.Button(root, text="添加", command=add_task)
add_button.grid(row=0, column=2)

# 创建任务列表框
task_listbox = tk.Listbox(root, height=15, width=50)
task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# 创建删除按钮
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
        tasks.pop(selected_task[0])
delete_button = tk.Button(root, text="删除", command=delete_task)
delete_button.grid(row=2, column=1)

# 启动主循环
root.mainloop()
