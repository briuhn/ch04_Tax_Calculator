import CaculationModule as calc

print("Sales Tax Calculator")

def main():
    while True:
        total_cost = 0
        print()
        print("ENTER ITEMS (ENTER -99 TO END)")

        while True:
            item_cost = float(input("Cost of item: "))
            if item_cost == -99:
                break
            total_cost += item_cost


        print("Total: " + str(round(total_cost,2)))
        sales_tax = calc.calculateTotalCost(total_cost)
        print("Sales Tax: "+ str(sales_tax))
        total_after_tax = calc.calculateTax(total_cost)
        print("Total after tax: " + str(total_after_tax))

        again = input("Again? (y/n)")
        if again != 'y':
            print("Thanks bye!")
            break



if __name__ == "__main__":
    main()

          
