# lambda function: a small anonymous function for a one time use (throw away function)
# they take any number of arguments, but have only 1 expression
# helps keep the namespace clean and is useful with higher order functions
# sort(), map(), filter(), reduce()
# lambda parameters: expression

double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " + last
is_even = lambda x: x % 2 == 0
age_check = lambda age: True if age >= 18 else False

print(double(4))
print(add(2, 3))
print(max_value(4, 5))
print(min_value(4, 5))
print(full_name("Spongebob", "Squarepants"))
print(is_even(5))
print(age_check(21))