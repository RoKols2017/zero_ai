import tkinter as tk

def input_name():
    name = entry.get()
    if name == "":
        name = "Медвед"

    label = tk.Label(root)
    label.grid(row=1, column=1)
    label.config(text="")
    label.config(text=f"Привет {name}!")

root = tk.Tk()
root.geometry('400x200')

root.title("Простой проект по вводу и выводу текста")

label = tk.Label(root, text="Введите свое имя:")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

button = tk.Button(root, text="Скорее нажми на кнопку", command = input_name)
button.grid(row=1, column=0)

button = tk.Button(root, text="Нажми для завершения", command=root.destroy)
button.grid(row=2, column=0)

root.mainloop()