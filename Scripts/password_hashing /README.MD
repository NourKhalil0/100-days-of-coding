# Understanding SHA-256 Hashing

## What is SHA-256?

**SHA-256** stands for **Secure Hash Algorithm 256-bit**. It is part of the SHA-2 family, developed by the **U.S. National Security Agency (NSA)** and published by **NIST**. SHA-256 is widely used in cryptography and security applications such as:

- Password hashing
- Digital signatures
- Data integrity verification
- Blockchain and cryptocurrency (e.g., Bitcoin)
- File checksums

SHA-256 always produces a **256-bit (32-byte)** hash, represented as a **64character hexadecimal string**, regardless of the input size. Scroll down to see the input and output example.

---

## What is a Hash Function?

A **hash function** is a one-way mathematical function that maps data of arbitrary size to a fixed length output. It has the following key properties:

###  Key Characteristics of SHA-256:

- Deterministic: The same input will always produce the same output.
- Fast Computation: Optimized for speed and performance.
- Irreversible (OneWay): It's computationally infeasible to retrieve the original input from the hash.
- Collision-Resistant: It’s extremely unlikely for two different inputs to produce the same hash.
- Avalanche Effect: A small change in the input leads to a completely different hash.

---

## How Does SHA-256 Work?

SHA-256 processes data in **512-bit blocks**, breaking the input into chunks and performing a series of bitwise operations and modular additions. Internally, it involves:

- Padding the message to a multiple of 512 bits.
- Parsing the message into 512bit blocks.
- Initializing eight 32bit words (the initial hash values).
- Running 64 rounds of bitwise transformations using logical functions (AND, Xor, NOT, etc.) and constants.

While the internal mechanics are complex, the usage is simple in most programming languages.

---

# SHA-256 input and out Example

***First example:*** 
![Alt-tekst](https://raw.githubusercontent.com/NourKhalil0/100-days-of-coding/main/images/Screenshot%202025-06-13%20at%2021.06.03.png)
***Second example:***
![Screenshot](https://raw.githubusercontent.com/NourKhalil0/100-days-of-coding/main/images/Screenshot%202025-06-13%20at%2021.06.33.png)

***Now what did you notice?***
- I hope by now you noticed that the first example had a longer password than the second one,
    this is during the algorithm which processes data in blocks and compresses it into a fixed length output to ensure consistent and secure fingerprints
---
## Algorithm simulator in code:
***Now i wanted to show you the actual algorithm. But, it would be a very long code.
to understand the basic aidea of how it can generate the same length, check out this code:***
````python
    def sha256_simulator(data):
    # this is just a simolator, not real SHA-256
    blocks = [data[i:i+64] for i in range(0, len(data), 64)]
    
    hash_state = 0
    for block in blocks:
       
        block_value = sum(bytearray(block.encode()))
        hash_state = (hash_state ^ block_value) % (2**256)

  
    return hex(hash_state)[2:].zfill(64)


print("Short:", simple_sha256_simulator("hi"))
print("Long :", simple_sha256_simulator("a" * 1000))
````
---
## SHA-256 for Passwords? Think Again.
***Although SHA-256 is cryptographically secure, it should NOT be used alone for password hashing. Here’s why:***
1. Too Fast: It can be brute forced efficiently using GPU or Asics. 
2. No Salt: Without a unique random salt, identical passwords produce identical hashes. 
3. No Adaptive Cost: It does not allow for increasing computational cost as hardware improves.
***Use specialized password hashing algorithms like:***
- [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)
- [scrypt](https://en.wikipedia.org/wiki/Scrypt)
- [Argon2](https://en.wikipedia.org/wiki/Argon2)
---
## Use Cases for SHA-256
1. Verifying file integrity.
2. Digital signatures 
3. Signing software updates .
4. Cryptographic protocols (TLS, SSL, SSH).
5. Blockchain and mining.


