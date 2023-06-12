def EditDistance(x, y):
    m, n = len(x), len(y)
    
    dp_chart = []
    for _ in range(m + 1):     #Creating empty chart
        row = [0] * (n + 1)
        dp_chart.append(row)

    for i in range(1, m + 1):  #Sets values in column 0 equal to i
        dp_chart[i][0] = i

    for j in range(1, n + 1):  #Sets values in row 0 equal to j
        dp_chart[0][j] = j

    operations = []

    for i in range(1, m + 1):                               #looping reccurence equations until we get to the last cell
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
print()

min_distance = EditDistance(x, y)
print(f"\nMinimum edit distance: {min_distance}")
