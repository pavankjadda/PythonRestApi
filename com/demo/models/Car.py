#self and this are same. It can be anything but it should be first paramater in method

from com.demo.models.Owner import Owner

class Car:
    def __init__(self,make,model,color,year,owner):
        self.make=make;
        self.model=model;
        self.color=color
        self.year=year;
        self.owner=owner;

    def printOwner(this):
        print("Owner:")
        print("firstName => " + this.owner.firstName);
        print("lastName => " + this.owner.lastName);
        print("email => " + this.owner.email);
        print("phone => " + this.owner.phone);
        print("");

    def printCar(this):
        print("make => " + this.make);
        print("model => " + this.model);
        print("color => " + this.color);
        print("year => " + this.year);
        this.printOwner();

print("Creating Car Objects");
print("")
owner1=Owner("Jack","Macdonals","jadaa@gma.cil","893-333-3232");
owner2=Owner("John","Doe","jdoe@gma.cil","893-333-3232");
owner3=Owner("Steve","Fofc","Fofc@gma.cil","893-333-3232");

car1=Car("Toyota","Camry","Grey","2018",owner1);
car2=Car("Toyota","Corolla","Red","2018",owner2);
car3=Car("Toyota","Rav4","Black","2019",owner3);

car1.printCar();
car1.printCar();
car1.printCar();
