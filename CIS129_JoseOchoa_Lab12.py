class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    def set_name(self, pet_name):
        self.name = pet_name

    def set_type(self, pet_type):
        self.type = pet_type

    def set_age(self, pet_age):
        self.age = pet_age

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age

def main():
    my_pet = Pet()

    pet_name = input("Enter your pet's name: ")
    my_pet.set_name(pet_name)

    pet_type = input("Enter your pet's type: ")
    my_pet.set_type(pet_type)

    pet_age = int(input("Enter your pet's age: "))
    my_pet.set_age(pet_age)

    print("\nYour pet's information:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_type())
    print("Age:", my_pet.get_age())

if __name__ == "__main__":
    main()