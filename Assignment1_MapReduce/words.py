def main():
    import re
    import sys
    
    if not sys.stdin.isatty():
        
        f = sys.stdin.read()
    else:
        file_name = sys.argv[1]
        f = open(file_name,"r").read()
        
    
    word = re.sub('[^a-zA-Z]',' ',f) 
    word2 = sorted(word.lower().split())
    
    
    word3 = sorted(set(word2))
    
    for i in word3:
        print(i)
        

if __name__ == '__main__':
    main()
