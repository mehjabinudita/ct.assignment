total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break  
    
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the average if numbers were entered
if count > 0:
    average = total / count
    print(f"Sum: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
else:
    print("No numbers were entered.")