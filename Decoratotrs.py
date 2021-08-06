# # python decorators allows extra functionality to an alredy existing function
# # it uses @ operator and are then placed on the top of the original functional
#
# @some_decorator
# def simple_func():
#     do simple stuff
#     return something
#
# def new_decorator(original_func):
#     def wrap_func():
#         print('some extra code, before the original function')
#         original_func()
#         print('some extra code, after the original function')
#     return wrap_func()
#
# @new_decorator
# def func_needs_decorator():
#     print('i want to be decorated')
#
#
# # example 2
#
# def get_doc(any_function):
#     def inner_func():
#         print(any_function.__doc__)
#         print('This is a inner function')
#     return inner_func()
#
# @get_doc
# def decoration_func():
#     """
#     i am a decorated function
#     """
#     return decoration_func

import os
os.getcwd()


