class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
        
class UpgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0
        
    def sub(self, val):
        self.value -= val
        
cal = UpgradeCalculator()
cal.add(10)
cal.sub(7)

print(cal.value)