import hashlib

pwd = input("Enter password: ")
hash = hashlib.sha256(pwd.encode()).hexdigest()
print("SHA-256 hash:", hash)
