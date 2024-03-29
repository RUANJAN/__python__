'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('red.TFrame', background='#ff0000')
        ttkStyle.configure('white.TFrame', background='#ffffff')
        ttkStyle.configure('yellow.TFrame', background='yellow')
        ttkStyle.configure('white.TLabel', background='#ffffff')
        ttkStyle.configure('gridLabel.TLabel', font=(
            'Helvetica', 16), foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry', font=('Helvetica', 16))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame, text="BMI試算", font=(
            'Helvetica', '20')).pack(pady=(80,20))

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True, fill=tk.BOTH)
        bottomFrame.columnconfigure(0, weight=3, pad=20)
        bottomFrame.columnconfigure(1, weight=5, pad=20)
        bottomFrame.rowconfigure(0, weight=1, pad=20)
        bottomFrame.rowconfigure(3, weight=1, pad=20)
        bottomFrame.rowconfigure(4, weight=1, pad=20)
        bottomFrame.rowconfigure(5, weight=1, pad=20)
        bottomFrame.rowconfigure(6, weight=1, pad=20)

        # 定義entry的textvariable
        self.nameStringVar = tk.StringVar()
        self.birthStringVar = tk.StringVar()
        self.heightIntVar = tk.IntVar()
        self.weightIntVar = tk.IntVar()

    # nameStringVar = tk.StringVar()
        ttk.Label(bottomFrame, text="姓名:", style='gridLabel.TLabel').grid(column=0, row=0, sticky=tk.E)

        nameEntry = ttk.Entry(
            bottomFrame, style='gridEntry.TEntry', textvariable=self.nameStringvar)
        nameEntry.grid(column=1, row=0, sticky=tk.W, padx=10)
    
        ttk.Label(bottomFrame, text="出生年月日:", style='gridLabel.TLabel').grid(
            column=0, row=1, sticky=tk.E)
        ttk.Label(bottomFrame, text="(2000/03/01)",style='gridLabel.TLabel').grid(column=0, row=2, sticky=tk.E)

        birthEntry = ttk.Entry(
            bottomFrame, style='gridEntry.TEntry', textvariable=self.birthStringVar)
        birthEntry.grid(column=1, row=1, sticky=tk.W, rowspan=2, padx=10)

        ttk.Label(bottomFrame, text="身高(cm):", style='gridLabel.TLabel').grid(
            column=0, row=3, sticky=tk.E)
        heightEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry', textvariable=self.heightintVat)
        heightEntry.grid(column=1, row=3, sticky=tk.W, padx=10)

        ttk.Label(bottomFrame, text="體重(kg):", style='gridLabel.TLabel').grid(column=0, row=4, sticky=tk.E)
        weightEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry', textvariable=self.weightIntVar)
        weightEntry.grid(column=1,row=4,sticky=tk.W,padx=10)
        
        self.messageText = tk.Text(
            bottomFrame, height=5, width=35, state=tk.DISABLED, takefocus=0, bd=0)
        self.messageText.grid(column=0, row=5, sticky=tk.N+tk.S, columnspan=2)

        messageText = tk.Text(bottomFrame, height=5,width=35, state=tk.DISABLED, takefocus=0, bd=0)
        messageText.grid(column=0, row=5, sticky=tk.N+tk.S, columnspan=2)

        #---------commitFrame開始-------------------------
        #有左右2個按鈕
        #
        commitFrame = ttk.Frame(bottomFrame)
        commitFrame.grid(column=0, row=6, columnspan=2)
        commitFrame.columnconfigure(0,pad=10)
        commitBtn = ttk.Button(commitFrame, text="計算")
        commitBtn.grid(column=0, row=0, sticky=tk.W)

        
        #clearBtn = ttk.Button(commitFrame, text="清除",command=lambda:print("清除"))這段是註冊一個城市
        # lambda註冊
        clearBtn = ttk.Button(commitFrame, text="清除", command=self.press_clear)
        clearBtn.grid(column=1,row=0,sticky=tk.E)
        #---------commitFrame結束-----------------

        #先在終端機裡先python才可以進入HELP求救
        # 在終端機下載pip install pillow
        #---------建立LOGO---------------
        logoImage = Image.open('logo.png')
        resizeImage = logoImage.resize((80,80),Image.LANCZOS)
        self.logoTkImage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(self,image=self.logoTkimage, width=180)
        logoLabel.place(x=30,y=40)
        # logoLabel = ttk.Label(self,image=self.logoTkimage,width=180)


    def press_clear(self) -> None:
        self.nameStringVar.set("")
        self.birthStringVar.set("")
        self.heightIntVar.set(0)
        self.weightIntVar.set(0)
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete("1.0", tk.END)
        self.messageText.configure(state=tk.DISABLED)
        print("清除")

def close_window(w):
    w.destroy()


'''
def press_clear(self,*args) -> None:
    for widfet in args:
        print(widfet)
        # 要執行widget.text--要變成---->widget.configure(text)
    print("清除")    
'''
    
#這是程式的執行點

    # window.geometry("400x500")
    #無法調整視窗大小的指令
    # window.protocol("WM_DELETE_WINDOW",lambda:window.destroy())



def main():
    window = Window()
    window.title("BMI計算")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW",lambda: close_window(window))
    window.mainloop()


if __name__ == "__main__":
    main()

