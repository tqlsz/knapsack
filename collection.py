import collections

Person = collections.namedtuple('Person', 'name age gender')
print 'Tpye of Person:', type(Person)
Bob = Person(name = 'Bob', age = 30, gender = 'male')
print 'Repreentation:', Bob
Jane = Person(name='Jane', age = 29, gender = 'female')
print 'Field by name', Jane.name, Jane[0]

for people in [Bob, Jane]:
    print "%s is %d years old %s"%people

