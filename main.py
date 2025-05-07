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
    def __init__(self, character, relationshipType):
        self.character = character
        self.relationshipType = relationshipType
        self.affection = random.randint(50, 100)  # Affection starts high

class Choice:
    def __init__(self, description, health_pct=0, happiness_pct=0, smarts_pct=0, looks_pct=0, karma_change=0, money_change = 0):
        self.description = description
        self.health_pct = health_pct
        self.happiness_pct = happiness_pct
        self.smarts_pct = smarts_pct
        self.looks_pct = looks_pct
        self.karma_change = karma_change;
        self.money_change = money_change

    def apply(self, character):
        def apply_percent(current, pct):
            return max(0, min(100, int(current + current * (pct / 100))))

        character.health = apply_percent(character.health, self.health_pct)
        character.happiness = apply_percent(character.happiness, self.happiness_pct)
        character.smarts = apply_percent(character.smarts, self.smarts_pct)
        character.looks = apply_percent(character.looks, self.looks_pct)
        character.karma = max(0, min(100, character.karma + self.karma_change))
        character.money += self.money_change

class Event:
    def __init__(self, description, choices=None, min_age=0, max_age=100):
        self.description = description
        self.choices = choices if choices else []
        self.min_age = min_age
        self.max_age = max_age

    def is_applicable(self, age):
        return self.min_age <= age <= self.max_age

    def apply(self, character):
        if not self.choices:
            print(f"Event: {self.description}")
            return

        print(f"Event: {self.description}")
        for idx, choice in enumerate(self.choices):
            print(f"{idx + 1}. {choice.description}")

        while True:
            try:
                selection = int(input("Choose an option: "))
                if 1 <= selection <= len(self.choices):
                    self.choices[selection - 1].apply(character)
                    break
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Enter a number.")

events = [
	Event(
		"Your Gums Hurt And You Need Something To Chew On, What Will you Chew?",
		[
			Choice("Chew On TV Remote", 0, 10, -5, 0, -10),
			Choice("Chew On A Rubber Chew Ring", 0, 10, 5, 0, 10)
		],
		1, 3
	),
	Event(
		"You Found 100 on the floor, What Will You Do?",
		[
			Choice("Take It", 0, 10, 0, 0, -10, 100),
			Choice("Leve It", 0, -10, 0, 0, 20),
		],
		5, 12
	),
]

class Character:
	def __init__(self, name, lastName, gender,age, health, happiness, smarts, looks):
		self.name = name
		self.lastName = lastName
		self.gender = gender
		self.age = age
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

		self.deathAge = random.randint(50, 120)

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

		possible_events = [e for e in events if e.is_applicable(self.age)]
		if possible_events:
			chosen = random.choice(possible_events)
			chosen.apply(self)

	def addRelation(self, relation):
		self.relationships.append(relation)

	def cheakDeath(self):
		if self.health < 0:
			self.alive = False
		elif self.age >= self.deathAge:
			self.alive = False

		for relation in self.relationships:
			relation.character.cheakDeath()

if __name__ == "__main__":
	print("==========WELCOME TO TEXTLIFE==========")
	# name = input("Enter The First Name of Your Character: ")
	# lastName = input("Enter The Last Name of Your Character: ")
	# gender = input("Enter The Gender of Your Character(Male/Female): ")
	name = "Yug"
	lastName = "Lodha"
	gender = "Male"
	if gender.lower() not in ["male", "female"]:
		print("Thats Not A Correct Value, Your Gender Was Randomly Selected as male")
		gender = "Male"
	# randomStats = input("Do You want random stats(Yes/No): ")
	randomStats = "Yes"
	if randomStats.lower() == "yes":
		player = Character(name, lastName, gender,0, random.randint(50,100), random.randint(50,100), random.randint(1,100), random.randint(1,100))
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
		player = Character(name, lastName, gender,0, health, happiness, smarts, looks)

	parents = random.randint(1,2)
	siblings = random.randint(0,2)

	player.printStats()

	if parents == 1:
		if random.randint(0,1) == 0:
			mother = Character(random.choice(female_names), lastName, "Female", random.randint(18, 50), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
			mother.money = random.randint(100, 5000000)
			motherRelation = Relationship(mother, "Mother")
			player.addRelation(motherRelation)
			print(f"I Have A Mother Named {mother.name.capitalize()} {mother.lastName.capitalize()}\n")
		else:
			father = Character(random.choice(male_names), lastName, "Male", random.randint(18, 50), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
			father.money = random.randint(100, 5000000)
			fatherRelation = Relationship(father, "Father")
			player.addRelation(fatherRelation)
			print(f"I Have A Father Named {father.name.capitalize()} {father.lastName.capitalize()}\n")
	elif parents == 2:
		mother = Character(random.choice(female_names), lastName, "Female", random.randint(18, 50), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
		father = Character(random.choice(male_names), lastName, "Male", random.randint(18, 50), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
		father.money = random.randint(100, 5000000)
		mother.money = int(father.money - ((10/100)*father.money))
		motherRelation = Relationship(mother, "Mother")
		fatherRelation = Relationship(father, "Father")
		player.addRelation(fatherRelation)
		player.addRelation(motherRelation)
		print(f"I Have A Mother Named {mother.name.capitalize()} {mother.lastName.capitalize()}")
		print(f"I Have A Father Named {father.name.capitalize()} {father.lastName.capitalize()}\n")

	if siblings ==1:
		if random.randint(0,1) == 0:
			sister = Character(random.choice(female_names), lastName, "Female", random.randint(1, 5), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
			sister.money = 0
			sisterRelation = Relationship(sister, "Sister")
			player.addRelation(sisterRelation)
			print(f"I Have A Sister Named {sister.name.capitalize()} {sister.lastName.capitalize()}\n")
		else:
			brother = Character(random.choice(male_names), lastName, "Male", random.randint(1, 5), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
			brother.money = 0
			brotherRelation = Relationship(brother, "Brother")
			player.addRelation(brotherRelation)
			print(f"I Have A Brother Named {brother.name.capitalize()} {brother.lastName.capitalize()}\n")
	elif siblings == 2:
		sister = Character(random.choice(female_names), lastName, "Female", random.randint(1, 5), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
		brother = Character(random.choice(male_names), lastName, "Male", random.randint(1, 5), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
		brother.money = 0
		sister.money = 0
		brotherRelation = Relationship(brother, "Brother")
		sisterRelation = Relationship(sister, "Sister")
		player.addRelation(brotherRelation)
		player.addRelation(sisterRelation)
		print(f"I Have A Sister Named {sister.name.capitalize()} {sister.lastName.capitalize()}")
		print(f"I Have A Brother Named {brother.name.capitalize()} {brother.lastName.capitalize()}\n")

	while player.alive:
		player.cheakDeath()
		print("Press 1 to Age Up")
		print("Press 2 to View Relationships")
		option = input("Enter Your Choice: ")
		print()

		if option == "1":
			player.ageUp()
			print("You Aged Up!!!")
		elif option == "2":
			i = 1
			for relationship in player.relationships:
				print(str(i) + ". " + relationship.relationshipType)
				i+=1
			chosenRelationship = int(input("Which Relationship Do You Want To View: "))
			chosenRelationship = player.relationships[chosenRelationship-1]
			chosenRelationship.character.printStats()
			print(f"Affection: {chosenRelationship.affection}")

		player.printStats()
		print()

	print(f"You Died At The Age Of {player.age}\nHere are you stats:")
	player.printStats()