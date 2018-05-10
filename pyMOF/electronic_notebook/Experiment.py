import string
import datetime

class Experiment():

    def __init__(self):
        
        _experiment_types = ['synthesis', 'samplepreparation', 'analysis']

        self.date = datetime.date.today()
        self.type = remove_spaces(input("What type of experiment are you performing? (Synthesis, Sample Preparation, Analysis)").casefold())
        
        while self.type not in _experiment_types:
            self.type = remove_spaces(input("""That input was incorrect - please enter again.
            What type of experiment are you performing? (Synthesis, Sample Preparation, Analysis)""").casefold())

        _raw_materials = {'water' : ['water', 'h2o', 'dihydrogenmonoxide'], 
                          'zinc oxide': ['zincoxide', 'zno', 'zinc(ii)oxide'],
                          'acetonitrile': ['acn']}

        self.materials = {}              
        material = remove_spaces(input("What materials were used?")).casefold()

        #FIX THIS
        while material is not "\r":
            material_amount = remove_spaces(input("How much of {} was used?".format(material)))
            self.materials[material] = material_amount
            material = remove_spaces(input("What materials were used?")).casefold()

def remove_spaces(string):
    new_string = ""
    for char in string:
        if char is " ":
            char = ""
        new_string = new_string + char
    return new_string


