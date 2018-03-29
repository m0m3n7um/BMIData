
import math
import matplotlib.pyplot as plt

class Person:
  
  def __init__(self,age,weight,BMIList,NBMIList):
    self.age = age
    self.weight = weight
    self.BMI = self.BMIcount(BMIList)
    self.NBMI = self.NBMIcount(NBMIList)
    
  def __str__(self):
    return str(self.age) + " " + str(self.weight) + " " + str(self.BMI) + " " + str(self.NBMI)
    
    
  def BMIcount(self,list):
    return ((float(list[0])/float((float(list[1]))**2)) * 703)
    
  
  def NBMIcount(self,list):
    return (float(-110) + (1.34 * float(list[0])) + (1.54 * float(list[1])) + (1.2 * float(list[2])) + (1.11 * float(list[3])) + (1.15 * float(list[4])) + (0.177 * float(list[5])))
    
class Population:
  
  def __init__(self,file):
    self.population = self.gatherinfo(file)
    self.slope = 0
    self.yint = 0
    self.corr1 = self.correlation([x.age for x in self.population], [y.BMI for y in self.population])
    self.plot1 = self.plot([x.age for x in self.population], [y.BMI for y in self.population], 'ro', 211)
    self.corr2 = self.correlation([x.weight for x in self.population], [y.NBMI for y in self.population])
    self.plot2 = self.plot([x.weight for x in self.population], [y.NBMI for y in self.population], 'ro', 212)

    
  def __str__(self):
    out = [str(c) for c in self.population]
    return str(out)
    
  def gatherinfo(self,file):
    population = []
    for line in file:
      currentinfo = line.split()
      p = (Person(currentinfo[21],currentinfo[22],[currentinfo[21],currentinfo[23]],[currentinfo[5],currentinfo[4],currentinfo[3],currentinfo[20],currentinfo[19],currentinfo[23]]))
      population.append(p)
    return population
    
  def correlation(self,xlist,ylist):
    N = len(xlist)
    zipped = zip(xlist,ylist)
    sumXY = 0
    sumX = 0
    sumY = 0
    sumXsq = 0
    sumYsq = 0
    for product in zipped:
      sumXY += float(product[0]) * float(product[1])
    for x in xlist:
      sumX += float(x)
      sumXsq += float(x)**2
    for y in ylist:
      sumY += float(y)
      sumYsq += float(y)**2
    self.slope = (N*sumXY - (sumX*sumY))/(N*sumXsq - (sumX**2))
    self.yint = (sumY - (self.slope*sumX)) / N
    corr = (N*sumXY - (sumX*sumY)) / math.sqrt((N*sumXsq - (sumX**2)) * (N*sumYsq - (sumY**2)))
    return corr
    
  def plot(self, xlist, ylist,color,position):
    plt.subplot(position)
    plt.plot(xlist,ylist,color)
    plt.plot([x for x in xlist], [(self.slope * float(x) + self.yint) for x in xlist], '--')
    plt.show()
    
input = open('Input.txt', 'r')
text = input.readlines()
lines = [x.strip("\n") for x in text]
poptest = Population(lines)
print (poptest.corr1)
print (poptest.corr2)
