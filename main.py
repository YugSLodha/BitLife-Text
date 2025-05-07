import random

# Male names
male_names = [
    "Alexander", "Benjamin", "Charles", "Daniel", "Ethan", 
    "Frederick", "George", "Henry", "Isaac", "James", 
    "Kenneth", "Liam", "Mason", "Nathaniel", "Oliver", 
    "Patrick", "Quentin", "Robert", "Samuel", "Thomas"
]

# Female names
female_names = [
    "Amelia", "Bella", "Chloe", "Daisy", "Emma", 
    "Fiona", "Grace", "Hannah", "Isla", "Julia", 
    "Katie", "Lucy", "Mia", "Olivia", "Penelope", 
    "Quinn", "Rose", "Sophia", "Tessa", "Violet"
]

class Relationship:
    def __init__(self, character, relationship_type):
        self.character = character
        self.relationship_type = relationship_type
        self.affection = random.randint(50, 100)  # Affection starts high
        self.mutual = True  # Assume it's mutual unless proven otherwise

class Character:
	def __init__(self, name, lastName, gender, health, happiness, smarts, looks):
		self.name = name
		self.lastName = lastName
		self.gender = gender
		self.age = 0
		self.health = health
		self.happiness = happiness
		self.smarts = smarts
		self.looks = looks

		self.money = 0
		self.job = "Unemployed"
		self.education = "Uneducated"
		self.karma = 50
		self.relationships = []
		self.alive = True

	def printStats(self):
		print(f"\nName: {self.name.capitalize()} {self.lastName.capitalize()}")
		print(f"Gender: {self.gender.capitalize()}")
		print(f"Age: {self.age}")
		print(f"Health: {self.health}")
		print(f"Happiness: {self.happiness}")
		print(f"Smarts: {self.smarts}")
		print(f"Looks: {self.looks}")
		print(f"Money: ${self.money}")

	def ageUp(self):
		self.age+=1
		for relation in self.relationships:
			relation.character.ageUp()

	def addRelation(self, relation):
		self.relationships.append(relation)

if __name__ == "__main__":
	print("==========WELCOME TO TEXTLIFE==========")
	name = input("Enter The First Name of Your Character: ")
	lastName = input("Enter The Last Name of Your Character: ")
	gender = input("Enter The Gender of Your Character(Male/Female): ")
	if gender.lower() not in ["male", "female"]:
		print("Thats Not A Correct Value, Your Gender Was Randomly Selected as male")
		gender = "Male"
	randomStats = input("Do You want random stats(Yes/No): ")
	if randomStats.lower() == "yes":
		player = Character(name, lastName, gender, random.randint(50,100), random.randint(50,100), random.randint(1,100), random.randint(1,100))
	elif randomStats.lower() == "no":
		health = int(input("Enter The Health You Want(1-100): "))
		if health<1 or health>100:
			print("Thats Not A Correct Value, Your Health Was Randomly Selected")
			health = random.randint(50,100)
		happiness = int(input("Enter The Happiness You Want(1-100): "))
		if happiness<1 or happiness>100:
			print("Thats Not A Correct Value, Your Happiness Was Randomly Selected")
			happiness = random.randint(50,100)
		smarts = int(input("Enter The Smarts You Want(1-100): "))
		if smarts<1 or smarts>100:
			print("Thats Not A Correct Value, Your Smarts Was Randomly Selected")
			smarts = random.randint(1,100)
		looks = int(input("Enter The Looks You Want(1-100): "))
		if looks<1 or looks>100:
			print("Thats Not A Correct Value, Your Looks Were Randomly Selected")
			looks = random.randint(1,100)
		player = Character(name, lastName, gender, health, happiness, smarts, looks)

	parents = random.randint(1,2)
	siblings = random.randint(0,3)

	player.printStats()

	if parents == 1:
		if random.randint(0,1) == 0:
			mother = Character(random.choice(female_names), lastName, "Female", random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
			motherRelation = Relationship(mother, "Mother")
			player.addRelation(motherRelation)
			print(f"I Have A Mother Named {mother.name.capitalize()} {mother.lastName.capitalize()}")
		else:
			father = Character(random.choice(male_names), lastName, "Male", random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
			fatherRelation = Relationship(father, "Father")
			print(f"I Have A Father Named {father.name.capitalize()} {father.lastName.capitalize()}")
	elif parents == 2:
		mother = Character(random.choice(female_names), lastName, "Female", random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
		motherRelation = Relationship(mother, "Mother")
		father = Character(random.choice(male_names), lastName, "Male", random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
		fatherRelation = Relationship(father, "Father")
		player.addRelation(fatherRelation)
		player.addRelation(motherRelation)
		print(f"I Have A Mother Named {mother.name.capitalize()} {mother.lastName.capitalize()}")
		print(f"I Have A Father Named {father.name.capitalize()} {father.lastName.capitalize()}")

	while player.alive:
		print("\nPress 1 to Age Up")
		option = input("Enter Your Choice: ")

		if option == "1":
			player.ageUp()

		player.printStats()