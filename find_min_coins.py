def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 20, 50]  # доступні номінали монет
    min_coins = {i: float('inf') for i in range(amount + 1)}  # ініціалізація з нескінченностями
    min_coins[0] = 0  # для суми 0 мінімальна кількість монет дорівнює 0
    used_coins = {}  # словник для зберігання кількості монет кожного номіналу

    for i in range(1, amount + 1):
        for coin in denominations:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    used_coins[i] = coin  # зберігаємо номінал монети, яка була використана

    # Повторно відтворюємо використані монети
    i = amount
    coins_count = {}
    while i > 0:
        coin = used_coins[i]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        i -= coin  # віднімаємо номінал монети від поточної суми

    return coins_count

