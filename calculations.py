from basics import mean, error

numbers_list = [1, 7, 3, 11, 41]
# mean_list = [1.2, 0.14, 2.56, .008]
result = error(mean(numbers_list), numbers_list)

print("Starting with list of numbers: ", numbers_list)
print("The mean is:", mean(numbers_list))
print("The error is:", result)
