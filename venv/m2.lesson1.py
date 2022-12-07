class Human:
    head = 1
    body = 1
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
     print(f'{self.name} is run')
hum = Human('Алдияр',18)
hum.run()
print(hum.name, hum.age, hum.head)

