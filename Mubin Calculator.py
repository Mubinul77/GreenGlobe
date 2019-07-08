from tkinter import*

def iCalc(source, side):
    storeObj = Frame (source, borderwidth =1,bd=4, bg="power blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command = None):
    storeObj = button(source, side, text, command = commadn)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def _init_(self):
        Frame._init_(slef)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('calculator')

        display = StringVar()
        Entry (self, relief=RAISED,
               textvariable=display,justify='right', bd=30, bg="powder blue").pack(side=TOP, expand=YES,
                        fill=BOTH)

        for clearBut in(["CE"],["C"]):
            erase = iCalc(slef, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))
        for NumBut in ("789/","456*","123-","0.+"):
            FunctionNum= iCalc(self,TOP)
            for char in NumBut:
                button (FunctionNum, LEFT, char,
                        lambda storeObj=display, q=char: storeObj.set(storeObj.get()+q))
        EqualsButton= iCalc(self,TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals = button (EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button (EqualsButton, LEFT, iEquals,
                                     lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
if __name__ == '_main_':
    app().mainloop()
                
        
