



proceeds = input("Enter proceeds: ")
costs = input("Enter costs: ")

proceeds = int(proceeds)
costs = int(costs)

if proceeds > costs:
    print("The proceeds of the firm exceed costs.")
    profit = proceeds - costs
    profitability = profit / proceeds
    print("Profitability is", profitability)

    count_of_employees= input("Enter the count of employees... ")

    count_of_employees = int(count_of_employees)

    profit_of_employee = profit / count_of_employees

    print("Profit of each employee is", profit_of_employee)

else:
    print("The costs of the firm exceed proceeds.")

