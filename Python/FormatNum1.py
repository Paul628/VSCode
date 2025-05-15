integer = input("Enter non-negative integer  number which should not begin with zero: ")
size = len(integer)

# Created three dicts for matching numbers as keys to corresponding words
dic_ones = {1: "One ", 2: "Two ", 3: "Three ", 4: "Four ",
            5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine "}
dic_tens = {10: " Ten ", 11: "Eleven", 12: " Twelve ", 13: " Thirteen ", 14: " Fourteen ", 15: " Fifteen ", 16: " Sixteen ",
            17: " Seventeen ", 18: " Eighteen ", 19: " Nineteen "}
dic_tys = {20: " Twenty ", 30: " Thirty ", 40: " Forty ", 50: " Fifty ",
           60: " Sixty ", 70: " Seventy ", 80: " Eighty ", 90: " Ninety "}


# Created one main function digits_length within which I called functions(ones,tens,hundreds,thousands,millions,billions)
# based on the input length
def ones(num):
    print(dic_ones[num], end="")


def tens(num):
    if num//10 == 1:
        print(dic_tens[num], end="")
    elif num % 10 == 0:
        print(dic_tys[num], end="")
    else:
        print(dic_tys[num-(num % 10)], end="")
        ones(num % 10)


def hundreds(num):
    if num % 100 == 0:
        ones(num//100)
        print("Hundred ")
    else:
        ones(num//100)
        print("Hundred", end="")
        digits_length(len(str(num % 100)), num % 100)


def billions(num):
    ones(num//1000000000)
    print("Billion ", end="")
    if num % 1000000000 != 0:
        digits_length(len(str(num % 1000000000)), num % 1000000000)


def millions(num):
    digits_length(len(str(num//1000000)), num//1000000)
    print("Million", end="")
    if num % 1000000 != 0:
        digits_length(len(str(num % 1000000)), num % 1000000)


def thousands(num):
    digits_length(len(str(num//1000)), num//1000)
    print("Thousand ", end="")
    if num % 1000 != 0:
        digits_length(len(str(num % 1000)), num % 1000)


def digits_length(length, number):
    if length == 1:
        ones(number)
    elif length == 2:
        tens(number)
    elif length == 3:
        hundreds(number)
    elif 7 > length > 3:
        thousands(number)
    elif 10 > length > 7:
        millions(number)
    else:  # else applies to length 10 or billions
        billions(number)


# ones and tens are the smallest magnitudes so they do not include recursive call to digits_length
digits_length(size, int(integer))