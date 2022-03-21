class Geeks:
    def __init__(self):
        self._age = 0
        
        @property
        def age(self):
            print('getter method called')
            return self._age 
        
        @age.setter
        def age(self,a):
            if (a < 18):
                raise ValueError('Sorry your age is below eligibility creteria')
            print('setter methos called')
            self._age = a 
            
mark = Geeks()

mark.age = 19

print(mark.age)