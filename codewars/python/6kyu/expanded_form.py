"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    array_caracters = str(num)
    qtd_caracters = len(array_caracters)
    sum_str = ''

    for i in range(qtd_caracters):
        if array_caracters[i] == "0":
            continue
        else:
            sum_str += array_caracters[i]
            cont = len(array_caracters) - (i + 1)

        while not cont == 0:
            sum_str += '0'
            cont -= 1

        soma = sum(int(x) for x in sum_str.split('+'))
        if not i == qtd_caracters - 1 and not soma == num:
            sum_str += ' + '

    return sum_str
