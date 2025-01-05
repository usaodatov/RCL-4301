
# Pseudocode for Assignment 1, Task 3-b (4301 - Introduction to Software Engineering)

'''

lower_bound = -20                        // Lower bound for n for practical reasons
upper_bound = 20                         // A broader range, but the condition inside the loop limits valid n

BEGIN                                           // Start of the program
  FOR n FROM lower_bound TO upper_bound DO      // Loop to iterate over the range of n
    IF 3n + 2 < 20 THEN                         // Condition to check if n is valid
      PRINT "n is valid: " + n                  // Print the valid n
    END IF                                      // End of the condition
  END FOR                                       // End of the loop
END                                             // End of the program

'''



# Define the bounds
lower_bound = -20                               # Lower bound for demonstration purposes
upper_bound = 20                                # Upper bound for demonstration purposes

# Loop through the range
for n in range(lower_bound, upper_bound):       # Loop through the range of n
    if 3 * n + 2 < 20:                          # Check if the condition is satisfied
        print(f"n is valid: {n}")               # Print valid n values

