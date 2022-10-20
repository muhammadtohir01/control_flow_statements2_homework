def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    m=a
    if m>b:
        m=b
    if m>c:
        m=c
    return int(m)
print(main(1,-4,2))