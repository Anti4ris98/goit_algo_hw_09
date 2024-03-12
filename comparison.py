import timeit
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

amount = 113
result1 = find_coins_greedy(amount)
result2 = find_min_coins(amount)
print("Монети для суми {}: {}".format(amount, result1))
print("Монети для суми {}: {}".format(amount, result2))

print(timeit.timeit("find_coins_greedy(amount)", globals=globals(), number=1000))
print(timeit.timeit("find_min_coins(amount)", globals=globals(), number=1000))

