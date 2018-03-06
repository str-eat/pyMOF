import os

class Crystal():
    '''
    PARAM: None
    RETURNS: None
    DESCRIPTION: Store the crystal attributes for later recall, when the data allows for a 2-D array
    the method name is prefixed with "append" when the data is a string or a 1-D array
    the method name is prefixed with "set"
    '''
    def __init__(self):
        name = ""
        group = ""
        cell = []
        self.node = []
        self.edge = []
        self.edgeCenter = [] 
    
    def setName(self, input):
        self.name = input
        
    def setGroup(self, input):
        self.group = input
    
    def setCell(self, input):
        self.cell = input
        
    def appendNodeArray(self, input):
        self.node.append(input) 
    
    def appendEdgeArray(self, input):
        self.edge.append(input)
        
    def appendEdgeCenterArray(self, input):
        self.edgeCenter.append(input)
        
    
def search_RCSR(crystalArray, searchFor):    
    while True:
        for crystal in crystalArray:
            if crystal.name == searchFor:
                print("name " + crystal.name)
                print("group " + crystal.group)
                for c in crystal.cell:
                    print("cell " + c)
                for n in crystal.node:
                    for each in n:
                        print("node " + each)
                for e in crystal.edge:
                    for each in e:
                        print("edge " + each)
                for ec in crystal.edgeCenter:
                    for each in ec:
                        print("edgeCenter " + each)
                        
def convert_RCSR_to_dictionary(crystalArray):
    """
        creates a dictionary of Crystal objects where the name is the key and the Crystal is the value
    """
    dict = {}
    for crystal in crystalArray:
        dict[crystal.name] = crystal        
    return dict 
    
def parse_nets():
    '''
        DESCRIPTION: Creates crystal object and then looks line by line for
        name description then calls buildCrystalArray and updates the crystal with the
        information in the form of arrays. 
    '''
    def buildCrystalAttributeArray(attributeName, attributeArray, lineName):
        '''
        PARAM: attributeName, attributeArray, lineName
        RETURNS: attributeArray
        DESCRIPTION: parses data from the file RCSRnets.txt by looking for spaces and EOF character
        to delimit the values into arrays
        '''
        entry = ""
        for character in lineName[len(attributeName) + 3 : ]:
            if character is not " ":
                if character is "\n":
                    attributeArray.append(entry)
                    continue           
                entry = entry + character
            elif entry is not "":
                attributeArray.append(entry)
                entry = ""
        return attributeArray
    
    filename = os.path.join(os.getcwd(), '..\\datasets\\RCSRnets.txt')
    crystalArray = []
    
    with open(filename, mode='r') as file:        
        for line in file:
            if "CRYSTAL" in line:
                crystal = Crystal()  
                                 
            elif "NAME" in line:
                name = line[7:-1]
                crystal.setName(name)
                
            elif "GROUP" in line:
                group = line[8:-1]
                crystal.setGroup(group)
                
            elif "CELL" in line:
                cellArray = []
                cellArray = buildCrystalAttributeArray("CELL", cellArray, line)
                crystal.setCell(cellArray)
                
            elif "NODE" in line:
                nodeArray = []
                nodeArray = buildCrystalAttributeArray("NODE", nodeArray, line)
                crystal.appendNodeArray(nodeArray)
                
            elif "EDGE_CENTER" in line:
                edgeCenterArray = []
                edgeCenterArray = buildCrystalAttributeArray("EDGE_CENTER", edgeCenterArray, line)
                crystal.appendEdgeCenterArray(edgeCenterArray)
                
            elif "EDGE" in line:
                edgeArray = []
                edgeArray = buildCrystalAttributeArray("EDGE", edgeArray, line)
                crystal.appendEdgeArray(edgeArray)
                
            elif "END" in line:
                crystalArray.append(crystal)
                
    return crystalArray

if __name__ == "__main__":
    parse_nets()
    
