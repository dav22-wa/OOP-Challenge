from pet import Pet

def main():
    my_pet = Pet("Nia", pet_type="cat")

    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.dance()
    my_pet.train("jump")
    my_pet.train("high five")
    my_pet.sing()
    my_pet.show_tricks()
    my_pet.get_mood()
    my_pet.get_status()

if __name__ == "__main__":
    main()
