##########
### The below Python code is copyrighted by Lusi Yang. ###
### Contact: lusiyang@gmail.com or lusi.yang@mail.utoronto.ca ###
### About: Simulated a chicken farm for my cats
### Copyright © 2017 ###
##########

# Chicken Production
class Chicken:
    total_eggs = 0.0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0.0
    
    def lay_egg(self, amount):
        self.eggs += amount
        Chicken.total_eggs += amount
        return self.eggs

# Chicken Data
c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")

# Egg Laying Process
Chicken.total_eggs
c1.lay_egg(3) # Chicken mama 1 had 3 eggs
Chicken.total_eggs # Total eggs become 3
c2.lay_egg(1) # Chicken mama 2 had 1 egg
Chicken.total_eggs # Total eggs become 4
c2.lay_egg(1) # Chicken mama 2 had another egg
Chicken.total_eggs # Total eggs become 5

