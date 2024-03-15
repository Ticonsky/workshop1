class Engine:
  def __init__(self, name, typ, potency, weight):
    self.name=name
    self.typ=typ
    self.potency=potency
    self.weight=weight

class Properties(Engine):
  def __init__(Engine,self, chasisA, chasisB, model, gasComsuption, year):
    self.chasis
    self.model=model
    self.gasComsuption=gasComsuption
    self.year=year
  def Chasis(chasisA,chasisB):
    x=1
    if x==1:
      Properties.chasis=chasisA
    else:
      Properties.chasis=chasisB
class Vehicle(Properties):
  def __init__(self, car, truck, yacht, motorcycle):
    self.car=car
    self.truck=truck
    self.yacht=yacht
    self.motorcycle=motorcycle
  def vehicleGasComsuption():
    Vehicle.gasComsuption=1.1*Vehicle.gasComsuption+(0.2*Vehicle.Properties.Engine.weight)-(Vehicle.Properties.chasis)
