import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 対策: ラジオボタンの選択をここで保持で永続化
        self.selected_frame = tk.IntVar(0)  # Radiobuttonのvalue属性と同じ値でデフォルト選択 ここではDLsite

        self.create_widgets()

    def create_widgets(self):

        fr1 = tk.Frame(root)
        fr1.pack()

        # ここで保持しようとするとこの関数終了後に変数が破棄されちゃって、値を保持できない
        # selected_frame = tk.IntVar()

        rd1 = tk.Radiobutton(fr1, text='DLsite',
                             variable=self.selected_frame, value=0)
        # rd1.pack(fill='x', side='left')
        rd1.pack()
        rd2 = tk.Radiobutton(
            fr1, text='Fansa', variable=self.selected_frame, value=1)
        # rd2.pack(fill='x', side='left')
        rd2.pack()


if __name__ == "__main__":
    root = tk.Tk()
    myapp = Application(master=root)
    myapp.master.title("ファイル名変換くん")  # タイトル
    myapp.master.geometry("700x200")  # ウィンドウの幅と高さピクセル単位で指定 (width x height)

    myapp.mainloop()
