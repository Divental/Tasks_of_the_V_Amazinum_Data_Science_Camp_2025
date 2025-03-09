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
Вибираю
"""
def first_condition(inner_list_numbers):
    product_to_pairs = {}
    for a, b in inner_list_numbers:
        product = a * b
        if product not in product_to_pairs:
            product_to_pairs[product] = []
        product_to_pairs[product].append((a, b))

    possible_prod_correct_pairs = {product: pairs for product, pairs in product_to_pairs.items() if len(pairs) > 1}

    return possible_prod_correct_pairs

def second_condition(inner_list_numbers, inner_list_numbers_two):
    sum_to_pairs = {}
    for a, b in inner_list_numbers:
        if a * b in inner_list_numbers_two:
            if a + b not in sum_to_pairs:
                sum_to_pairs[a + b] = []
            sum_to_pairs[a + b].append((a, b))
    return sum_to_pairs

def third_condition(sum_to_pairs):
    possible_sum_correct_pairs = {product: pairs for product, pairs in sum_to_pairs.items() if len(pairs) == 1}
    return possible_sum_correct_pairs

def fourth_condition(sum_to_pairs, possible_sums):
    final_pairs = [pairs[0] for s, pairs in sum_to_pairs.items() if s in possible_sums]
    return final_pairs


inner_list_numbers= search_for_all_pairs()
print(inner_list_numbers)
inner_list_numbers_one = first_condition(inner_list_numbers)
print(inner_list_numbers_one)
inner_list_numbers_two = second_condition(inner_list_numbers, inner_list_numbers_one)
print(inner_list_numbers_two)
inner_list_numbers_three = third_condition(inner_list_numbers_two)
print(inner_list_numbers_three)
inner_list_numbers_four = fourth_condition(inner_list_numbers_two, inner_list_numbers_three)
print(inner_list_numbers_four)


