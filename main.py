"""
There are two whole numbers:
1 < a,b <100

One scientist ("Sum") get provided with sum of mmbers, another ("Prod") get provided with product of numbers.
Both scientists know that numbers 1 < a,b <100.

Determine the numbers being based on the following dialog:

Prod: I don't know the numbers;
Sum: I know it;
Prod: then I know the numbers;
Sum: then I know the numbers too.

"""

"""
Створюю всі можливі пари множників в діапазоні від 1 < a,b < 100 та повертаю значення
"""
def search_for_all_pairs():
    search_list_pairs = [(a,b) for a in range(2, 100) for b in range (a, 100)]

    return search_list_pairs

"""
Знаходжу всі можливі добутки P=a×b та перевіряю які з них мають більше ніж одну пару (a,b).
"""
def first_condition(inner_list_numbers_):
    product_pairs = {}
    for a, b in inner_list_numbers_:
        value = a * b
        if value not in product_pairs:
            product_pairs[value] = []
        product_pairs[value].append((a, b))

    possible_prod_correct_pairs = {value: pairs for value, pairs in product_pairs.items() if len(pairs) > 1}

    return possible_prod_correct_pairs

"""
Знаходжу всі можливі суми S=a+b і залишу лише ті, які відповідають хоча б одному неоднозначному добутку.
"""
def second_condition(inner_list_numbers_, inner_list_numbers_two_):
    sum_pairs = {}
    for a, b in inner_list_numbers_:
        if a * b in inner_list_numbers_two_:
            if a + b not in sum_pairs:
                sum_pairs[a + b] = []
            sum_pairs[a + b].append((a, b))
    return sum_pairs

"""
Залишу лише ті пари, де після того, як "Sum" визначив числа, "Prod" теж зможе їх дізнатися.
"""
def third_condition(sum_pairs):
    possible_sum_correct_pairs = {value: pairs for value, pairs in sum_pairs.items() if len(pairs) == 1}
    return possible_sum_correct_pairs

"""
Виводжу всі можливі пари (a,b), які відповідають умовам задачі.
"""
def fourth_condition(sum_pairs, possible_sum):
    final_numbers_pairs = [pairs for s, pairs in sum_pairs.items() if s in possible_sum]
    return final_numbers_pairs

inner_list_numbers= search_for_all_pairs()
print(inner_list_numbers)
inner_list_numbers_one = first_condition(inner_list_numbers)
print(inner_list_numbers_one)
inner_list_numbers_two = second_condition(inner_list_numbers, inner_list_numbers_one)
print(inner_list_numbers_two)
inner_list_numbers_three = third_condition(inner_list_numbers_two)
print(inner_list_numbers_three)
inner_list_numbers_four = fourth_condition(inner_list_numbers_two, inner_list_numbers_three)
print("\n", "Final list: ", inner_list_numbers_four)


