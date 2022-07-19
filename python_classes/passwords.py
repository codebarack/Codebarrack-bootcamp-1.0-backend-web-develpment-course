
password = "TupleIsThe"
txt = open("file.txt", "r+")
txt.write(password)
word = txt.readline()
txt.close()
user_input = input("> Please input your password: ")
n = 3
count = 0
while count < n:
    count += 1
    if user_input == word:
        print("Access Granted")
        break
else:
    print("Access Denied")
    