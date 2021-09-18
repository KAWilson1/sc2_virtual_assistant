import tkinter as tk
from tkinter import filedialog
import black_box

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

    def open_build(self):
        """
        Populates the textarea from a text file which is selected via a File Dialog Menu
        """
        path = filedialog.askopenfilename()
        #Open file
        with open(path) as f:
            lines = f.readlines()
        build_steps = black_box.parse_input(lines)

        #Format build steps and populate text area
        for build in build_steps:
            build_str = ""
            build_str += build[0] + " " #Add build timing
            build_str += " ".join(build[1]) + "\n" #Add any number of audio queues
            self.textbox.insert(tk.END, build_str)

    def start(self):
        #Get build from text area
        raw_text = self.textbox.get("1.0", tk.END)
        build_steps = black_box.parse_input(raw_text.splitlines())
        black_box.play_audio_queues(build_steps)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(side="bottom")
        
        lbl_title = tk.Label(self, text="SC2 Virtual Assistant", font=LARGE_FONT)
        lbl_title.pack(pady=10, padx=10)

        lbl_timer = tk.Label(self, text="0:00", font=LARGE_FONT)
        lbl_timer.pack(pady=10, padx=10)

        btn_open = tk.Button(self, text="Open", command=lambda: self.open_build())
        btn_open.pack(side="left")

        btn_save = tk.Button(self, text="Save")
        btn_save.pack(side="left")

        btn_start = tk.Button(self, text="Start", command=lambda: self.start())
        btn_start.pack(side="right")


        self.textbox = tk.Text(bottomFrame)
        self.textbox.pack(side="bottom")



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
    
