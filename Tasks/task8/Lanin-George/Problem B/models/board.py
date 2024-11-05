class Board:

    activeList = []
    
    solutions = set([])
    
    text_file = open("Output.txt", "w")

    def appendActive(self, queen):
           self.activeList.append([queen.x, queen.y]) 

    def getActive(self):
        return self.activeList

    def removeActive(self):
        self.activeList.pop()

    def saveSolution(self):
        tmp = self.activeList.copy()
        self.solutions.add(tuple(sorted(tuple(x) for x in tmp)))
        self.text_file.write(str(tuple(sorted(tuple(x) for x in tmp))))
        self.text_file.write("\n")

    def getSolutions(self):
        return self.solutions
