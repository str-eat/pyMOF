import tkinter as tk

class Notebook(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.new_experiment = tk.Button(self)
        self.edit_existing = tk.Button(self)
        self.new_experiment["text"] = "Create a new experiment"
        self.edit_existing["text"] = "Edit and existing experiment"
        self.new_experiment["command"] = self.create_new_experiment
        self.new_experiment.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def create_new_experiment(self):
        print("new experiment created")

root = tk.Tk()
app = Notebook(master=root)
app.mainloop()