#!/usr/bin/env python3
#Button Clicker
#Bethany DuMontelle
#11 December 2017

"""A program that has you push buttons to unlock it"""

#imports everything from tkinter
from tkinter import *

#sets up a font that is used throughout the program
FONT = ("Arial", 12)

#custom class; derived from Frame
class Application(Frame):
    """"""
    def __init__(self, master):
        """initializes the frame"""
        #calls super application, master at the end calls the same __init__
        super(Application, self).__init__(master)
        self.grid()
        #makes the password string that's needed to know the password
        self.password = ''
        #created widgets
        self.create_widgets()
        
    def create_widgets(self):
        """creates text entry box for the buttons clicked and buttons for the user to click"""
        #text entry box
        self.txe_password = Entry(self, width = 15)
        self.txe_password.grid(row = 0, column = 0, sticky = W, columnspan = 3)  
        
        #number buttons
        self.btn_one = Button(self, text = '1', font = FONT, 
                              command = lambda:self.password_nums("1"))      
        self.btn_one.grid(row = 3, column = 0)
        
        self.btn_two = Button(self, text = '2', font = FONT,
                                      command = lambda:self.password_nums("2"))      
        self.btn_two.grid(row = 3, column = 1) 
        
        self.btn_three = Button(self, text = '3', font = FONT,
                                        command = lambda:self.password_nums("3"))      
        self.btn_three.grid(row = 3, column = 2)  
        
        self.btn_four = Button(self, text = '4', font = FONT,
                                          command = lambda:self.password_nums("4"))      
        self.btn_four.grid(row = 2, column = 0)  
        
        self.btn_five = Button(self, text = '5', font = FONT,
                                   command = lambda:self.password_nums("5"))      
        self.btn_five.grid(row = 2, column = 1)  
        
        self.btn_six = Button(self, text = '6', font = FONT,
                                     command = lambda:self.password_nums("6"))      
        self.btn_six.grid(row = 2, column = 2)  
        
        self.btn_seven = Button(self, text = '7', font = FONT,
                                   command = lambda:self.password_nums("7"))      
        self.btn_seven.grid(row = 1, column = 0)    
        
        self.btn_eight = Button(self, text = '8', font = FONT,
                                       command = lambda:self.password_nums("8"))      
        self.btn_eight.grid(row = 1, column = 1)   
        
        self.btn_nine = Button(self, text = '9', font = FONT,
                                    command = lambda:self.password_nums("9"))      
        self.btn_nine.grid(row = 1, column = 2) 
        
        self.btn_zero = Button(self, text = '0', font = FONT,
                                     command = lambda:self.password_nums("0"))      
        self.btn_zero.grid(row = 4, column = 0) 
        
        #unlock button
        self.btn_unlock = Button(self, text = 'Unlock', font = FONT,
                                   command = self.unlock)      
        self.btn_unlock.grid(row = 5, column = 0, columnspan = 3)     
    
        #clear button
        self.btn_clear = Button(self, text = 'Clear', font = FONT,
                                command = self.clear_text)
        self.btn_clear.grid(row = 4, column = 1, columnspan = 2)
        
        #Thanks to stack overflow (https://goo.gl/9434v6), JasonPy's answer
        #made me realize how this piece works and got the whole program to run
    def password_nums(self , password_add):
        '''adds the number pressed into the password variable'''
        if len(self.password) < 7:
            self.password += password_add
        #brings it to the update text function
        self.update_text()
            
    def update_text(self):
        '''erases current text and places the new password inside the text entry box'''
        self.txe_password.delete(0, END)
        self.txe_password.insert(INSERT, self.password)
    
    def clear_text(self):
        '''erases current text and resets the password variable'''
        self.txe_password.delete(0, END)
        self.password = ''
        
    def unlock(self):
        '''decides whether the password is correct or not'''
        if self.password == '3014159' :
            self.password = 'UNLOCKED!'
            
        else:
            self.password = 'ERROR'
        self.update_text()
    
#main
#create root window
root = Tk()

#sets attributes of the window
root.title("Password")
root.geometry("125x195")

#framework
app = Application(root)
app.grid()

#kick off the event handler loop
root.mainloop()

