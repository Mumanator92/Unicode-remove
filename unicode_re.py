def re_unicode(n):
    """This function remove unicodes from  a string.

    Args:
        n (str): str
    """
    for i in n:
        if i.isalnum() or i.isspace() == True:
            print(i, end='')


re_unicode("Py&%#thon $i#s t°h|e b$e#%&s*t")