# 1. What is the function that creates Regex objects?
import re
regex = re.compile(r'')

# 2. Why are raw strings often used when creating Regex objects?
import re
regex = re.compile(r"\d+")
match = regex.search("Price: 100 dollars")
print(match.group())  

# 3. What does the search() method return?
# The search() method  returns a match object if a match is found

# 4. How do you get the actual strings that match the pattern from a Match object?
# You can get the actual matched string from a Match object using the .group() method.

# 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d), what does group 0 cover? Group 1? Group 2?

import re

pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = pattern.search("123-456-7890")

if match:
    print("Group 0:", match.group(0))  
    print("Group 1:", match.group(1))  
    print("Group 2:", match.group(2)) 

# 6. Parentheses and periods lave specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

# Parentheses () → Used for capturing groups.
# Period . → Matches any single character except a newline.
# To match them as actual characters, you need to escape them with a backslash (\).

# 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

# If your regex does not contain parentheses (), findall() returns a list of matching strings
                          
# 8. What does the | character signify in regular expressions?   

# The | in regular expressions acts as an OR operator, allowing you to match one pattern or another.

# 9. What two things does the ? character signify in regular expressions?    
# Makes the Preceding Character or Group Optional                                                                   