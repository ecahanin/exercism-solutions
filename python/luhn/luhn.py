
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdecimal():
            return False
        array = list(map(int, list(self.card_num)))
        i = 2
        while i <= len(array):
            array[-i] = self.double_digit(array[-i])
            i += 2
        return sum(array) % 10 == 0

    def double_digit(self, digit):
        digit = digit * 2
        if digit > 9:
            digit -= 9
        return digit
