def find_coins_greedy(amount):
    denominations = [50, 20, 10, 5, 2, 1]  # доступні номінали монет
    coins_used = {}  # словник для зберігання кількості монет кожного номіналу

    for coin in denominations:
        if amount >= coin:  # якщо сума більша або рівна поточному номіналу монети
            num_coins = amount // coin  # кількість таких монет
            coins_used[coin] = num_coins  # додаємо до словника
            amount -= num_coins * coin  # віднімаємо від суми вже використану кількість монет
        if amount == 0:  # якщо сума стала рівною нулю, вихід з циклу
            break

    return coins_used

