def re_unicode(n):
    """This function remove unicodes from  a string.

    Args:
        n (str): str

    >>> re_unicode("Py&%#thon $i#s t°h|e b$e#%&s*t")
    Python is the best
    """
    for i in n:
        if i.isalnum() or i.isspace() == True:
            print(i, end='')


if __name__ == "__main__":
    import doctest
    doctest.testmod()