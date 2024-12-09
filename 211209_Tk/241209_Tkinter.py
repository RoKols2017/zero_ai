import tkinter as tk

def input_name():
    name = entry.get()
    if name == "":
        name = "Медвед"

    label = tk.Label(root)
    label.pack()
    label.config(text=f"Привет {name}!")

root = tk.Tk()
root.geometry('400x200')

root.title("Простой проект по вводу и выводу текста")

label = tk.Label(root, text="Введите свое имя:")
label.pack()

button = tk.Button(root, text="Скорее нажми на кнопку", command=input_name)
button.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Для завершения нажми меня", command=root.destroy)
button.pack()

root.mainloop()