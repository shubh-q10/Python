'''
Given the data of student marks in the format of list of tuples of format (rollno:str, marks:int), write a function to filter student roll numbers based on the following criteria:

    • 'above_average': Students with marks above or equal to the average.

    • 'below_average': Students with marks below the average.

    • 'fail': Students with marks less than 40.

    • 'toppers': Students with marks 90 or above.

    • None: Return all roll numbers.

    • Any other value should return None.

The order of the roll numbers in the filtered roll numbers should be same as they appear in the data.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

Example

data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]
print(get_roll_nos(data, 'above_average'))  # Output: ["101", "102", "104"]
print(get_roll_nos(data, 'fail'))           # Output: ["105"]
print(get_roll_nos(data, 'toppers'))         # Output: ["104"]
print(get_roll_nos(data))                   # Output: ["101", "102",
'''




data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]

def get_roll_nos(data:list, criteria=None):
    avg = sum(marks for _, marks in data)/len(data) #here each tuple has to value and we want second value which is marks so, to ignore the first value we use _
    result = []
    
    for roll, marks in data: #here each tuple have two element so we are using two names for each
        if criteria == "above_average" and marks >= avg:
            result.append(roll)
        elif criteria == "below_average" and marks < avg:
            result.append(roll)
        elif criteria == "fail" and marks < 40:
            result.append(roll)
        elif criteria == "toppers" and marks >= 90:
            result.append(roll)
        elif criteria is None:
            result.append(roll)
            
    if criteria not in ("above_average", "below_average", "fail", "toppers", None):
        return None
    
    return result
        
    
        
print(get_roll_nos(data, 'above_average'))
        
        
        
            
        
        
        
    
    
