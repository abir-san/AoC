dial = 50
count = 0

with open("txt_day1_advent2025") as f:
    for line in f:
        line = line.strip()

        direction = line[0]
        num = int(line[1:])
        for i in range(num):
            if direction == "L":
                dial = (dial - 1) % 100
            else:
                dial = (dial + 1) % 100

            if dial == 0:
                count += 1

print(count)