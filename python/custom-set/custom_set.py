class CustomSet:
    def __init__(self, elements=[]):
        self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return self.elements.issubset(other.elements)

    def isdisjoint(self, other):
        return len(self.elements & other.elements) == 0

    def __eq__(self, other):
        return self.elements == other.elements

    def add(self, element):
        self.elements.add(element)
        return self

    def intersection(self, other):
        return CustomSet(self.elements & other.elements)

    def __sub__(self, other):
        self.elements = self.elements - other.elements
        return self

    def __add__(self, other):
        self.elements = self.elements | other.elements
        return self
        
