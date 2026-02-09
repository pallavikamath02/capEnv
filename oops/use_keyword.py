class myname:
    def pen(self):
        return "I have a pen"

    def use(self):
        return self.pen()

class erase:
    def rubber(self):
        return "I have a rubber"

    def use(self):
        return self.rubber()

def salt(ask):
    print(ask.use())

salt(myname()) 
salt(erase())  