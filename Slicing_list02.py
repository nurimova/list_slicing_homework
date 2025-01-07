def main(list1):
    """
    A list of several elements is given. Reverse this list.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[-1::-1]
s=[1,2,3,4,5,6,7,8]
print(main(s))