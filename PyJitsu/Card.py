from .CardElement import CardElement
from .CardColor import CardColor
class Card:
    def __init__(self, element, color, number): # TODO: Powers
        
        if not isinstance(element,CardElement):
            raise TypeError
        if not isinstance(color,CardColor):
            raise TypeError
        if not isinstance(number,int):
            raise TypeError
        
        self.element = element
        self.color = color
        self.number = number