
class Hero:
    association = "Justice League"
    
    def __init__(self, name, power, brand, origin):
        self.name = name
        self.power = power
        self.brand = brand
        self.origin = origin

    def alterego(self):
        print(f" I am {self.name}" )
        return self
        
    def skill(self):
        print(f" I'm {self.name} my power is  {self.power}" )
        return self
        
    def comic(self):
        print(f" I'm {self.name} from {self.brand} comics" )
        return self

    def location(self):
        print(f" {self.name} is from {self.origin}" )  
        return self
        
    @classmethod
    def change_association(cls,name):
        cls.association = name
        print(" I am a member of the " + cls.association)
        return 

batman = Hero("batman", "money", "DC", "Gotham")
superman = Hero("superman", "the sun", "DC", "Metropolis")
wonderwoman = Hero("wonderwoman", "being an amazon", "DC", "Metropolis")

batman.alterego().skill().comic().location().change_association("The League of Villains")
print("")
superman.alterego().skill().comic().location().change_association("Power Rangers")
print("")
wonderwoman.alterego().skill().comic().location().change_association("The Avengers")
print("")

