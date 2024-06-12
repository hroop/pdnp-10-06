import chardet

# pip install chardet

with open('test.log', 'rb') as f:
    lines = f.read()

print(lines)  # b'Nadpisane\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'
# \xc5 bajt zapisany szesnastkowo
result = chardet.detect(lines)
print(result)  # {'encoding': 'Windows-1254', 'confidence': 0.6658130518007462, 'language': 'Turkish'}
# przy większej próbce jest ok
# {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
