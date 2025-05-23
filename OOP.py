class Players:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age


    def setAge(self,age):
        self.age = age

    def getName(self,):
        return self.name

    def setAge(self,age):
        self.age = age

    def printPlayerInfo(self):
        print("name == ",self.name)
        print("age == ",self.age)



if __name__ == '__main__':
  player1  = Players("jonathan",31)
  player1.printPlayerInfo()

