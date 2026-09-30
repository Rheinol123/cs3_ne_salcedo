class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        if self.health > 0:
            print(f"{self.name} attacks and deals {self.damage} damage!")
            zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage!")
        if self.health <= 0:
            print(f"{self.name} died!")

class Zombie: 
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        self.distance -= 1
        print(f"{self.name} took a step closer...")

    def attack(self, plant):
        if self.health > 0:
            print(f"{self.name} attacks and deals {self.damage} damage.")
            plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage!")
        if self.health <= 0:
            print(f"{self.name} died!")

peashooter = Plant("Peashooter", 15, 15)
snow_pea = Plant("Snow Pea", 20, 10)
zombie = Zombie("Zombie", 150, 10, 3)
plants = [peashooter, snow_pea]
turn = 1

while True:

    for plant in plants:
        print(f"{plant.name}: {max(0, plant.health)} HP")
        print(f"Zombie: {max(0, zombie.health)} HP")
        print(f"Distance: {zombie.distance}")

    if zombie.health <= 0:
        print("PLANTS WIN!") 
        break

    living_plants = [plant for plant in plants if plant.health > 0]
    if len(living_plants) == 0:
        print("ZOMBIE WINS...")
        break

    for plant in plants:
        if plant.health > 0: 
            plant.attack(zombie)
        if zombie.health <= 0:
            break

    if zombie.health <= 0:
        print("PLANTS WIN!") 
        break

    living_plants = [plant for plant in plants if plant.health > 0]
    if len(living_plants) == 0:
        print("ZOMBIE WINS...")
        break

    if zombie.distance > 0:
        zombie.move()
    else:
        target = living_plants[0]
        zombie.attack(target)

    living_plants = [plant for plant in plants if plant.health > 0]
    if len(living_plants) == 0:
        print("ZOMBIE WINS...")
        break

    turn += 1
print("GAME OVER!")