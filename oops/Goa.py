class goa:
    def __init__(self, name, age):
        self.name = name
        iv = int(age)
        if iv < 0:
            raise ValueError("age must be non-negative")
        self.age = iv

    def relax_on_baga_beach(self):
        print(f"{self.name} is relaxing on Baga Beach.")

    def watch_sunset_at_chapora_fort(self):
        print(f"{self.name} is watching the sunset at Chapora Fort.")

    def try_water_sports_at_calangute(self):
        print(f"{self.name} is trying water sports at Calangute.")

    def taste_goan_cuisine(self):
        print(f"{self.name} is tasting Goan cuisine (fish curry & feni).")

    def enjoy_goa_nightlife(self):
        print(f"{self.name} is enjoying Goa nightlife at Tito's/Lupos.")

    def show_tasks(self):
        print(f"{self.name} ({self.age}) did these tasks in Goa:")
        self.relax_on_baga_beach()
        self.watch_sunset_at_chapora_fort()
        self.try_water_sports_at_calangute()
        self.taste_goan_cuisine()
        self.enjoy_goa_nightlife()

if __name__ == "__main__":
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    person = goa(name, age)
    person.show_tasks()
