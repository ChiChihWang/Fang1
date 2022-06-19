def DrawSortedLottoNumbers(n, m):
    
    if(n < m):
        
        print("Invalid Input")

        return 0
        
    import random
    
    lotto_numbers = list(range(1, n + 1))
    
    # Randomly Draw Numbers
    random.shuffle(lotto_numbers)
    drawn_numbers = sorted(lotto_numbers[:m])
    
    return drawn_numbers