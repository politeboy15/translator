from tkinter import *
from googletrans import Translator
def tran():
    text = t.get('1.0', END)
    a = translator.translate(text, dest = 'en')
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)
root = Tk()
root.geometry('500x350')
root.title('Translator v0.0.3')
root.resizable(0, 0)
root['bg'] = 'cadetblue1'
translator = Translator()
label = Label(root,fg='lime',background='blanchedalmond',font='Arial 15',text = 'Write your sentence or word:  ')
label.place(relx=0.5, y = 30,anchor=CENTER)
t = Text(root, width=35,height=5,font='Arial 12')
t.place(relx=0.5, y = 100, anchor=CENTER)
btn = Button(root,width=45,text='Translate',command=tran)
btn.place(relx=0.5, y = 180, anchor=CENTER)
t1 = Text(root, width=35,height=5,font='Arial 12')
t1.place(relx=0.5, y = 260, anchor=CENTER)
root.mainloop()