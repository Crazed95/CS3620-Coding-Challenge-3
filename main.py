print('Part 1')
# Creating two methods for applying discounts


def number_1(x):
    return x*.9


def number_2(x):
    return x * .95


price = float(input('what is the price? '))
print(f'Original Price is {price:.2f}')
price = number_1(price)
print(f"New price after student discount {number_1(price):.2f}")

if input("Apply next 5% discount? (Y/N) : ").lower() == 'y':
    price = number_2(price)
    print(f"New price is {price:.2f}")
else:
    print(f"Final price is {price:.2f}")


print('Part 2')
print("The mathematical expression is x*(x+5)^2 where x = 5")
calc = (lambda x:x*(x+5)**2)(5)

print(f"Solution using lambda expression is: {calc:.2f}")


print("Part 3")

# list of prices
prices = [100.0, 90.0, 80.0, 70.0, 60.0]
print(f"Original list {prices}")


def discount(x):
    return x*0.9


discounted_prices = list(map(discount, prices))
print(f"New list discounted by 10% {discounted_prices}")


print("Part 4")

class Computer:
    def __init__(self,brand,specs):
        self.brand = brand
        self.specs = specs
    def getspecs(self):
        return self.specs
    def displayspecs(self):
        print(f"Brand: {self.brand}")
        print(f"Specifications: {self.specs}")


class Desktop(Computer):
    def __init__(self,brand,specs,dimensions):
        super().__init__(brand,specs)
        self.dimensions = dimensions

    def get_dimensions(self):
        return self.dimensions

    def displayspecs(self):
        super().displayspecs()
        print(f"Dimensions: {self.dimensions}")


class Laptop(Computer):
    def __init__(self, brand, specs, weight):
        super().__init__(brand, specs)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def displayspecs(self):
        super().displayspecs()
        print(f"Weight: {self.weight}")

desktop1 = Desktop("ASUS", "16GB RAM, 1TB SDD","462mm x 230mm x 466mm ")


labtop1 = Laptop("HP","16GB RAM 512 SSD","5.07lB")

desktop1.displayspecs()
labtop1.displayspecs()


print("Part 5")

class overload:
    def __init__(self,x):
        self.x = x
    def __mul__(self, other):
        return overload(self.x + other.x)

    def __str__(self):
        return str(self.x)


a = overload(3)
b = overload(15)

result = a * b

print(result)
