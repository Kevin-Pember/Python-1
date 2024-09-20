userIn = input("Please enter some text: \n")
if(userIn.startswith("Dear")):
    print("Formal letter.")
if(userIn.endswith("?") or "help" in userIn):
    print("Request for help.")
pythonMention = userIn.count("Python")
print("The word 'Python' appears",pythonMention,"time(s). ")
programIndex = userIn.find("programming")
if(programIndex != -1):
    print("The word 'programming' starts at index",programIndex,". ")
else:
    print("No 'programming' found.")
if(pythonMention > 0 and programIndex != -1):
    print("Python programming mentioned.")
if(any(c.isalpha() for c in userIn) and any(n.isnumeric() for n in userIn)):
    print("Alphanumeric content found.")