email = input("Enter your email: ")

# we wanna split the email at the @ symbol

index = email.index("@")

# start from beginning up until @ symbol
username = email[:index]
# start from @ symbol until the end
# do + 1 to omit the @ symbol
domain = email[index + 1:]

print (f"Your username is {username} and domain is {domain}")