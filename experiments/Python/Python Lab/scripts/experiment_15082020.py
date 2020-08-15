import itertools as it

# Experiment 1
forward = "Hello world!"
backward = forward[::-1]

print("- Experiment: 1")
print("     Forward:", forward)
print("     Backward:", backward)
print("")

# Experiment 2
array = [2, 4, 8, 16, 32]
var_a, var_b, var_c, var_d, var_e = array
print("- Experiment: 2")
print("     Array:", array)
print("     var_a =", var_a)
print("     var_b =", var_b)
print("     var_c =", var_c)
print("     var_d =", var_d)
print("     var_e =", var_e)
print("")

# Experiment 3
array_a = [[1, 3], [5, 7, 9], [0, 2, 4, 6, 8]]
array_b = list(it.chain.from_iterable(array_a))
print("- Experiment: 3")
print("     array_A :", array_a)
print("     array_B :", array_b)
print("")

# Experiment 4
var_a, *var_b, var_c, var_d = [1, 2, 3, 4, 5, 6]
print("- Experiment: 4")
print("     var_a = ", var_a)
print("     var_b = ", var_b)
print("     var_c = ", var_c)
print("     var_d = ", var_d)
print("")

# Experiment 5
array = [1, 3, 5, 7, 9]
print("- Experiment: 5")
for index, value in enumerate(array):
    print("     index = ", index, ", value=", value)
print("")

# Experiment 6
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
last_three = slice(-5, None)
print("- Experiment: 6")
print("     Expression = ", last_three)
print("     Value = ", array[last_three])
print("")

# Experiment 7
closure = (x ** 2 for x in range(10))
print("- Experiment: 7")
print("     Closure:", closure)
print("     Next", next(closure))
print("     Next", next(closure))
print("")
