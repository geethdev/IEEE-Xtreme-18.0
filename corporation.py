from fractions import Fraction
import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2

    salaries = list(map(int, data[idx:idx + N]))
    happiness = [0] * N 
    idx += N

    results = []

    def range_update(l, r, c, type):
        for i in range(l, r + 1):
            if type == 0:  
                if salaries[i] != c:
                    if salaries[i] < c:
                        happiness[i] += 1
                    elif salaries[i] > c:
                        happiness[i] -= 1
                    salaries[i] = c
            elif type == 1:  
                new_salary = salaries[i] + c
                if new_salary > salaries[i]:
                    happiness[i] += 1
                elif new_salary < salaries[i]:
                    happiness[i] -= 1
                salaries[i] = new_salary

    def range_query_salary(l, r):
        total_salary = sum(salaries[l:r + 1])
        count = r - l + 1
        return Fraction(total_salary, count)

    def range_query_happiness(l, r):
        total_happiness = sum(happiness[l:r + 1])
        count = r - l + 1
        return Fraction(total_happiness, count)

    for _ in range(Q):
        qtype = int(data[idx])
        l = int(data[idx + 1]) - 1
        r = int(data[idx + 2]) - 1
        idx += 3

        if qtype == 0 or qtype == 1:
            c = int(data[idx])
            idx += 1
            range_update(l, r, c, qtype)
        elif qtype == 2:
            avg_salary = range_query_salary(l, r)
            results.append(f"{avg_salary.numerator}/{avg_salary.denominator}")
        elif qtype == 3:
            avg_happiness = range_query_happiness(l, r)
            results.append(f"{avg_happiness.numerator}/{avg_happiness.denominator}")

    print("\n".join(results))

solve()