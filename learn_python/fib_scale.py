'''
get user_count of numbers from user
initialize user_count as starting variable

function to create fib scale


'''

user_count = int(input("How many numbers in the Fibonacci scale would you like?: " ))


scale = [1,1]

if user_count <= 1:
    scale.remove(1)
elif user_count == 2:
    pass
elif user_count >= 3:
    scale_length = len(scale) - 1
    while scale_length > user_count:
        last_item = scale[scale_length]
        second_to_last_item= scale[scale_length - 1]
        new_scale_item = second_to_last_item + last_item
        scale.append(new_scale_item)

print(scale)

        # add the last and second to last values
        # return new
