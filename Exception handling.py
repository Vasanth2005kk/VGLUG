try:# TRY BLOCK
    # Prompt the user for a number and convert it to an integer
    num = int(input("Enter the number:"))
    
    # Initialize an empty list to store sums of valid combinations
    list_2 = []
    
    # Iterate over possible values of i from 1 to num
    for i in range(1, num + 1):
        # Iterate over possible values of j from 1 to i
        for j in range(1, i + 1):
            # Iterate over possible values of k from 1 to j
            for k in range(1, j + 1):
                # Check if the product of i, j, and k equals the input number
                if i * j * k == num:
                    # Print the combination found
                    print([i, j, k], "===>", end=" ")
                    # Calculate the sum of i, j, and k
                    list_1 = i + j + k
                    print(list_1)  # Print the sum
                    # Append the sum to list_2
                    list_2.append(list_1)

    # Initialize lists to store unique sums and their occurrences
    list_3 = []
    list_4 = []
    
    # Iterate through the sums in list_2
    for i in list_2:
        # If the sum is not in list_3, add it
        if i not in list_3:
            list_3.append(i)
        # If the sum is already in list_3 but not in list_4, add it to list_4
        elif i not in list_4:
            list_4.append(i)

    # Print a separator line
    print("<_______________________________________________________________>")
    
    # Iterate through unique sums in list_4
    for i in list_4:
        # Print the answer if it is not empty
        if i:
            print("answer is: ===>", i)
except ValueError as error: # EXCEPTION BLOCK OR ERROR BLOCK
    # Handle non-integer input errors
    print("ERROR ==>", error)
finally:# FINALLY BLOCK
    # Print a message indicating that the process is done
    print("Done")
