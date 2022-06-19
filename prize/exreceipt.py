def DrawSortedReceiptNumbers(n, m):
    
    if(n < m):
        
        print("Invalid Input")

        return 0
        
    import random
    
    receipt_numbers = list(range(1, n + 1))
    
    # Randomly Draw Numbers
    drawn_numbers = []
    
    for _ in range(0, m):
        
        drawn_numbers += [random.choice(receipt_numbers)]
    
    
    return drawn_numbers