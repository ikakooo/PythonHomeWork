text = 'azcbobobegghakl'
maxAlpabeticalString = ''
AlpabeticalString = ''
for char in text:
    if (AlpabeticalString == ''):
        AlpabeticalString = char
    elif (AlpabeticalString[-1] <= char):
        AlpabeticalString += char
    elif (AlpabeticalString[-1] > char):
        if (len(maxAlpabeticalString) < len(AlpabeticalString)):
            maxAlpabeticalString = AlpabeticalString
            AlpabeticalString = char
        else:
            AlpabeticalString = char
if (len(AlpabeticalString) > len(maxAlpabeticalString)):
    maxAlpabeticalString = AlpabeticalString
print(maxAlpabeticalString)