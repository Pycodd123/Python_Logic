#set variable
i = 1
#sets how many times it will repeat the pattern
while i <= 10:
    #sets how much it will increment every time i increases
    j = 1
    #makes a loop for the incremental digits 
    while j <= i:
        #makes the digits increase
        j = j+1
        #prints results
        print("*", end = "")
    #makes i higher by one at the end of the cycle    
    i = i+1
    print()

