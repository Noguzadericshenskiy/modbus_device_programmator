import tkinter as tk


class EntryForm(tk.Toplevel):

    def __init__(self, master, sum_var):
        super().__init__(master)
        tk.Label(self, text="level one").pack()
        self.sum_var = sum_var
        self.entry_1 = tk.Entry(self)
        self.entry_1.pack()
        self.entry_2 = tk.Entry(self)
        self.entry_2.pack()
        tk.Button(self, text="submit", command=self.submitBtn).pack()

    def submitBtn(self):
        val_1 = self.entry_1.get()
        val_2 = self.entry_2.get()
        self.sum_var.set(int(val_1) + int(val_2))


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.sum_var = tk.IntVar()
        tk.Label(self, text = "Main window").pack()
        tk.Button(self, text= "To enter Data", command=self.spawn_entry_popup).pack()
        sum_label = tk.Label(self, textvariable=self.sum_var)
        sum_label.pack()

    def spawn_entry_popup(self):
        EntryForm(self, self.sum_var)
        print("jr", self.sum_var.get())


GUI().mainloop()