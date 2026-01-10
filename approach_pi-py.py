# pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    
    
def approach_pi(n_terms):
    pi_quarter = 0
    sign = 1
    divisor = 1
    
    for _ in range(n_terms):
        pi_quarter += sign * (1 / divisor)
        sign *= -1  
        divisor += 2
        
    return 4 * pi_quarter
    

print(approach_pi(100000000))