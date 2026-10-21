
import tkinter as tk
root = tk.Tk()
root.title("Máy tính bỏ túi")
root.geometry("320x400")
root.resizable(False, False)
bieu_thuc = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=bieu_thuc,
    font=("Arial", 20),
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4,
           padx=10, pady=15, ipady=10, sticky="nsew")
def bam_nut(gia_tri):
    if gia_tri == "=":
        try:
            ket_qua = eval(bieu_thuc.get())
            bieu_thuc.set(str(ket_qua))
        except:
            bieu_thuc.set("Lỗi")
    elif gia_tri == "C":
        bieu_thuc.set("")
    else:
        if bieu_thuc.get() == "Lỗi":
            bieu_thuc.set("")
        bieu_thuc.set(bieu_thuc.get() + gia_tri)

cac_nut = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for ten_nut, hang, cot in cac_nut:
    nut = tk.Button(
        root,
        text=ten_nut,
        font=("Arial", 16),
        command=lambda x=ten_nut: bam_nut(x)
    )
    nut.grid(row=hang, column=cot,
             padx=4, pady=4, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
