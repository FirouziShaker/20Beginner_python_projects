def replace_word():
    
    print("*"*20)
    
    str="Hello all , we are here to know Germany as well as possible".lower()
   
    print(str)
    
    print("*"*20)
    
    select_word_to_replace=input("Please choose a word to replace: ").lower()
    replacement_word=input("Please say, what do you want to replace instead that: ").lower()
    new_str=str.replace(select_word_to_replace,replacement_word)
    
    print("*"*20)
    
    print(new_str)
    
    print("*"*20)

replace_word()