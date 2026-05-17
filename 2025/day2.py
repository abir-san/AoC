def is_invalid(n):
    s = str(n)
    length = len(s)

    for size in range(1, length // 2 + 1):

        if length % size != 0:
            continue

        pattern = s[:size]
        repeats = length // size

        if pattern * repeats == s:
            return True

    return False


data = input().strip()

total = 0

for r in data.split(","):
    start, end = map(int, r.split("-"))

    for n in range(start, end + 1):
        if is_invalid(n):
            total += n

print(total)
