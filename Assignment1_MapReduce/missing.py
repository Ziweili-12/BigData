def missing():
    import sys
    number = sys.argv[1]
    try:
        number2 = int(number)
        
        ls = sys.argv[2:]
        ls2 = list(ls[0])
        ls2 = [word for word in ls2 if word != " "]
        ls3 = []
        for i in range(len(ls2)):
            x = float(ls2[i])
            ls3.append(x)
        
        ls3_length = len(ls3)
        
        if len(ls3)==len(set(ls3)):
            
            ls4 = sorted(ls3)
            
            
            if number2==ls3_length+1:
                
                
                sum_total = (ls3_length+1)*(ls3_length+2)/2
                sum2 = sum(ls4)
                missing_value = sum_total - sum2
                print("The missing value is {}.".format(missing_value))
                
            else:
                print("The length of the input series is not correct.")
                 
                
        
        
        else:
            print("There are  duplicates in this set.")
    
    except ValueError: 
        print("The first input is not numeric.")
    
missing()    
    

