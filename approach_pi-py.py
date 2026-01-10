# pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    
import time
def approach_pi(n_terms):
    start_time = time.time()
    pi_quarter = 0
    sign = 1
    divisor = 1
    
    for _ in range(n_terms):
        pi_quarter += sign * (1 / divisor)
        sign *= -1  
        divisor += 2
    
    aproximation = 4 * pi_quarter
    end_time = time.time()
    print(f'Aproximation of PI: {aproximation}')
    print(f'Time: {end_time - start_time} seconds.')
        
    return aproximation
    

approach_pi(100000000)