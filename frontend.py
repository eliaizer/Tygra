from tkinter.filedialog import askopenfiles, askopenfilenames

from customtkinter import *

from tkinterdnd2 import DND_FILES, TkinterDnD


class frontendTygra(TkinterDnD.CTk):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker
        self.title("Tygra - графический ffmpeg")
        self.iconbitmap("res/circle.ico")

        self.x = int(self.winfo_screenwidth() * 0.35)
        self.y = int(self.winfo_screenheight() * 0.35)
        self.geometry(f"{self.x}x{self.y}")

        self.init_ui()

        self.mainloop()

    def on_string_input(self, event):
        pass

    def on_button_input(self):
        askopenfilenames()

    def on_drop_input(self, event):
        self.input_string.delete(0, "end")
        self.input_string.insert(0, f"{event.data}")

    def on_string_output(self, event):
        pass

    def on_button_output(self):
        askopenfilenames()

    def on_drop_output(self, event):
        self.output_string.delete(0, "end")
        self.output_string.insert(0, f"{event.data}")

    def start_work(self):
        pass

    def init_ui(self):
        #self.label = CTkLabel(self, text="Перетащи файл сюда")
        #self.label.pack(pady=50)
        self.init_ui_left()
        self.init_ui_right()
        # Добавить выбор множества файлов или папок

        # Подумать над сохранением нескольких файлов сразу


    def init_ui_left(self):
        self.left = CTkFrame(self, width=(self.x * 0.95) // 2)

        self.input = CTkFrame(self.left)

        self.loptions = CTkFrame(self.left)
        CTkLabel(self.loptions, text="Опции (обновляются в зависимости от входящих файлов").pack(fill="x", padx=10, pady=10)

        self.input.drop_target_register(DND_FILES)
        self.input.dnd_bind("<<Drop>>", self.on_drop_input)

        self.input_string_group = CTkFrame(self.input)
        self.input_label = CTkLabel(self.input, text="Перетащите файл сюда...")

        self.input_string = CTkEntry(self.input_string_group)
        self.input_button = CTkButton(self.input_string_group, text="Обзор...", command=self.on_button_input)

        self.left.pack(side="left", fill="y", padx=10, pady=10)
        self.input.pack(side="top", fill="x", padx=10, pady=10)
        self.loptions.pack(side="top", fill="x", padx=10, pady=10)
        self.input_string_group.pack(side="top", fill="x", padx=10, pady=10)
        self.input_label.pack()
        self.input_string.pack(side="left")
        self.input_button.pack(side="right")

        #CTkLabel(left, text="Какой файл вы хотите конвертировать?").pack(side="left", fill="y", padx=10, pady=10)


        #ffmpegOption = CTkFrame(left, bg_color="white")
        #ffmpegOption.pack(pady=10)
        # Добавить появление флагов для выбранного файла

    def init_ui_right(self):
        self.right = CTkFrame(self, width=(self.x * 0.95) // 2)

        self.output = CTkFrame(self.right)

        self.roptions = CTkFrame(self.right)
        CTkLabel(self.roptions, text="Опции (обновляются в зависимости от входящих файлов").pack(fill="x", padx=10,
                                                                                                pady=10)

        self.output.drop_target_register(DND_FILES)
        self.output.dnd_bind("<<Drop>>", self.on_drop_output)

        self.output_string_group = CTkFrame(self.output)
        self.output_label = CTkLabel(self.output, text="Перетащите файл сюда...")

        self.output_string = CTkEntry(self.output_string_group)
        self.output_button = CTkButton(self.output_string_group, text="Обзор...", command=self.on_button_output)

        CTkButton(self.right, text="Старт", command=self.start_work).pack(side="bottom", fill="y", padx=10, pady=10)

        self.right.pack(side="right", fill="y", padx=10, pady=10)
        self.output.pack(side="top", fill="x", padx=10, pady=10)
        self.roptions.pack(side="top", fill="x", padx=10, pady=10)
        self.output_string_group.pack(side="top", fill="x", padx=10, pady=10)
        self.output_label.pack()
        self.output_string.pack(side="left")
        self.output_button.pack(side="right")



#logo = CTkImage(light_image=Image.open("res/circle.png"), size=(100, 100))
#CTkLabel(app, text="", image=logo).pack(fill="x", pady=10, padx=10)
#CTkLabel(app, text="Tygra - GUI конвертор на базе ffmpeg", font=('JetBrains Mono Bold', 20)).pack(fill="x", pady=10, padx=10)