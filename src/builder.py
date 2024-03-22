import abc

class Car:
    def __init__(self) -> None:
        self.engine = None


class Manual:
    pass

class Builder(abc.ABC):
    """Abistract class"""
    @abc.abstractmethod
    def reset(self):
        pass

    # @abc.abstractmethod
    # def set_seats(self):
    #     pass

    @abc.abstractmethod
    def set_engine(self, engine: str):
        pass

    # @abc.abstractmethod
    # def set_trip_computer(self):
    #     pass

    # @abc.abstractmethod
    # def set_GPS(self):
    #     pass

    @abc.abstractmethod
    def get_product(self):
        pass


class CarBuilder(Builder):
    """Classe responsável por criar o objeto carro"""
    def __init__(self) -> None:
        self.car: Car = None
        self.reset()

    def reset(self):
        self.car = Car()

    def set_engine(self, engine: str) -> None:
        """Diz qual o motor do carro
        
        Parameters:
            engine: Modelo do motor
        
        Returns:
            None:
        """
        self.car.engine = engine

    def get_product(self) -> Car:
        car = self.car
        self.reset()
        return car


class Director:
    """O diretor serve para criar o objetos complexos

    ```python
    >>> d = Director()
    >>> c = CarBuilder()
    >>> d.make(c)
    >>> p = c.get_product()
    >>> print(p.engine)
    ```
    """
    def make(self, builder: Builder):
        """Cria o objeto"""
        builder.set_engine("V8")


d = Director()
c = CarBuilder()

d.make(c)
p = c.get_product()

print(p.engine)
