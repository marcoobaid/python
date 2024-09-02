import tkinter as tk

main = tk.Tk()

main.geometry('500x500')
main.title('My First GUI')

label = tk.Label(main, text='Hello World!', font=('Arial', 18))
label.pack(padx=20, pady=20)

button = tk.Button(main, text='Press to Like!' , font=('Arial', 18))
button.pack()

main.mainloop()
