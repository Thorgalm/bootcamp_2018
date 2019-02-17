from collections import OrderedDict

class Konwerter:
    dict_val = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1} \
    # dict_val = OrderDict([('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), 'XL': 40, 'X': 10,'IX': 9, 'V': 5, 'IV': 4, 'I': 1} \

    @ classmethod
    def int_to_roman(cls, num):
        if not (0 < num <= 3999):
            return "Liczba poza przedziałem"
        elif isinstance(num, int):
            result = ''
            for k, v in Konwerter.dict_val.items():
                while num >= v:
                    result += k
                    num -= v
            return result

    @ staticmethod
    def roman_to_int(rom):
        result = 0
        for i in range(len(rom)):
            if i > 0 and Konwerter.dict_val[rom[i]] > Konwerter.dict_val[rom[i - 1]]:
                result += Konwerter.dict_val[rom[i]] - 2 * Konwerter.dict_val[rom[i - 1]]
            else:
                result += Konwerter.dict_val[rom[i]]

        return result

print(Konwerter.int_to_roman(2019))
print(Konwerter.roman_to_int('MMXXVVII'))