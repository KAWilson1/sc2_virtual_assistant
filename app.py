import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #init Tk
        container = tk.Frame(self) #define window

        #side sets our constraints
        #expand means go past our contraints if there is whitespace in the window
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame = StartPage(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(side="bottom")
        
        label = tk.Label(self, text="Text Display", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button0 = tk.Button(self, text="button0")
        button0.pack(side="left")

        button1 = tk.Button(self, text="button1")
        button1.pack(side="left")

        button2 = tk.Button(self, text="button2")
        button2.pack(side="left")


        textbox = tk.Text(bottomFrame)
        textbox.pack(side="bottom")



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
    
