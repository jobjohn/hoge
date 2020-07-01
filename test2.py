import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title(u"ファイル名変換くん")  # タイトル
    root.geometry("700x200")  # ウィンドウの幅と高さピクセル単位で指定（width x height）

    fr1 = tk.Frame()
    fr1.pack()

    lf = ttk.Labelframe(
        fr1,
        text='Options',
        padding=5)

    selected_frame = tk.IntVar()
    rd1 = tk.Radiobutton(
        lf, text='DLsite', variable=selected_frame, value=0)
    rd2 = tk.Radiobutton(
        lf, text='Fansa', variable=selected_frame, value=1)
    rd1.pack()
    rd2.pack()
    lf.pack(fill="x", padx=20)

    root.mainloop()
