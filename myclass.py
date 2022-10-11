class myclass:
    val = 25
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print('The entered values are {} and {}'.format(self.a,self.b))

    def mult(self):
        c = self.a * self.b
        print('The multiplication = ' + str(c))

    def sum(self):

        c = self.a + self.b
        print('The sum = ' + str(c))



my = myclass(5,6)
print(my.val)
 
my.mult()
my.sum()
