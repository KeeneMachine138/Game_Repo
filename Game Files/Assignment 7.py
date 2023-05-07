class Pokemon:
    def __init__(self, name, level=1, health=100, pokemon_type="Normal" ):
        self.name = name
        self.level = level
        self.health = health
        self.type = pokemon_type
    def attack(self, attackee):
        print(self.name, "Attacks",attackee.name )
        attackee.health = attackee.health - 10
    def speak(self):
        print("Pokemon sound")
        
    def __str__(self):
        return "Pokemon: {}".format(self.name)
    
class Pikachu(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, "Pikachu", 1, 100, "Electric")
    def attack(self, attackee):
        print("Pikachu used Thunderbolt on", attackee.name)
        print("It does 5 damage")
        attackee.health = attackee.health - 5
    def speak(self):
        print("Pika, Pikachu")
        
class Bulbasaur(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, "Bulbasaur", 1, 100, "Grass")
    def attack(self, attackee):
        print("Bulbasaur uses Razor Laef on",attackee.name)
        print("it does 10 damage")
        attackee.health = attackee.health - 10
    def speak(self):
        print("Bulba, Bulba, Bulbasaur")
    
class Stadium():
    def __init__(self, name, pokemon_a, pokemon_b):
        self.name = name
        self.pokemon_a = pokemon_a
        self.pokemon_b = pokemon_b
    def battle(self):
        self.pokemon_a.speak()
        self.pokemon_b.speak()
        while self.pokemon_a.health > 0 and self.pokemon_b.health > 0:
            self.pokemon_a.attack(self.pokemon_b)
            self.pokemon_b.attack(self.pokemon_a)
            print(self.pokemon_a.name,"Current health", self.pokemon_a.health)
            print(self.pokemon_b.name,"Current health:", self.pokemon_b.health)

p = Pikachu()
b = Bulbasaur()
s = Stadium("Wrestler Mania", p, b)
s.battle()


        

