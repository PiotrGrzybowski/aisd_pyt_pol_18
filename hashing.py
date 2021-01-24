from structures.hash_tables import random_str


class Company:
    def __init__(self, name, size, president, tax_id):
        self.name = name
        self.size = size
        self.president = president
        self.tax_id = tax_id

    def __hash__(self):
        return hash(self.name) + hash(self.tax_id)

    # def __eq__(self, company):
    #     pass


d = {}

d['Piotr'] = 12
d[(1, 2)] = 3

value = 12
print(id(value))
d[value] = "liczba"
value += 2
print(id(value))

print(d)

companies = set()
company = Company('Apple', 60000, 'Tim Cook', '493476294712248')
companies.add(company)

print(company in companies)
print(Company('Apple', 60000, 'Tim Cook', '493476294712248') in companies)

names = set()
n1 = "Piotr"
names.add(n1)
n2 = "Piotr"
print(n2 in names)

print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')

print(id(n1))
print(id(n2))