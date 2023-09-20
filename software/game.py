import circuitpython_csv

#musttodo test file write
#todo make alibis a csv of contact,[clues,...]

class gamedata:
    gamenum=0
    myclue=None
    myname=None
    newclue=None
    namefile="data/myname.txt"
    gamefile="data/game1.csv"
    alibifile="data/alibis.txt"

    threats=[]
    attacks=[]
    victims=[]
    alibis=[]
    def __init__(self,gamenum=0):
        self.gamenum=gamenum
        self.read_name()
        self.read_alibis()
        self.gamefile="data/game"+str(gamenum)+".csv"
        self.read_clues()

    def check_clue(self,newclue,alibi):
        # todo: check signature
        # todo: remove duplicates in alibis
        #print(newclue,alibi)
        self.alibis.append(alibi)

#        for clue in (self.threats+self.attacks+self.victims):
#            if clue[1] == newclue: 
#                clue[3] = newclue
#                clue[4] = alibi
#                self.newclue=newclue
#                return newclue
        for j, cluetype in enumerate([self.threats,self.attacks,self.victims]):
            for i in range(self.cluecounts[j]):
                if cluetype[i][1]==newclue:
                    cluetype[i][3]=newclue
                    cluetype[i][4]=alibi
                    self.newclue=[i,j]
                    return newclue
        return False 
    
    def is_solved(self):
        #musttodo solution checking and reporting
        #for t in threats:# for t,a,v
            # for each clue
                # if clue is null append to suspects
            # if >1 suspect return false
        return True

    def read_name(self):
        #getname, if not, do oob?
        try:
            with open("data/myname.txt",'r') as file:
                self.myname=file.readline().rstrip()
                print("hello",self.myname)
        except OSError:
            print("Error reading name from data/myname.txt")
            self.myname="unknown"

    def wipe_name(self): 
        self.myname=""
        self.write_name()

    def write_name(self):
        try:
            fhandle = open("data/myname.txt", 'w')
            fhandle.write(self.myname)
            fhandle.close()
        except OSError:
            print("Error writing name file")
            return False
        return True

    def read_clues(self):
        try:
            with open(self.gamefile, 'r') as file:
                csv=circuitpython_csv.reader(file)
                threats=[]
                attacks=[]
                victims=[]
                for row in csv:
                    if row[0] == "T":self.threats.append(row)
                    elif row[0] == "A":self.attacks.append(row)
                    elif row[0] == "V":self.victims.append(row)
                    elif row[0] == "*":self.myclue=row[1]
            self.cluecounts=[len(self.threats),len(self.attacks),len(self.victims)]
            self.check_clue(self.myclue,self.myname)
        except OSError:
            print("Error reading from file:", self.gamefile)
    
    def wipe_clues(self):
        for cluetype in [self.threats,self.attacks,self.victims]:
            for clue in cluetype:
                if clue!=self.myclue:
                    clue[3]=""
                    clue[4]=""
        self.newclue=-1
        self.check_clue(self.myclue,self.myname)
        self.write_clues()

    def write_clues(self):
        #should be called every time we add a clue?
        try:
            fhandle = open(self.gamefile, 'w')
            fhandle.write("\n".join(collection))
            fhandle.close()
        except OSError:
            print("Error writing clues file:", self.gamefile)
            return False
        return True

    def read_alibis(self):
        try:
            with open("data/alibis.txt", 'r') as file:
                self.alibis = [line.strip() for line in file]
        except OSError:
            print("Error reading alibis.txt")

    def wipe_alibis(self):
        self.alibis=[self.myname]
        self.write_alibis()

    def write_alibis(self):
        try:
            fhandle = open("data/alibis.txt", 'w')
            fhandle.write("\n".join(alibis))
            fhandle.close()
        except OSError:
            print("Error writing ailbis file")
            return False
        return True

