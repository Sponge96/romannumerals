ROMAN_NUMERALS = {
  "M": 1000,
  "CM": 900,
  "D": 500,
  "CD": 400,
  "C": 100,
  "XC": 90,
  "L": 50,
  "XL": 40,
  "X": 10,
  "IX": 9,
  "V": 5,
  "IV": 4,
  "I": 1
}


def run(n):

    converted = ""

    while n > 0:
        for i in ROMAN_NUMERALS:
            while n >= ROMAN_NUMERALS[i]:
                converted += str(i)
                n -= ROMAN_NUMERALS[i]


    return converted
