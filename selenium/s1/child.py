from demo import Calc

class ChildImpl(Calc):
    n1 = 100
    def __init__(self,nnumber):
        Calc.__init__(self,2,10)
        self.nnumber = nnumber

    def getCompleteData(self):
        return self.n1 + self.number1 + self.number2 + self.summ()+self.nnumber


obj2 = ChildImpl(5)
print(obj2.getCompleteData())