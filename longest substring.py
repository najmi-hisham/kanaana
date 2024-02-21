def findMaxLen(s):
    if (len(s) <= 1):
        return 0
 
    # Initialize curMax to zero
    curMax = 0
 
    longest = [0] * (len(s))
 
    # Iterate over the string starting
    # from second index
    for i in range(1, len(s)):
        print(f"im in iteration {i}")
        if ((s[i] == ')'
             and i - longest[i - 1] - 1 >= 0
             and s[i - longest[i - 1] - 1] == '(')):
            print(f"longest: {longest}")
            print("ALL CONDITION BELOW PASS")
            print(f"1. My string is )\n2. [i - longest[i - 1] - 1]:[{i} - {longest[i - 1]} - 1]={i - longest[i - 1] - 1}\n3. s[i - longest[i - 1] - 1] or s{[i - longest[i - 1] - 1]} is {s[i - longest[i - 1] - 1]}")
             
            longest[i] = longest[i - 1] + 2 #add 2 with prev longest 
            if (i - longest[i - 1] - 2 >= 0):
                longest[i] += (longest[i - longest[i - 1] - 2]) # if there is new partner like (()) then(())
                print(f"\ni triggered the if with condition below:\n1. i({i})- longest[i - 1]({longest[i - 1]}) - 2 >= 0 :{i - longest[i - 1] - 2}")
                print(f"i will add value current longest with {longest[i - longest[i - 1] - 2]} from longest[{[i - longest[i - 1] - 2]}]")
            else:
                longest[i] += 0
                print(f"i not triggered the if i({i})- longest[i - 1]({longest[i - 1]}) - 2 >= 0 :{i - longest[i - 1] - 2}")
            curMax = max(longest[i], curMax)
            print(f"max(longest[i], curMax):max({longest[i]},{curMax})")
        print(f"longest updated: {longest}")
        print(f"curmax: {curMax}")
        print("---------------------------------------------------")
    return curMax
 
 
# Driver Code
if __name__ == '__main__':
    Str = "((()))(())"
     
    # Function call
    print(findMaxLen(Str))
 