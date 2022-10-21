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
    if a<b or c>b or a<c:
        return b
    if b<a or c>a or b<c:
        return a
    if a<c or b>c or b>a:
        return c
print(main(3,7,1))
