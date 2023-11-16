class Emploree:
  def __init__( self, baseSalary, bonusHrs, sales, name):
    {
      self.baseSalary = baseSalary 
      self.bonusHrs = bonusHrs
      self.sales = sales
      self.name = name

    }
  def CalculatSalary():
  {
    retrun self.baseSalary+self.bonusHrs+self.sales+self.name 
  }
  
moha = car(23, 111, 33,355)
salary = moha.CalculatSalary()
print(salary)
