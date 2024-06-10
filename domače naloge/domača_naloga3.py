ovire = [(1, 3, 6),
         (2, 4, 3),
         (4, 6, 7),
         (3, 4, 9),
         (6, 9, 5),
         (9, 10, 2),
         (9, 10, 8)]

n = int(input('x koordinata '))
ovira_1 = 1000

for (x1, x2, y) in ovire:
    if x1 <= n <= x2:
        if y < ovira_1:
            ovira_1 = y



print(ovira_1)