#__init__() funcation is called automatically every time when the class being used to create object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
#__str__() funcation controls what should be returned when the class object is represnted as a string
p1 = Person("John", 36)

print(p1)

class Person2:
    def __init__(self,name2,age2):
        self.name2=name2
        self.age2=age2
p2=Person2(name2="mohamed",age2=55)
print(p2.name2,"(",p2.age2,")")


class Person3:
    def __init__(self, name3, age3):
        self.name3 = name3
        self.age3 = age3

    def myfun(self):
        print("Hello my name is " + self.name3 + " and my age is " + str(self.age3))

p3 = Person3("mohamed", 12)
p3.myfun()

class student:
    def __init__(self,stname):
        self.stname=stname
        self.mark=[]
        print("welcom {} in the school" .format(stname))

    def add_marks(self, mark):
        self.mark.append(mark)

    def avg(self):
        return sum(self.mark) / len(self.mark)


st=student("mohamed")
st.add_marks(40)
st.add_marks(50)
st.add_marks(60)
st.add_marks(70)
st.add_marks(80)
print(st.mark)
print(st.avg())

class claculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
    def dev(self):
        return self.x/self.y
calc=claculator(10,20)
print("Sumation = "+str(calc.add()))
print("Multiblication = " +str(calc.mul()))
print("Devation = " +str(calc.dev()))


class animal (object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("{} is eating {}" .format(self.name,food))

class dog(animal):
    def fetch(self,thing):
        print("{} get the {} " .format(self.name,thing))

class cat (animal):
    def cat_eat(self):
        print("{} is eating food".format(self.name))


class Pers:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)
class Student(Pers):
    def __init__(self, fname, lname, gradyear):
        super().__init__(fname, lname)
        self.gradyear = gradyear

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.gradyear)


s1 = Student("Mohame", "Eid", 2000)
s1.welcome()

def power(x):
    return x**2
x=power(5)
print(x)
power2=lambda x:x**2
x=power2(5)
print(x)

print((lambda x:x**2)(5))

sum1=lambda x,y:x+y
z=sum1(5,10)
print(z)
print((lambda x,y:x+y)(10,20))

class car:
    def __init__(self,colour,car_type):
        self.colour=colour
        self.car_type=car_type
    def __add__(self, other):
        return car(self.colour+"&"+other.colour,self.car_type+"&"+ other.car_type)
    def __repr__(self):
        return f"car(colour={self.colour},type={self.car_type})"
    def __str__(self):
        return f"A {self.colour}{self.car_type}"
    def __getitem__(self, item):
        if item==0:
            return self.colour
        elif item==1:
            return self.car_type
        else:
            print("Index out of range")

class CarWithPrice(car):
    def __init__(self,colour, car_type, price):
        super().__init__(colour,car_type)
        self.price=price
    def print_price(self):
        print(f"The price of this car {self.car_type} is {self.price}")

class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def get_cart_len(self):
        return len(self.cart)

    def __len__(self):
        return len(self.cart)

    def __call__(self):
        print(f"Order placed by {self.customer}")

    def __str__(self):
        cart_items = ", ".join(str(item) for item in self.cart)
        return f"{self.customer} bought: {cart_items}"

    def __repr__(self):
        return f"Order(cart={self.cart}, customer={self.customer})"

    def add_item(self, item):
        self.cart.append(item)

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    #to add from first

    def __radd__(self, other):
        new_cart=self.cart.copy()
        new_cart.inse(0,other)
        return Order(new_cart,self.customer)
    def __getitem__(self, key):
        return  self.cart[key]
    def __setitem__(self, key, value):
        self.cart[key]=value
        return self






order = Order(["laptop", "monitor"], "Mohamed Eid")
print(order.get_cart_len())  # Output: 2
print(order.customer)  # Output: Mohamed Eid
print(order.cart)  # Output: ['laptop', 'monitor']
print(len(order))  # Output: 2
print(order)  # Output: Mohamed Eid bought: laptop, monitor
print(str(order))  # Output: Mohamed Eid bought: laptop, monitor
print(repr(order))  # Output: Order(cart=['laptop', 'monitor'], customer=Mohamed Eid)
order.add_item("mouse")
print(order.cart)  # Output: ['laptop', 'monitor', 'mouse']

# Use the __add__ method to create a new order
new_order = order + "usb"
print(new_order.cart)  # Output: ['laptop', 'monitor', 'mouse', 'usb']


print(order[2])

order[1]="kkkklk"

print(order)

def sum_nums(my_list):
    res=0
    for x in my_list:
        res+=x

    return res
list_of_nums=[1,2,3,4]
print(sum_nums(list_of_nums))

def sum_num_arg(*args):
    res=0
    for x in args:
        res+=x
    return res
print(sum_num_arg(1,2,3,4,5))

def sum_key(a,b,*args,option=True):
    res=0
    if option:
        for x in args:
            res+=x
        return a+b+res
    else:
        return res
print(sum_key(1,2))
print(sum_key(1,2,3,4,5))
print(sum_key(1,2,3,4,5,option=False))

def make_sentence(**kwargs):
    res=""
    for x in kwargs.values():
        res+=x
    return res
def human_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
print(make_sentence(a="Mohamed ",b=" Eid ",c=" wahby "))
print(f"-------------")
print(human_details(name="Mohamed",job="hacker",age="22"))

def print_args(x,y,*args,option=True,**kwargs):
    print(x,y)
    print(args)
    print(option)
    print(kwargs)
print(print_args(1,2,"3 is args"," 4 is args",option=False,job="hackora",description="3ed0x92"))


def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

myGen=myGenerator()

print(next(myGen))
print(next(myGen))


for n in myGen:
    print(n)

