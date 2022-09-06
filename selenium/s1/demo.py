

class Calc:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def getData(self):
        print(f'number 1 {self.number1} number 2 {self.number2} ')

    def summ(self):
        return self.number1 + self.number2

object = Calc(5,8)
object.getData()
print(object.summ())