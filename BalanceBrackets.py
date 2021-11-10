def balance(brackes):
        stack= []               
        startingBracks = '{(['
        endBrackecks   = '])}'

        for i in brackes:
            if i in startingBracks:
                stack.append(i)
            if i in endBrackecks:
                if len(stack)==0:
                    return False
                if stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '(' and i==')':
                    stack.pop()
                elif stack[-1]=='[' and i ==']':
                    stack.pop()
                else:
                 return False
        return len(stack)==0        

print(balance('{([])}'))