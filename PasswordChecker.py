import re
pattern = "^.(?=.{8,})(?=.[0-9].[0-9])(?=.[a-z].[a-z])(?=.[A-Z].[A-Z])(?=.[@?#$%^&+=].[@?#$%^&+=]).$"
password = input("Enter Password\n")
result = re.findall(pattern,password)
if(result):
    print("Password is valid")
else:
    print("Password is invalid")
