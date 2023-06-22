import csv

def main():

    # declare a csv_list [] to store the csv
    list = []

    # first, open the file to read over
    # TODO remove "/Pybank" below
    # only using this filename temporarily for the debugger
    with open('./Resources/budget_data.csv') as file:
        reader = csv.DictReader(file)
            # TODO Successfully store header row - Why?
            # this append loop will successfully re-write the headers anyway
            # maybe that's all they mean in the instructions?
        header = reader.fieldnames
        for row in reader:
                list.append(row)

    do_stuff(list)


def do_stuff(info):
    
    # declare variables
    month_count = 0
    net_profit = 0
    change = 0
    increase = 0
    decrease = 0

    # For loop to column_length
    for dict in info:
         
         # grab values for current row's cells
         monthly_profit = int(list(dict.values())[1])
         date = str(list(dict.values())[0])

         net_profit = net_profit + monthly_profit
         
         if month_count == 0:
            last_month = monthly_profit
            total_change = monthly_profit
            month_count += 1
         else:
            current_month = monthly_profit
            change = current_month - last_month
            last_month = monthly_profit
            total_change = total_change + change
            month_count +=1

         if change > increase:
            increase = change
            increase_date = date
         if change < decrease:
             decrease = change
             decrease_date = date

            # change_from_last_month = current_month_profit - last_month_profit
            # net_profit = net_profit + profit
    
    # TODO
    # Average change calculation
        # Is this just net_profit/month_count?
        # Or average 

    # pass these values to print_output
    # return average of changes in profit/losses over time
    # return greatest increase in profits (date and amount)
    # return greatest decrease in profits (date and amount)
    average = total_change / month_count
    print(increase_date)
    print(decrease_date)
    print(total_change)
    print(average)
    # TODO
    #ensure the variables are passed correctly to print_output
    months = month_count
    total_change = net_profit
    avg_change = "TODO"
    increase = f"{increase_date} (${increase})"
    decrease = f"{decrease_date} (${decrease})"
    # call function to print results to terminal
    print_output(months, total_change, avg_change, increase, decrease)

    # TODO
    # export results to text file with results
        #open a new file, write results, save to analysis folder

# prints everything to terminal
def print_output(months, total_change, avg_change, increase, decrease):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_change}")
    print("Average Change:", avg_change)
    print("Greatest Increase in Profits:", increase)
    print("Greatest Decrease in Profits:", decrease)


main()