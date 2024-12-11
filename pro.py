def cumulative_sum(lst):
    # Initialize an empty list to store cumulative sums
    cumulative_lst = []
    # Variable to keep track of running total
    total = 0

    # Loop through each element in the list
    for num in lst:
        total += num  # Add the current number to the running total
        cumulative_lst.append(total)  # Append the running total to the cumulative list
    
    return cumulative_lst

# Output
input_list = [1, 2, 3, 4, 5]
result = cumulative_sum(input_list)
print("Cumulative Sum:", result)

# description 
'''
How It Works:
First element: 1 → cumulative sum = [1]
Second element: 1 + 2 = 3 → cumulative sum = [1, 3]
Third element: 1 + 2 + 3 = 6 → cumulative sum = [1, 3, 6]
Fourth element: 1 + 2 + 3 + 4 = 10 → cumulative sum = [1, 3, 6, 10]
Fifth element: 1 + 2 + 3 + 4 + 5 = 15 → cumulative sum = [1, 3, 6, 10, 15] 
'''
