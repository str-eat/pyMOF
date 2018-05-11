import string
import datetime
import csv

class Experiment(object):
    def __init__(self, experimentName, experimentType, experimentObjective):
        super().__init__()
        self.experimentName = experimentName
        self.experimentType = experimentType
        self.experimentObjective = experimentObjective
        self.create_experiment()

    def create_experiment(self):
        self.date = datetime.date.today()
        print(self.experimentName)
        print(self.experimentType)
        print(self.experimentObjective)

        #FIX THIS
        # while material is not "\r":
            # material_amount = self.remove_spaces(input("How much of {} was used?".format(material)))
            # self.materials[material] = material_amount
            # material = self.remove_spaces(input("What materials were used?")).casefold()

    def remove_spaces(self, string):
        new_string = ""
        for char in string:
            if char is " ":
                char = ""
            new_string = new_string + char
        return new_string

def get_experiment_names():
    return

def get_experiment_types():
    with open('data/experiment types.csv', 'r') as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            experiment_types_list = row
    return experiment_types_list