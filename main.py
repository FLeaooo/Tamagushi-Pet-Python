from random import randrange
import random
"""
Atributos = Nome, Fome, Felicidade, Words
Metodos = feed, Brincar, ensinar, Pegar dados, passar o tempo
"""


class Pet():
    food_max = 10
    exciment_max = 10
    words = ['Yep Yep', 'Inhame Inhame...', 'Uhuuuu...', 'Hmmmm...']
    
    def __init__(self, name, type_animal):
        self.day = 1
        self.name = name
        self.type = type_animal
        self.food = 10
        self.exciment = 10
        self.words = self.words[:]
        
    @property
    def clock(self):
        self.day += 1
        self.food -= 1
        self.exciment -= 1
        self.mood
        
    @property
    def mood(self):
        health = self.check_health()
        if health <= 0:
            print(f"{self.name} morreu")
        elif health <= 3:
            print(f"{self.name} esta muito doente")
        elif health <= 5:
            print(f"{self.name} esta cansado")
        elif health <= 8:
            print(f"{self.name} esta bem")
        else:
            print(f"{self.name} esta maravilhosamente bem")
        
    def check_health(self):
        return float(self.food + self.exciment) / 2.0
            
    def talk(self):
        lista = random.sample(self.words, len(self.words))
        print(f"{self.name} falou {lista[0]}")
    
    def wise(self):
        return len(self.words)
        
    def feed(self):
        self.food += randrange(1, 5)
        if self.food >= self.food_max:
            self.food = 10
            print("I am full")
        else:
            print("Im still hungry")
        self.clock
            
    def play(self):
        self.exciment += randrange(1, 5)
        if self.exciment >= self.food_max:
            self.exciment = 10
            print("I am happy")
        else:
            print("Im still want play")
        self.clock
            
    def teach(self, word):
        self.words.append(word)
        print("Yep, I learn something new")
        self.clock
        
    def __str__(self):
        return (f"Name:{self.name}\nWise:{self.wise()}\nHungry:{self.food}"
                f"\nExciment{self.exciment}\nHealth:{self.check_health()}\nDays:{self.day}")
        
    
def main():
    name_pet = input("Name the pet:")
    type_pet = input("What is the type of the pet:")
    
    pet = Pet(name_pet, type_pet)
    
    choice = 1 
    print(
            """
            Intereja com seu pet
            
            1-Alimentar 
            2-Brincar
            3-Ensinar
            4-Conversar 
            5-Checar humor
            6-Checar atributos
            7-Sair para beber
            0-Quit
            """
        )
    while choice != 0:
        
        choice = int(input("Choice: "))
        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            word = input("Insert the new word:")
            pet.teach(word)
        elif choice == 4:
            pet.talk()
        elif choice == 5:
            pet.mood
        elif choice == 6:
            print(pet)
        elif choice == 7:
            while True:
                acao = int(input("1-Voltar pra casa\n2-Tomar uma\nR:"))
                pet.clock
                if acao == 1:
                    break
                if acao == 2:
                    print("-Essa ta boa!!!")
            
            
        
main()