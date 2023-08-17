from tkinter import *
root = Tk()
root.title('Dictionary')
root.geometry('400x400')
root.configure(background = 'snow')

DEFS = {'simile': '''A figure of speech in which two unlike things are 
        explicitly compared''',         
        
        'metaphor': '''A figure of speech in which a term or phrase 
        is applied to something to which it is not literally applicable 
        in order to suggest a resemblance.'''}

txtDef = Label(root, bg = 'light blue', fg = 'black')
txtDef.place(relx = 0.5, rely = 0.6, anchor = CENTER)

entWord = Entry(root)
entWord.place(relx = 0.5, rely = 0.4, anchor = CENTER)

def getDef(name):
    txtDef['text'] = DEFS.get(name)

btnGetDef = Button(root, text = 'Get Definition', command = lambda: getDef(entWord.get()))
btnGetDef.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()