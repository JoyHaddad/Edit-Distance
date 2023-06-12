def minDistance(x, y):
    m, n = len(x), len(y)
    
    dp_chart = []
    for _ in range(m + 1):
        row = [0] * (n + 1)
        dp_chart.append(row)


    for i in range(1, m + 1):
        dp_chart[i][0] = i

    for j in range(1, n + 1):
        dp_chart[0][j] = j

    operations = []

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp_chart[i][j] = dp_chart[i - 1][j - 1]
            else:
                dp_chart[i][j] = min(dp_chart[i - 1][j - 1], dp_chart[i - 1][j], dp_chart[i][j - 1]) + 1
                if dp_chart[i][j] == dp_chart[i - 1][j - 1] + 1:
                    operations.append(f"Substitute \"{x[i - 1]}\" into \"{y[j - 1]}\"")
                elif dp_chart[i][j] == dp_chart[i - 1][j] + 1:
                    operations.append(f"Delete \"{x[i - 1]}\"")
                elif dp_chart[i][j] == dp_chart[i][j - 1] + 1:
                    operations.append(f"Insert \"{y[j - 1]}\"")

    for op in operations:
        print(op)

    return dp_chart[m][n]

# User input for x and y
x = input("Enter the first word: ")
y = input("Enter the second word: ")

min_distance = minDistance(x, y)
print(f"Minimum edit distance: {min_distance}")
