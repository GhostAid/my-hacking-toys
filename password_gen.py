import random
import string

print("🔐 BABY PASSWORD MAKER 🔐")
print("=" * 30)

# How long?
length = int(input("How many letters? (12 is good): "))

# What to put inside?
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Mix everything together
all_chars = letters + numbers + symbols

# Pick random ones
password = ""
for i in range(length):
    password = password + random.choice(all_chars)

print("\n🎁 Your super secret password:")
print(password)
print("\n👶 Don't tell anyone!")
