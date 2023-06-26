#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    i = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except Exception as e:
            if isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, TypeError):
                print("wrong type")
            elif isinstance(e, IndexError):
                print("out of range")
            result = 0
        finally:
            new.append(result)
    return new
