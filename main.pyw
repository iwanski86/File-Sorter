import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import os
import shutil

images_formats = ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.raw']
audio_formats = ['.mp3', '.wav', '.flac', '.wma', '.aac', '.m4a']
video_formats = ['.mp4', '.mov', '.avi', '.wmv', '.webm', '.flv', '.mkv', '.ogv', '.ogg', '.mov', '.qt',
                 '.rm', '.rmvb', '.m4p', '.mpg', '.mp2', '.mpeg', '.mpv', '.mpe', '.m2v', '.m4v', '.svi', '.3gp',
                 '.3g2', '.f4v', '.f4p', '.f4a', '.f4b']
text_formats = ['.doc', '.docx', '.pdf', '.md', '.eml', '.rtf', '.txt', '.log', '.asc', '.msg', '.wps']
executable_formats = ['.bat', '.bin', '.cmd', '.com', '.cpl', '.exe', '.msc', '.msi', '.msp']


class Root:

    def __init__(self):
        self.directory = ""
        self.root = tk.Tk()
        self.root.tk_setPalette(background='white')
        self.root.geometry("300x450")
        self.root.minsize(300, 450)
        self.root.title("file sorter")

        # button-check state
        self.images_check_state = tk.IntVar()
        self.audio_check_state = tk.IntVar()
        self.video_check_state = tk.IntVar()
        self.text_check_state = tk.IntVar()
        self.executable_check_state = tk.IntVar()

        # gui elements
        self.label1 = tk.Label(self.root, text="Folder: ", font=('Calibri bold', 12))
        self.folder_label = tk.Label(self.root, text="No folder chosen", font=('Calibri', 11))
        self.folder_button = tk.Button(self.root, text="Change", font=("Calibri", 11), command=self.choose_folder)
        self.what_label = tk.Label(self.root, text="What to sort: ", font=('Calibri bold', 12))
        self.desc_label = tk.Label(self.root, text="Sub-folders will be created in the above folder. "
                                                   "\n If sub-folders exist files will be placed in there.",
                                   font=('Calibri italic', 10), wraplength=280)
        self.separator = ttk.Separator(self.root)
        self.images_check = tk.Checkbutton(self.root, text="images", font=("Calibri", 12),
                                           variable=self.images_check_state)
        self.audio_check = tk.Checkbutton(self.root, text="audio", font=("Calibri", 12),
                                          variable=self.audio_check_state)
        self.video_check = tk.Checkbutton(self.root, text="video", font=("Calibri", 12),
                                          variable=self.video_check_state)
        self.text_check = tk.Checkbutton(self.root, text="text", font=("Calibri", 12),
                                         variable=self.text_check_state)
        self.executable_check = tk.Checkbutton(self.root, text="executable", font=("Calibri", 12),
                                               variable=self.executable_check_state)
        self.start_button = tk.Button(self.root, text="Start", font=("Calibri bold", 12), command=self.sort_it)
        self.label2 = tk.Label(self.root, text="", font=('Calibri', 12))

        # template
        self.label1.grid(column=0, row=0, padx=10, pady=0, sticky='w')
        self.folder_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')
        self.folder_button.grid(column=0, row=2, padx=10, pady=5, sticky='w')
        self.desc_label.grid(column=0, row=3, padx=10, sticky='w')
        self.separator.grid(column=0, row=4, padx=10, pady=10, sticky='ew')
        self.what_label.grid(column=0, row=5, padx=10, sticky='w')
        self.images_check.grid(column=0, row=6, padx=10, sticky='w')
        self.audio_check.grid(column=0, row=7, padx=10, sticky='w')
        self.video_check.grid(column=0, row=8, padx=10, sticky='w')
        self.text_check.grid(column=0, row=9, padx=10, sticky='w')
        self.executable_check.grid(column=0, row=10, padx=10, sticky='w')
        self.start_button.grid(column=0, row=11, padx=10, pady=10, sticky='w')
        self.label2.grid(column=0, row=12, padx=10, sticky='w')

        self.root.mainloop()

    def choose_folder(self):
        self.directory = tk.filedialog.askdirectory()
        self.folder_label.config(text=self.directory, wraplength=280)
        self.folder_label.config(fg='black')
        if self.directory == "":
            self.folder_label.config(text="No folder chosen")

    def sort_it(self):

        if self.directory == "":
            self.folder_label.config(fg='red')
        else:
            images_path = self.directory + '/images'
            audio_path = self.directory + '/audio'
            video_path = self.directory + '/video'
            text_path = self.directory + '/text'
            executable_path = self.directory + '/executable'

            # create directories if they don't exist
            if self.images_check_state.get() == 1 and not os.path.exists(images_path):
                os.mkdir(images_path)
            if self.audio_check_state.get() == 1 and not os.path.exists(audio_path):
                os.mkdir(audio_path)
            if self.video_check_state.get() == 1 and not os.path.exists(video_path):
                os.mkdir(video_path)
            if self.text_check_state.get() == 1 and not os.path.exists(text_path):
                os.mkdir(text_path)
            if self.executable_check_state.get() == 1 and not os.path.exists(executable_path):
                os.mkdir(executable_path)

            # sorting loop
            for entry in os.listdir(self.directory):
                
                self.label2.config(text="Working...", fg='red')

                source_path = os.path.join(self.directory, entry)

                if self.images_check_state.get() == 1 and entry.endswith(tuple(images_formats)):
                    destination_path = os.path.join(images_path, entry)
                    shutil.move(source_path, destination_path)
                    
                elif self.audio_check_state.get() == 1 and entry.endswith(tuple(audio_formats)):
                    destination_path = os.path.join(audio_path, entry)
                    shutil.move(source_path, destination_path)
                    
                elif self.video_check_state.get() == 1 and entry.endswith(tuple(video_formats)):
                    destination_path = os.path.join(video_path, entry)
                    shutil.move(source_path, destination_path)

                elif self.text_check_state.get() == 1 and entry.endswith(tuple(text_formats)):
                    destination_path = os.path.join(text_path, entry)
                    shutil.move(source_path, destination_path)
                    
                elif self.executable_check_state.get() == 1 and entry.endswith(tuple(executable_formats)):
                    destination_path = os.path.join(executable_path, entry)
                    shutil.move(source_path, destination_path)

            self.label2.config(text="Done", fg='green')


Root()
