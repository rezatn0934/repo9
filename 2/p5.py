

def safe_int(i):
    try:
        return int(float(i))
    except:
        return None
    
    
    
if __name__ == "__main__":
    print(safe_int(input("Enter int: ")))