

def case_sensetive(string):
    lower_case = 0
    upper_case = 0
    for char in string:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
    return upper_case, lower_case


if __name__ == "__main__":
    String = input("Enter a string:\n>>> ")
    Upper, Lower = case_sensetive(String)
    print(f"Number of uppercase char:{Lower}\nNumber of uppercase char: {Upper}")
