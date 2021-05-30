import tkinter as tk
e1 = 0
def show_entry_fields():
    print(e1.get())
    e1.get() + 1
    print(e1.get())

master = tk.Tk()
tk.Label(master, 
         text="Prime Number").grid(row=0)


e1 = tk.Entry(master)
e1.grid(row=0, column=1)
print(e1)


tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
