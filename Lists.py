

friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends[1] = "Mike"
print (friends[1:3])

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
friends.remove("Kim")
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends.pop()
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
print(friends.index("Oscar"))
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Kim", "Oscar", "Toby"]
friends.sort()
print(lucky_numbers)