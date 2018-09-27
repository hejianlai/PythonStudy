def cheak_kuohao(s):
    stack = []
    for char in s:
        if char in {'(','[', '{'}:
            stack.append(char)
        elif char == ')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}':
            if len(stack)>0 and stack[-1]=='{':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print(cheak_kuohao('()[]{{[]}}'))