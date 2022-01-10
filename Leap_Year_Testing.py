# This program will check and test if a year is Leap or not.

# Function setup
def is_year_leap(year):
    
    # Math's condition to tell if a year is a Leap Year or not.
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    
    # If conditions are not met, return False
    else:
        return False

# Test Time!

# Given YEARS!
test_data = [1900, 2000, 2016, 1987]

# Given expected results!
test_results = [False, True, True, False]

# For each item in test_data
for i in range(len(test_data)):
	yr = test_data[i]
    
    # Show-me the output this way:...
    # '1900 -> Failed', or...
    # ...'1900 -> Ok'
	print(yr,"->",end="")
    
    # Checking if the year is a leap year
	result = is_year_leap(yr)
    
    # Outputs must be 'Failed' for...
    # ...not corresponding results in test_data[i] and test_results[j]
    # 1900 is not a Leap year, thus might be False
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")