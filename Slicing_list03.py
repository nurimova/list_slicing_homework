def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return  list1[-1::-1]
s=['a','b','c','d','i','f','g','h','j']
print(main(s))