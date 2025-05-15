class FormatNumber():
    @staticmethod
    def create_maps(start=0, stop=10, skip=None, names=()):
        if skip:
            return {k: v for k, v in zip(range(start, stop, skip), names)}
        return {k: v for k, v in zip(range(start, stop), names)}

    # Created three dicts for matching numbers as keys to corresponding words
    dict_ones = create_maps(1, 10, names=["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"])

    dict_tens = create_maps(10, 20,
                            names=[" Ten ", " Eleven ", " Twelve ", " Thirteen ", " Fourteen ", " Fifteen ", " Sixteen ",
                                   " Seventeen ", " Eighteen ", " Nineteen "])
    dict_tys = create_maps(20, 100, 10,
                           names=[" Twenty ", " Thirty ", " Forty ", " Fifty ", " Sixty ", " Seventy ", " Eighty ",
                                  " Ninety "])

    def __init__(self, number):
        self.num = number

    def ones(self, num):
        print(self.dict_ones[num], end="")

    def tens(self, num):
        if num // 10 == 1:
            print(self.dict_tens[num], end="")
        elif num % 10 == 0:
            print(self.dict_tys[num], end="")
        else:
            print(self.dict_tys[num - (num % 10)], end="")
            self.ones(num % 10)

    def hundreds(self, num):
        # print(type(num))
        if num % 100 == 0:
            self.ones(num // 100)
            print(" Hundred")
        else:
            self.ones(num // 100)
            print(" Hundred", end="")
            self._format_number(num % 100)

    def billions(self, num):
        self.ones(num // 1000000000)
        print(" Billion", end="")
        if num % 1000000000 != 0:
            self._format_number(num % 1000000000)

    def millions(self, num):
        self._format_number(num // 1000000)
        print(" Million", end="")
        if num % 1000000 != 0:
            self._format_number(num % 1000000)

    def thousands(self, num):
        self._format_number(num // 1000)
        print(" Thousand", end="")
        if num % 1000 != 0:
            self._format_number(num % 1000)

    def _format_number(self, number):
        length = len(str(number))
        if length == 1:
            self.ones(number)
        elif length == 2:
            self.tens(number)
        elif length == 3:
            self.hundreds(number)
        elif 7 > length > 3:
            self.thousands(number)
        elif 10 > length > 7:
            self.millions(number)
        else:  # else applies to length 10 or billions
            self.billions(number)

    def format_number(self):
        self._format_number(self.num)


if __name__ == '__main__':
    integer = int(input("Enter non-negative integer  number which should not begin with zero: "))
    english_repr = FormatNumber(integer)
    english_repr.format_number()
