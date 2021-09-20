import tkinter as tk
from tkinter import filedialog
import black_box
import playsound

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
            #m:ss time format of build timing
            build_str += str(build[0] // 60) + ":" + str(build[0] % 60) + " "
            #Add any number of audio queues
            build_str += " ".join(build[1]) + "\n" 
            self.textbox.insert(tk.END, build_str)

    def start(self):
        """
        Starts the stopwatch on the GUI and plays audio queues at specified times
        For n audio queues that play, the next n function calls to start() will occur
            650ms faster than if no audio queue(s) played. This allows the timer to 
            maintain relatively accurate timing while playing queues.
        """
        #Get time from GUI
        counter = self.lbl_timer["text"]
        split_time = counter.split(":")
        counter_sec = int(split_time[0]) * 60 + int(split_time[1])
        
        #Get build from text area
        raw_text = self.textbox.get("1.0", tk.END)
        build_steps = black_box.parse_input(raw_text.splitlines())

        #Write new time to GUI
        new_time = counter_sec + 1 # increment next time to render
        counter_to_display = str(new_time // 60) + ":" + str(new_time % 60) #m:ss time format
        self.lbl_timer["text"] = counter_to_display

        #Check if current time has associated audio queue
        global num_audio_queues #queues to be played this function call
        for i in range(0, len(build_steps)):
            if counter_sec == build_steps[i][0]:
                for audio_queue in build_steps[i][1]:
                    playsound.playsound("audio_queues/" + audio_queue + ".mp3")
                    num_audio_queues += 2 #add 2 seconds of "recovered time" per audio queue
        
        #For n audio queues that play, the next n function calls will occur sooner
        if num_audio_queues > 0:
            num_audio_queues -= 1
            self.after(350, self.start)
        else:
            self.after(1000, self.start)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(side="bottom")
        
        lbl_title = tk.Label(self, text="SC2 Virtual Assistant", font=LARGE_FONT)
        lbl_title.pack(pady=10, padx=10)

        self.lbl_timer = tk.Label(self, text="0:00", font=LARGE_FONT)
        self.lbl_timer.pack(pady=10, padx=10)

        btn_open = tk.Button(self, text="Open", command=lambda: self.open_build())
        btn_open.pack(side="left")

        btn_save = tk.Button(self, text="Save")
        btn_save.pack(side="left")

        btn_start = tk.Button(self, text="Start", command=lambda: self.start())
        btn_start.pack(side="right")

        self.textbox = tk.Text(bottomFrame)
        self.textbox.pack(side="bottom")

if __name__ == "__main__":
    global num_audio_queues #used to adjust timer based on number of played audio queues
    num_audio_queues = 0
    app = MainWindow()
    app.mainloop()
    
