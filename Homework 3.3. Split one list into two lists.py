def split_list(lst):
    # Якщо список порожній
    if len(lst) == 0:
        return [[], []]

    # Знаходимо середину (якщо непарна кількість елементів – перший список більший)
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]


# 🔹 Перевірка на прикладах
print(split_list([1, 2, 3, 4, 5, 6]))   # [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))            # [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))      # [[1, 2, 3], [4, 5]]
print(split_list([1]))                  # [[1], []]
print(split_list([]))                   # [[], []]
