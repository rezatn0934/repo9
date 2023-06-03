

def palindrome(str1):
    str2 = str1[::-1]
    if str1 == str2:
        print("this is palindrome.")
    else:
        print("this is not palindrome.")
        
        
if __name__=="__main__":
    str1 = input("Enter your String: ").lower()
    palindrome(str1)
        