#Question 1
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

#Question 2
print((3+10**2/2) or 70.0)

#Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    #Option D matches its reverse and is therefore a palindrome

#Question 5
def find_words(filename):
    """
    This function opens a file and counts words that start with 'un' and end with 'an'.
    :param filename: str, the name of the file containing the text.
    :return: int, the number of matches found.
    """
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  # Split each line into words based on whitespace
                for word in words:
                    if word.startswith('un') and word.endswith('an'):
                        count += 1
    except FileNotFoundError:
        print("The file was not encountered.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return count

#Question 6
list_1 = [1, 2, 3]
print("Original list:", list_1)

# Change the list
list_1.append(4)  # Add an item to the end
print("Modified list:", list_1)

Example with String (Immutable)
python
Copy
my_string = "Good Morning"
print("Original string:", string_1)

# Try to modify the string
try:
    string_1[0] = 'y'  # Attempt to change the first character
except TypeError as e:
    print("Error:", e)
Error: 'str' object does not support item assignment

#Question 7
import random

# Generate a list of 10 random numbers between 1 and 100
random_num = []
for i in range(10):
    random_num.append(random.randint(1, 100))

# Modify the list according to the specified conditions
for i in range(len(random_num)):
    if random_num[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_num[i] = random.randint(20, 30)
    elif random_num[i] < 50:
        # Replace numbers less than 50 with 'XX'
        random_num[i] = 'XX'

# Print the modified list
print(random_num)

#Question 8
def is_url_valid(url):
    """
    Checks if the passed string is a valid URL.

    Args:
    url (str): The string to check.

    Returns:
    bool: True if the string is a valid URL, False otherwise.
    """
    # Check if the URL starts with http:// or https://
    if url.startswith("http://") or url.startswith("https://"):
        # Check if there is a dot somewhere after the protocol
        if '.' in url[url.find("//") + 2:]:
            return True
    return False


# Example usage:
print(is_url_valid("http://example.com"))  # Output: True
print(is_url_valid("https://google.com"))  # Output: True
print(is_url_valid("ftp://example.com"))  # Output: False
print(is_url_valid("example.com"))  # Output: False

#Question 9
def days_since_bday(birthday):

  """

  Calculate the number of full days that have passed in whole years since the given birthday.



  Args:

  birthday (str): The birthday in "DD-MM-YYYY" format.



  Returns:

  int: The number of full days passed excluding the birth year and current year.

  """

  # Extract the year from the birthday string

  yr_of_birth = int(birthday.split('-')[2])



  # Assuming the current year is 2025

  current_yr = 2025



  # Calculate the full years passed, excluding birth year and current year

  full_yrs_passed = current_yr - yr_of_birth - 1 # Subtract 1 to exclude the current year



  # Convert full years to days (approximation, not accounting for leap years)

  days_passed = full_yrs_passed * 365 # Each year is roughly 365 days


  return days_passed

print(days_since_bday("02-02-2005"))  # Output will show days passed from the years 2005 to 2024

#Question 10
