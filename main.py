#print ('Hola')

#class Human:     
#  def __init__(self):
#    self.name='Nome'
#    self.age = 0
#    self.gender = 'Nome'
#  def introduce(self):
#    print('Hello, my name is', self.name)
#  def add_info(self):
#    self.name = input('Name:')
#    self.age = int (input('Age:'))
#    self.gender = input ('Gender')




#obj = Human()
#obj.introduce()
#obj.add_info()
#obj.introduce()

from random import*

class Student: 
  def __init__(self,name):
    self.name = name
    self.gladness = 50
    self.progress = 0
    self.alive = True
    
  def study(self):
    print('Study time')
    self.progress += 0.12
    self.gladness -= 5
  
    
  def sleep(self):
    prinf('Sleep time')
    self.gladness += 3
    
  def chill(self):
    print('Chill time')
    self.gladness += 5
    self.progress -= 0.1
    
  def is_alive(self):
    if self.progress < -0.5:
      print('Sooo bad')
      self.alive = False
    elif self.gladness <= 0:
      print('Depression...')
      self.alive = False
    elif self.progress > 5:
      print('Passed the exam!')  
      self.alive = False
      
  def end(self):
    print('Gladness:', self.gladness)
    print('Progress:', self.gladness)
    
  def live(self, day):
    print('Day:',day)
    live_cube =randint(1,3)
    if live_study == 1:
      self.study()
    elif live_cube == 2:
      self.sleep() 
    elif live_cube == 3:
      self.is_alive()
    self.end()
    self.is_alive()

obj = Student('Bob')

for day in range(365):
	if obj.alive == False:
		break
	obj.live(day)
