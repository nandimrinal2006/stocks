from datetime import datetime
import pandas as pd

# Load the file
# Prompt the user for the first input and assign it to 'text_one'
print("Generate new orders as text list : ") 
input_file = input("Enter the input file name: ")

# Prompt the user for the second input and assign it to 'text_two'
output_file = input("Enter the output/processed file name: ")
  
df = pd.read_excel("order_files/"+input_file)  #input file 
orders_custom = [] 

for idx, row in df.iterrows():
    # 1. Format the date to D/M/YY
    dt = datetime.strptime(row["Date"], "%d %b %Y %I:%M:%S %p")
    date_formatted = f"{dt.day}/{dt.month}/{dt.strftime('%y')}"

    # 2. Clean numeric representations
    old_order_price = f"{row['Price']:g}"
    new_order_price = f"{round(row['New Order Price'], 2):g}" 

    order_text=f"{row['Stock']} : {row['New Order Type (Sell/Buy)']} {row['Quantity']}@{new_order_price} ({row['Order Type (Buy/Sell)']} {row['Quantity']}*{old_order_price}: {date_formatted} )"
    

    # 3. Print the formatted string
    print(
        order_text
    )
    orders_custom.append(order_text)

all_orders_text = "\n".join(orders_custom)
txt_filename = "order_files/"+output_file #output file
with open(txt_filename, "w") as f:
    f.write(all_orders_text)

print(f"Successfully saved to {txt_filename}")