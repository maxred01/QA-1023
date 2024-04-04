class Cat:
    def meow(self, number_of_meow):
        print("Meow" * number_of_meow)
        return number_of_meow

    def sleep(self, hours):
        print(f"The cat is sleeping for {hours} hours.")


CAT = Cat().meow(42)
