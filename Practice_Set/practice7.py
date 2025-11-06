# Count word occurences in a paragraph using dictionary.
paragraph=str(input("Enter a paragraphs:"))
paragraph=paragraph.lower()
for ch in ".,!?":
    paragraph=paragraph.replace(ch," ")

words=paragraph.split()
dict={}
for word in words:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(f"Dictionary:{dict}")


