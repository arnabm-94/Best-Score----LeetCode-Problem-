'''
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

'''
#Solution : 1

def first_second(my_list):
    # TODO
    # Convert the list to a set to remove duplicates
    unique_scores = set(my_list)
    
    # Sort the unique scores in descending order
    sorted_scores = sorted(unique_scores, reverse=True)
    
    # Get the first and second highest scores
    first = sorted_scores[0]
    second = sorted_scores[1]
    
    return first, second

# Example usage
myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(myList))  # Output: (90, 87)

####################################################################

#Solution : 2   #LeetCode Solution 

#Define a function called first_second that takes a list called my_list as an argument.
def first_second(my_list):

#Initialize two variables max1 and max2 to store the first and second best scores. 
#Set their initial values to negative infinity.
    max1, max2 = float('-inf'), float('-inf')
 
#Start a for loop that iterates through each element in my_list.
    for num in my_list:

#Check if the current element is greater than max1.
        if num > max1:

#If the current element is greater than max1, update max2 to the current value of max1.
            max2 = max1

#Set max1 to the current element, as it is now the highest value found so far.
            max1 = num

#If the current element is greater than max2 but not equal to max1, update max2.
        elif num > max2 and num != max1:

#Set max2 to the current element, as it is now the second-highest value found so far.
            max2 = num
 
#After the for loop is done, return the first and second best scores as a tuple.
    return max1, max2
 
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)

'''
#Time complexity:

The function iterates through the list my_list once, with each iteration taking constant time O(1) to perform comparisons and updates. 
Since there are n elements in the list, the overall time complexity of the function is O(n).

#Space complexity:

The function uses a constant amount of additional space to store the variables max1 and max2. 
There are no other data structures or variables created that depend on the size of the input list. 
Therefore, the space complexity is O(1), as it remains constant regardless of the input size.
'''
