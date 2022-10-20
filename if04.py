def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    m=a
    if m<b:
        m=b
    if m==a==b:
        m=0

    return int(m) 
print(main(3,3))