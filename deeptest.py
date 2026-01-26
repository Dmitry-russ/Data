sales = [
    {'product': 'A', 'date': '2024-01-01', 'amount': 100},
    {'product': 'B', 'date': '2024-01-01', 'amount': 200},
    {'product': 'A', 'date': '2024-01-02', 'amount': 150},
    {'product': 'B', 'date': '2024-01-02', 'amount': 250},
    {'product': 'A', 'date': '2024-01-03', 'amount': 120},
]


def sum(sales):
    result: dict = {}
    count: dict = {}
    for line in sales:
        product = line.get("product")
        amount = line.get("amount")
        if product in result:
            result[product]["total"] = result[product]["total"] + amount
            count[product] += 1
        else:
            result[product] = {"total": 0}
            result[product]["total"] = amount
            count[product] = 0
            count[product] += 1

    overall_total = 0
    for prod in result:
        result[prod]['average'] = round(float(result[prod]['total'] / count[prod]), 2)
        overall_total += result[prod]['total']
    result['overall_total'] = overall_total
    return result


print(sum(sales))
