import logging

logging.basicConfig(filename='log_file.log', filemode='w',encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)

class ValueError(Exception):
    pass

class NegativeValueError(ValueError):
    def __init__ (self, w:int, h:int):        
        self.w = w
        self.h = h

    def __str__(self):
        if self.w < 0:
            return 'Ширина должна быть положительной, а не ' + str(self.w)
        elif self.h != None and self.h < 0:            
            return 'Высота должна быть положительной, а не ' + str(self.h)        

class Rectangle:
    def __init__(self, width, height=None):       
        if width < 0 or height!= None and height < 0:
            raise NegativeValueError(width, height)
        self.width = width
        if height is None: self.height = width
        else: self.height = height  

    def perimeter(self):       
        return 2 * (self.width + self.height)

    def area(self):       
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)
    
    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
if __name__ == '__main__':
    
    try: 
        rec1 = Rectangle(10, 10)        
        logger.info(rec1.__str__() + ':\n\t\t\t\tпериметр: ' + str(rec1.perimeter()) + '\n\t\t\t\tплощадь: ' + str(rec1.area()) + '\n')
        
        rec2 = Rectangle(6, 4)
        logger.info(rec2.__str__() + ':\n\t\t\t\tпериметр: ' + str(rec2.perimeter()) + '\n\t\t\t\tплощадь: ' + str(rec2.area()) + '\n')
               
        logger.info('Результат сложения двух прямоугольников: ')
        rec3 = rec1 + rec2
        logger.info(rec3.__str__()+ '\n')               
        
        logger.info('Результат вычитания двух прямоугольников: ')
        rec4 = rec1 - rec2
        logger.info(rec4.__str__() + '\n')
       
        logger.info('Результат сравнения двух прямоугольников: ')
        if rec1 > rec2:
            logger.info(rec1.__str__() + ' больше')
        else:
            logger.info(rec2.__str__() + ' больше')
            
    except NegativeValueError as e:
        logger.critical(e)