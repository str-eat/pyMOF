import tkinter as tk
import sys
import os
import pickle
import csv
try:
    dir_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(dir_path)
    from experiment import Experiment as experiment
    from experiment import get_experiment_types
    from experiment import get_experiment_names
except ImportError:
    print(ImportError)

class Notebook(tk.Frame):
    # Initialize the class as a child of tkInter frame so that a frame opens upon creation and immediately
    # prompt the user whether to create a new experiment, select an existing experiment or exit the window
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

    # create_edit_experiment method creates the buttons that register the action the user will take and links
    # to a method that performs the next function
    def create_edit_experiment(self):
        self.create_experiment = tk.Button(self)
        self.edit_existing = tk.Button(self)
        self.create_experiment["text"] = "Create a new experiment"
        self.edit_existing["text"] = "Edit and existing experiment"
        self.create_experiment["command"] = self.new_experiment
        self.edit_existing["command"] = self.existing_experiment
        self.create_experiment.pack(side="top")
        self.edit_existing.pack(after=self.create_experiment)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.close_window)
        self.quit.pack(side="bottom")

    def new_experiment(self):
        self.empty_window()
        self.__init__(master=root)
        self.nameLabel = tk.Label(self, text="Name")
        self.nameLabel.pack(side='top')
        self.experimentName = tk.Entry(self)
        self.experimentName.pack(after=self.nameLabel)

        self.typeLabel = tk.Label(self, text="Type")
        self.typeLabel.pack(after=self.experimentName)
        self.experimentTypeChoices = get_experiment_types()
        self.experimentType = tk.StringVar(root)
        self.experimentType.set("Synthesis")
        self.experimentTypeDropdown = tk.OptionMenu(self, self.experimentType, *self.experimentTypeChoices)
        self.experimentTypeDropdown.pack(after=self.typeLabel)

        self.objectiveLabel = tk.Label(self, text="Objective")
        self.objectiveLabel.pack(after=self.experimentTypeDropdown)
        self.experimentObjective = tk.Text(self)
        self.experimentObjective.pack(after=self.objectiveLabel)
        
        def submit():
            new_experiment = experiment(self.experimentName.get(), self.experimentType.get(),\
            self.experimentObjective.get("1.0", 'end-1c'))
            print("new experiment created")
            print(new_experiment)
            self.experiment_details(experiment=new_experiment)
        
        self.submitExperiment = tk.Button(self, text='Submit', command=submit)
        self.submitExperiment.pack(side='bottom')

    def existing_experiment(self):
        self.empty_window()
        experimentNameChoices = experiment.get_experiment_names()
        # open existing experiment
        # next screen
        print("Select which experiment you'd like to edit")

    def experiment_details(self, experiment=None):
        self.empty_window()
        self.__init__(master=root)
        
        def save():
            with open('data/experiments.csv', 'r+', newline='')  as myFile:  
                reader = csv.reader(myFile)
                exists = False
                for row in reader:
                    if experiment.experimentName in row:
                        exists = True
                        break                  
                    elif experiment.experimentName not in row:
                        continue
                if not exists:
                    data = [experiment.experimentName, experiment.experimentType, experiment.experimentObjective]
                    writer = csv.writer(myFile)
                    writer.writerow(data)
                    print("Saved")
                else:
                    print("Not saved")
                        
        self.saveExperiment = tk.Button(self, text="Save", command=save)
        self.saveExperiment.pack(side='top')

    def empty_window(self):
        self.destroy()
    
    def close_window(self):
        root.destroy()

root = tk.Tk()
app = Notebook(master=root)
app.create_edit_experiment()
app.mainloop()