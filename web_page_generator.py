import tkinter as tk
from tkinter import *
#webbrowser module is a python library that
#allows you to create web documents and display them in the browser. 
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.entry = tk.Entry(self)

        #Creates a button that says “Default HTML Page” under the “Web Page Generator” title 
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10) , pady=(10,10))


        #Creates a button that allows user to submit custom text to web generator
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.userinput)
        self.btn.grid(row=2, column=2, padx=(10,10) , pady=(10,10))

        #Creates an entry bar to type customized text
        self.userinputlabel = Label(self.master, text="Enter custom text or click the default HTML")
        self.userinputlabel.grid(row=0, column=1)
        self.userinput = Entry(width=75)
        self.userinput.grid(row=1, column=1, columnspan=1, padx=(10, 10), pady=(10, 10))
        
        
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def userinput(self):
        htmlText = self.userinput.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
       



    



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
