def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    
    a=n%10 #9
    b=(n%100)//10 # 8
    c=(n%1000)//100 # 5
    d=(n%10000)//1000 # 4
    f=(n//100000) # 1
    m=a
    if m<b:
        m=b
    if m<c:
        m=c
    if m<d:
        m=d  
    if m<f:
        m=f
    
    return m
    

print(main(14581))