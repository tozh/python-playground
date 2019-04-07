# # decorator without argument
#
#
# def show_arguements(func):
#     print("decorator calls")
#
#     def wrapper(ls):
#         print(ls)
#         return func(ls)
#     return wrapper
#
#
# @show_arguements
# def my_func(ls):
#     print('my_func called')
#
#
# # # decorator is a syntactic sugar for the command here:
# # # decorator changes the function
# # my_func = show_arguements(my_func)
#
# a = [1, 2, 3]
# my_func(a)

# decorator with arguments:
# this means your func with arguments should return a decorator

def add_elements(*added):
    def decorator(func):
        def wrapper(ls):
            for elem in added:
                ls.append(elem)
            return func(ls)
        return wrapper
    return decorator


@add_elements(5, 6, 7)
def print_list(ls):
    print(ls)


# print_list = add_elements(5, 6, 7)(print_list)

a = [1, 2, 3]
print_list(a)



