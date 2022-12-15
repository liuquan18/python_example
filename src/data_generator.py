def generatexy():
    """generate random series of x and y for plot. 

    You could add a more detailed description of the function here
    if it were more complicated than simply adding two arguments.

    Parameters:
        No parameters.

    Returns:
        float: x and y

    Examples:
        >>> randomxy(1)
        3
    """
    x = [1,2,3,4,5,6,7,8,9,10]
    radom_letters = 'claraBaley'
    y = [ord(l) for l in radom_letters]
    return x,y
