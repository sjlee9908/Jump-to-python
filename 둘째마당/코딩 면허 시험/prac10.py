class Calculator():
    def __init__(self, n):
        self.n=n
    def sum(self):
        return sum(self.n)
    def avg(self):
        return sum(self.n)/len(self.n)
    

cal1=Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2=Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())