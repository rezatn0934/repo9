print(dict(sorted(eval(input()).items(), key=lambda x: x[-1], reverse=True)[:3]))
