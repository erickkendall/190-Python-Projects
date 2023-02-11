from faker import Faker
fake = Faker()

# List all available data sets
# for i in dir(fake):
#    print(i)

print(fake.name())

for _ in range(10):
    print(fake.name())
    print(fake.address())
    print('\n')

print(fake.text())
