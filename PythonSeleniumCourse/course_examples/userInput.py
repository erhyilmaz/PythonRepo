password = "Deneme"
trialCount = 0

while True:
    trialCount += 1
    if trialCount > 3:
        print(f"trialCount {trialCount-1} == 3")
        break
    user_input = input("Enter Password: ")
    if user_input == password:
        print(f"Well done! You entered correct password: {user_input}")
        break
    else:
        pass

print("Finish!")
