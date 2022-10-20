def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and c>b and a<c:
        return b
    if b<a and c>a and b<c:
        return a
    if a<c and b>c and b>a :
        return c
print(main(2,6,4))