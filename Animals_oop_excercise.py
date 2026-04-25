class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

koira = Dog('Rekku', 1997)

print(f"Koiran nimi on {koira.name} ja hän on syntynyt vuonna {koira.birth_year}")