import tkinter as tk
import tkinter.ttk as ttk
import picfilter
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.abpath = "C:\\Users\\l\\Desktop\\windows_pic\\"
        self.master.title("DeskFinder")
        self.master.maxsize(1000, 400)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        # create Widgets
        self.leftlist = tk.Listbox(self, selectmode='browse')
        self.rightframe = tk.Frame(self)
        self.rightframe.canvas = tk.Canvas(self, width=400, height=225, bg="black")
        self.rightframe.namebar = tk.Frame(self, width=400)
        self.rightframe.namebar.nameinput = tk.Frame(self)
        self.rightframe.namebar.nameinput.entry1 = ttk.Entry(self, width=50)
        self.rightframe.namebar.nameinput.button1 = tk.Button(self, height=1, width=10)
        self.rightframe.namebar.namedisplay = tk.Label(self)

        name_list = self.leftlist
        pic_canvas = self.rightframe.canvas
        name_label = self.rightframe.namebar.namedisplay
        name_input = self.rightframe.namebar.nameinput.entry1
        name_button = self.rightframe.namebar.nameinput.button1

        # 获取图片文件名列表
        self.piclist = picfilter.getlist()
        print(self.piclist[-1])
        for i in self.piclist:
            self.leftlist.insert('end', '-' + i)
        self.leftlist.configure(height=len(self.piclist))

        # 显示当前文件名
        self.currentFile = self.piclist[0]  # 当前被选中的图片名称
        self.fillText = tk.StringVar()
        self.fillText.set(self.currentFile)
        # 'Rename the picture here here(if you want)'
        name_label['text'] = "Filename is \'" + self.currentFile + "\'"
        name_label['anchor'] = 'nw'
        name_input['textvariable'] = self.fillText

        # 设置首次图片显示

        image = self.abpath + self.currentFile
        image = Image.open(image)
        # TODO:find out how to autoset the size of pic
        image = image.resize((400, 225), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        # TODO:why it is [202,114],where is [0,0]:the center of the window?
        pic_canvas.create_image([202, 114], image=image)

        # 绑定button与更改图片名称
        name_button.configure(text="Rename")
        name_button.bind("<Button-1>", self.New_name)

        # 绑定listbox与更改图片展示
        name_list.bind("<<ListboxSelect>>", self.Pic_select)

        # pack各类Widgets
        self.leftlist.pack(side="left", padx=10, pady=10, fill="both", expand=1)

        self.rightframe.canvas.pack(side="top", pady=10)

        self.rightframe.namebar.namedisplay.pack(fill='y', pady=10)

        name_input.pack(side='left', anchor='center', padx=20)
        name_button.pack(side='left', anchor="center", padx=10)
        self.rightframe.namebar.nameinput.pack(anchor='center', fill='y')

        self.rightframe.namebar.pack(pady=10)

        self.rightframe.pack(side="right")
        self.pack()
        self.mainloop()

    def List_flash(self, old, new):
        index = self.piclist.index(old)
        print("index:" + str(index))
        self.piclist = picfilter.getlist()
        print("list changed")
        self.leftlist.configure(height=len(self.piclist))
        self.leftlist.delete(index)
        self.leftlist.insert(index, '-' + new)
        self.leftlist.select_set(index)
        self.leftlist.mainloop()

    def New_name(self, event):
        new = self.fillText.get()
        old = self.currentFile
        if (picfilter.namechange(old, new)):
            downlabeltext = "File name is changed,new name is \"" + new + "\""
        else:
            downlabeltext = "File name change failed"
        self.rightframe.namebar.namedisplay.config(text=downlabeltext)
        self.currentFile = new
        self.fillText.set(self.currentFile)
        self.List_flash(old, new)

    def Pic_display(self, filename):
        image = self.abpath + filename
        print("image:" + image)
        # TODO:change image path to currentpic
        image = Image.open(image)
        # TODO:find out how to autoset the size of pic
        image = image.resize((400, 225), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        # TODO:why it is [202,114],where is [0,0]:the center of the window?
        self.rightframe.canvas.create_image([202, 114], image=image)
        self.rightframe.canvas.mainloop()
        # self.mainloop()

    def Pic_select(self, event):
        CurSelection = self.leftlist.curselection()
        print(CurSelection)
        CurSelection = CurSelection[0]
        CurSelection = self.piclist[CurSelection]
        self.currentFile = CurSelection
        self.rightframe.namebar.namedisplay.config(text=self.currentFile)
        self.fillText.set(self.currentFile)
        self.Pic_display(self.currentFile)


