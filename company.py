class Company:
    def __init__(self, name, size, president, tax_id):
        self.name = name
        self.size = size
        self.president = president
        self.tax_id = tax_id

    def __repr__(self):
        return f'Company({self.name}, {self.size}, {self.president}, {self.tax_id})'

    def __hash__(self):
        return hash(self.name) + hash(self.tax_id)

    def __eq__(self, other):
        if self is other:
            return True
        elif not isinstance(other, Company):
            return False
        else:
            return self.name == other.name and \
                   self.size == other.max_size and \
                   self.president == other.president and \
                   self.tax_id == other.tax_id



companies = set()

companies.add(Company('Apple', 60000, 'Tim Cook', '493476294712248'))
companies.add(Company('Apple', 60000, 'Tim Cook', '493476294712248'))
companies.add(Company('Apple', 60000, 'Tim Cook', '493476294712248'))
companies.add(Company('Apple', 60000, 'Tim Cook', '493476294712248'))

print(companies)

# company = Company('Apple', 60000, 'Tim Cook', '493476294712248')
#
# print(id(company))
# print(hash(company))
#
# import numpy
# y = numpy.array([id(company)], dtype='int64')
# SIZEOF_VOID_P = 8
# result = (y >> 4) | (y << (8 * SIZEOF_VOID_P - 4))
# print(result[0])
