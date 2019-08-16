
class Product:
    def UseProduct(self):
        raise NotImplementedError("UseProduct() must be defined in subclass")

class ConcreteProduct(Product):
    def UseProduct(self):
        print("Implemented in Concrete Method:Use Product")


class Creator:
    def FactoryMethod(self):
        raise NotImplementedError("FactoryMethod() Must be defined in subclass")
    def AnOperation(self):
        self.product=self.FactoryMethod();
        return self.product

class ConcreteCreator(Creator):
        def FactoryMethod(self):
            return ConcreteProduct()

prodCreator=ConcreteCreator()
prod=prodCreator.AnOperation()
prod.UseProduct()
