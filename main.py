ans = ""
def math(num1,num2,mode):
    ans = ""
    if mode == "a":
        ans = int(num1) + int(num2)
        return ans
    elif mode == "s":
        ans = int(num1) - int(num2)
        return ans
    elif mode == "m":
        ans = int(num1) * int(num2)
        return ans
