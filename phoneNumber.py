def getWordsFromPhoneNumber(phoneNumber):
    # Write your code here
    map = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": ""}
    result = []
    def helper(phonenumber, i, slate, result):
        if i == len(phonenumber):
            if len(slate) > 0:
                result.append("".join(slate))
        else:
            chars = map[phonenumber[i]]
            if chars:
                for x in chars:
                    slate.append(x)
                    helper(phonenumber, i+1, slate, result)
                    slate.pop()
            else:
                helper(phonenumber, i+1, slate, result)
    
    helper(phoneNumber, 0, [], result)
    if result:
        return result
    else:
        return ["-1"]