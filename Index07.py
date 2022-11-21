def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if n>len(s)-1:
        return False
    return s[n]

print (main("salom", 3))