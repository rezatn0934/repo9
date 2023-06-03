Dict = { 0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', \
        20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
def Convert(Number):
    try:
        return Dict[Number]
    except KeyError:
        if 9 < Number < 99:
            return Convert(Number - Number % 10) + ' ' + Convert(Number % 10).lower()
        elif 99 < Number:
            return Convert(Number - Number % 100 -Number % 10) + ' ' + Convert(Number - Number % 10) + ' ' + Convert(Number % 10).lower()


def ReadFile(Path):
    with open(Path, 'r') as File:
        return File.read().split()


def WriteFile(Path, Text):
    with open(Path, 'w') as File:
        File.write(Text)


Old_Path = input("Enter Old Path:\n>>> ")
New_Path = input("Enter New Path:\n>>> ")
TextList= ReadFile(Old_Path)

for item in (TextList):
    if item.isdigit():
        TextList[TextList.index(item)] = Convert(int(item))


WriteFile(New_Path, ' '.join(TextList))

