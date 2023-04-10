class Calculator():
    
    def __init__(self, list):
        self.list = list
        self.re = 0
    
    def sum(self):
        for i in self.list:
            self.re += int(i)
        print(self.re)
        
    def avg(self):
        print(self.re/len(self.list))
        
cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()