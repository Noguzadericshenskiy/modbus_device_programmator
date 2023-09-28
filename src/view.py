from tkinter import Tk, Button, filedialog, Frame, StringVar, Listbox
from tkinter.ttk import Combobox, Entry, Label, Progressbar

from src import config
from devices import devases_setup

port = "COM5"


class RootWin(Tk):
    def __init__(self):
        super().__init__()
        self.title("Программатор устройств Modbus")
        self.geometry("1000x800")
        self.resizable(False, False)
        self.configure(background=config.main_window_color)
        self.lbl_type = Label(self, text='Тип',)
        self.lbl_type.config(config.lbl_conf)
        self.lbl_type.grid(column=0, row=1)
        self.combobox_type = Combobox(
            self,
            width=40,
            height=10,
            values=self.combobox_type(),
            state="readonly"
        )
        # self.combobox_type.bind("<<ComboboxSelected>>", self.selected_type)
        self.combobox_type.grid(column=1, row=1)
        self.btn_connect = Button(self, text="Подключить", command=self.get_selected_type,)
        self.btn_connect.config(config.btn_conf)
        self.btn_connect.grid(column=2, row=1, columnspan=2)
        self.btn_disconnect = Button(self, text="Отключить", command=self.disconnect,)
        self.btn_disconnect.config(config.btn_conf)
        self.btn_disconnect.grid(column=5, row=1)
        self.lbl_status_devise = Label(self, text='Статус',)
        self.lbl_status_devise.config(config.lbl_conf)
        self.lbl_status_devise.grid(column=0, row=2)
        self.lbl_status = Label(self, text="подключено", )
        self.lbl_status.config(config.lbl_conf)
        self.lbl_status.grid(column=1, row=2)
        self.lbl_address = Label(self, text="Адрес",)
        self.lbl_address.config(config.lbl_conf)
        self.lbl_address.grid(column=2, row=2)
        self.etr_address = Entry(self)
        self.etr_address.grid(column=3, row=2,)
        self.btn_write = Button(self, text="Записать", command=self.write )
        self.btn_write.config(config.btn_conf)
        self.btn_write.grid(column=5, row=2)
# ToDo сюда добавить поле вывода с информацией
        self.i = InfoBordFrame()
        self.i.grid(column=0, row=3, columnspan=5)
        self.i.config(borderwidth=2, background="#00FA9A")


        self.etr_save_info = Button(
            self,
            text="Сохранить в файл",
            command=self.save_in_file,
            background=config.button_color,
            borderwidth=4,
        )
        self.etr_save_info.grid(column=0, row=4)

    def get_selected_type(self):
        value = self.combobox_type.get()
        print(value)

    @staticmethod
    def combobox_type():
       listd = ()
        for i in devases_setup:
         listd(i["name"])

        items = ("Type 1", "Type 2", "Type 3", "Type 4")

        return items

    def get_list_devices():
        ...

    def quit_app(self):
        self.quit()

    def disconnect(self):
        print("Отключить")

    def write(self):
        self.pbar_write = Progressbar(self,
                                      orient="horizontal",
                                      mode="indeterminate",
                                      )
        self.pbar_write.grid(column=0, row=5)

        value = self.etr_address.get()
        print(value)

    def save_in_file(self):
        filedialog.asksaveasfilename(title="Сохранение в файл")
        print("Сохранить в файл")


class InfoBordFrame(Frame):
    def __init__(self):
        super().__init__()
        self.columnconfigure(2)
        self.rowconfigure(2)
        self.lbl_status_devise = Label(self, text='Содержание регистров устройства',)
        self.lbl_status_devise.config(config.lbl_conf)
        self.lbl_status_devise.grid(column=0, row=1, )
        self.lbl_status_devise = Label(self, text='Содержание регистров устройства после записи', )
        self.lbl_status_devise.config(config.lbl_conf)
        self.lbl_status_devise.grid(column=0, row=1)

        listvar = StringVar(value="param1")
        c = Listbox(listvariable=listvar, height=10)








if __name__ == "__main__":
    app = RootWin()
    app.mainloop()
