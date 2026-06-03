from PIL import Image
from customtkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD

app = CTk()

app.title("Tygra - графический ffmpeg")
app.iconbitmap("res/circle.ico")

x = int(app.winfo_screenwidth()*0.35)
y = int(app.winfo_screenheight()*0.35)
app.geometry(f"{x}x{y}")

logo = CTkImage(light_image=Image.open("res/circle.png"), size=(100, 100))
CTkLabel(app, text="", image=logo).pack(fill="x", pady=10, padx=10)
CTkLabel(app, text="Tygra - GUI конвертор на базе ffmpeg", font=('JetBrains Mono Bold', 20)).pack(fill="x", pady=10, padx=10)

left = CTkFrame(app, width=(x*0.95)//2)
right = CTkFrame(app, width=(x*0.95)//2)

left.pack(side="left", fill="y", padx=10, pady=10)
right.pack(side="right", fill="y", padx=10, pady=10)

app.mainloop()