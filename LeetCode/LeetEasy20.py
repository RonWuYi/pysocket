def isValid(s: str) -> bool:
    ss = {"1":"(", "2":")", "3":"[", "4":"]", "5":"{", "6":"}"}
    if len(s) <= 1 or len(s)%2!=0:
        return False
    elif len(s) == 2:
        # if s[0] ==
        if s[0] == ss["1"] and s[1] == ss["2"]:
            return True
        if s[0] == ss["3"] and s[1] == ss["4"]:
            return True
        if s[0] == ss["5"] and s[1] == ss["6"]:
            return True
        return False

    else:
        for i in range(0, len(s), 2):
        # for i in s[:range(len(s)//2)]:
            if s[i] == ss["2"] or s[i] == ss["4"] or s[i] == ss["6"]:
                return False
        for i in range(0, len(s)//2, 2):

            if s[i] == ss["2"] or s[i] == ss["4"] or s[i] == ss["6"]:
                return False
            else:
                if (s[i] == ss["1"] and s[i+1] == ss["2"]) or (s[i] == ss["1"] and s[-(i+1)] == ss["2"]):
                    return True
                if (s[i] == ss["3"] and s[i+1] == ss["4"]) or (s[i] == ss["3"] and s[-(i+1)] == ss["4"]):
                    return True
                if (s[i] == ss["5"] and s[i+1] == ss["6"]) or (s[i] == ss["5"] and s[-(i+1)] == ss["6"]):
                    return True
                return False
    # # s = "()[]{}"
    # ss = {"1":"(", "2":")", "3":"[", "4":"]", "5":"{", "6":"}"}
    # if len(s) <= 1 and len(s)%2!=0:
    #     return False
    # else:
    #     for i in range(0, len(s), 2):
    #     # for i in s[:range(len(s)//2)]:
    #         if s[i] == ss["2"] or s[i] == ss["4"] or s[i] == ss["6"]:
    #             return False
    #     for i in range(0, len(s), 2):
    #     # else:
    #         if (s[i] == ss["1"] and s[i+1] == ss["2"]) or (s[i] == ss["1"] and s[-(i+1)] == ss["2"]):
    #             return True
    #         if (s[i] == ss["3"] and s[i+1] == ss["4"]) or (s[i] == ss["3"] and s[-(i+1)] == ss["4"]):
    #             return True
    #         if (s[i] == ss["5"] and s[i+1] == ss["6"]) or (s[i] == ss["5"] and s[-(i+1)] == ss["6"]):
    #             return True
    #         return False
                # for i in range(len(s)):

def isValid02(sstring):
    stack = []

    mapping = {")": "(", "}": "{", "]": "["}

    for char in sstring:
        if char in mapping:
            top_element = stack.pop() if stack else '#'

            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

                