class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type.lower()
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

        self.emoji = {
            "dog": "🐶",
            "cat": "🐱",
            "dragon": "🐉",
            "bird": "🐦",
            "bunny": "🐰",
        }.get(self.pet_type, "🐾")

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.emoji} {self.name} has eaten 🍖 Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.emoji} {self.name} took a nap 😴 Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.emoji} {self.name} played and had fun 🎾 Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.emoji} {self.name} is too tired to play 🥱")

    def dance(self):
        if self.energy >= 3:
            self.energy -= 3
            self.happiness = min(10, self.happiness + 3)
            print(f"{self.emoji} {self.name} does a happy dance! 💃🎶 Happiness +3!")
        else:
            print(f"{self.emoji} {self.name} is too tired to dance... 😔")

    def sing(self):
        print(f"{self.emoji} {self.name} sings a cute song 🎵🐾")
        self.happiness = min(10, self.happiness + 2)

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.emoji} {self.name} learned a new trick: {trick}! 🎓")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.emoji} {self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.emoji} {self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n📋 {self.emoji} Status of {self.name} the {self.pet_type.capitalize()}")
        print(f"🍗 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😄 Happiness: {self.happiness}/10")

    def get_mood(self):
        if self.happiness >= 8:
            mood = "😊 Happy"
        elif self.happiness >= 5:
            mood = "😐 Okay"
        else:
            mood = "😢 Sad"
        print(f"{self.emoji} {self.name}'s mood: {mood}")
