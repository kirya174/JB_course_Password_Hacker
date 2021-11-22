for cost, revenue, month in zip(costs, revenues, months):
    print(month + " " + str(int(revenue)-int(cost)))
