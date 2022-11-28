'''
2.Tkinter 以表格的形式，显示文件
点击选择，出现文件选择对话框
'''
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from turtle import title
import os

flag=0
def select_open_file():
    #返回值为元组形式的文件名
    file=askopenfilename(title='选择文件',filetypes=[('All Files','*.*')])
    print('file:',file)
    global flag
    flag+=1
    labe_n=Label(win,text=flag)
    labe_p=Label(win,text=file)
    labe_n.grid(row=flag+1,column=0)
    labe_p.grid(row=flag+1,column=1)
    labe_p.bind('<Double-Button-1>',lambda f:os.startfile(file) )



win=Tk()
win.geometry("400x400")
win.title('选择文件-双击路径打开')
btn=Button(win,text='选择文件',command=select_open_file)
print(btn)
btn.grid(row=0,columnspan=2)
label1=Label(win,text='序号')
label2=Label(win,text='路径')
label1.grid(row=1,column=0)
label2.grid(row=1,column=1)



win.mainloop()



from tkinter import*
from tkinter.filedialog import *
from tkinter.ttk import *#样式
import os

def ImageOpen():
    file=askopenfilenames(title='打开图片',filetypes=[('png图片','*.png')])#可以一次性选择多张
    for i,filename in enumerate(file):#返回索引和值
        tree.insert('',END,values=(i,filename))

def click(event):
    item=tree.selection()
    print(tree.item(item))
    os.startfile()

win=Tk()
win.title('显示图片')

btn=Button(win,text='选择',command=ImageOpen).pack(pady=5)
tree=Treeview(win,columns=('id','path'),show='headings')
tree.heading('id',text='序号')
tree.heading('path',text='路径')
tree.pack()
tree.bind('<Double-Button-1>',click)#双击左键
win.mainloop()
