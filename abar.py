import re
text="I am learning Python"
result=re.search("python",text)
if result:
    print("Found")
else:
    print("Not found")
