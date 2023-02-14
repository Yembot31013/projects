import tkinter

tk = tkinter.Tk()
frame = tkinter.Frame(tk, borderwidth=2)
frame.pack(expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(expand=1)
button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack()
tk.mainloop()
