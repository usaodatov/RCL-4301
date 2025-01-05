# Pseudocode for Assignment 1, Task 3-c (4301 - Introduction to Software Engineering)

'''

# Define the bounds for d
lower_bound = 0                                                # Minimum value of d
upper_bound = 20                                               # For demonstration purposes, higher than necessary

BEGIN                                                          # Start of the program
  FOR d FROM lower_bound TO upper_bound DO                     # Iterate over the range of d
    IF 150 - 10 * d > 30 THEN                                  # Check if d satisfies the inequality condition
      PRINT "d is valid: " + d                                 # Print value of d
    END IF                                                     # End of the condition
  END FOR                                                      # End of the loop
END                                                            # End of the program


'''


# Define the bounds
lower_bound = 0                                                # Lower bound for demonstration purposes
upper_bound = 20                                               # Upper bound for demonstration purposes

# Loop through the range
for d in range(lower_bound, upper_bound):                      # Loop through the range of d
    if 150 - 10 * d > 30:                                      # Check if the condition is satisfied
        print(f"d is valid: {d}")                              # Print valid d values

