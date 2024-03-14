sales = {   
        'India' : 100,
        'China' : 500,
        'USA' : 800,
        'UK' : 900,
        'Japan' : 700
         }

sales_sorted_byvalues = sorted(sales.items(), key=lambda x: x[1])
print(sales_sorted_byvalues)