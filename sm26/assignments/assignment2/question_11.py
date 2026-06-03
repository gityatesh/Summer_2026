paragraph='hello my name is yatesh sharma. im 20 years old. im a data science engineering student. \n i have a keen interest in machine learning and artificial intelligence. \n i also enjoy playing football and listening to music.'

with open('paragraph.txt', 'w') as doc1:
    doc1.write(paragraph)
    
with open('paragraph.txt', 'r') as doc1:
    lines = doc1.readlines()

    #now we'll print total words total lines and total characters in paragraph.txt
    totalwords = 0
    totalcharacters = 0    
    for line in lines:
        totalwords += len(line.split())
        totalcharacters += len(line)
        
    print(f'{totalcharacters}, {totalwords}, {len(lines)}')