f = open("/Users/janstosik/project-euler-tasks-001-100/problem-079-passcode-derivation/keylog.txt")
content = f.read()
logins = content.split("\n")


print(f"len: {len(logins)}, list: {logins}")

unique_chars = []
for item in logins:
    for char in item:
        if char not in unique_chars:
            unique_chars.append(char)
            
print("\n")
print(unique_chars)

# Okay so we got 8 digits in the password :) 
# Now let's see what always comes before a given char and what always comes after  

for char in unique_chars:
    before = []
    after = []
    for item in logins:
        if char not in item:
            continue
        if char == item[0]:
            after.append(item[1])
            after.append(item[2])
        if char == item[1]:
            before.append(item[0])
            after.append(item[2])
        if char == item[2]:
            before.append(item[0])
            before.append(item[1])
            
    print(f"\n {char}, before: {list(set(before))}, after: {list(set(after))}, \n")


# after printing it i've done the rest by hand
print(" answer derived from that is: 73162890")
