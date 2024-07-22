def sales_report (sales):
    if sales > 100000.00:
        per = 0.10

    elif sales <= 100000.00:
        per = 0.05
    commission = sales * per
    nextyears = sales * 1.05
    return commission, nextyears

salesperson = input("Enter salesperson's name: ")
sales = float(input("Enter salesperson's sales: "))
commission, nextyears = sales_report(sales)
print("Salesperson's name: ", salesperson)
print("Salesperson's commission: ", commission)
print("Salesperson's next years target: ", nextyears)
