#  Route Cipher with Custom Hash Function 

##  Overview

This project implements a **Route Cipher combined with a custom-designed hash function** to achieve both **encryption** and **data integrity**.

The system works by:

* Encrypting plaintext using **spiral traversal**
* Appending a **custom hash**
* Verifying integrity during decryption

---

##  Code Approach

The input message is first **preprocessed** by removing spaces to simplify matrix handling. The processed text is then combined with a **custom-generated hash**, ensuring integrity is embedded directly into the encrypted data.

Next, the combined text is arranged **row-wise into a 2D matrix**. The dimensions of the matrix are dynamically calculated using:

* Ceiling of square root for rows
* Ceiling division for columns

This guarantees that all characters fit into the grid.

###  Encryption Process

* The matrix is filled **row-wise**
* Encryption is performed by traversing the matrix in a **spiral pattern**
* The traversal follows:

  * Top row → Right column → Bottom row → Left column
* This rearrangement produces the **ciphertext**

---

###  Decryption Process

* An empty matrix is created
* The ciphertext is filled back using the **same spiral traversal pattern**
* The matrix is then read **row-wise**
* The last 8 characters are extracted as the hash
* The remaining part is the original message

Finally, the hash is recomputed and compared:

* Match → VALID
* Mismatch → TAMPERED

---

##  Hash Function Approach

A **custom hash function** is designed to generate a unique representation of the message, ensuring data integrity.

Unlike standard hashing algorithms, this function is built from scratch using **bit manipulation and arithmetic operations**.

---

###  How It Works

1. **Initial Seed**

   * Starts with a large constant value:

     ```
     2654435769
     ```
   * This improves distribution and avoids weak initial states

2. **Character Processing**

   * Each character is converted to its ASCII value using `ord()`
   * The position index is included to ensure order sensitivity

3. **Bit Mixing**

   * Applies:

     ```
     (h << 5) + (h >> 2) + value + index
     ```
   * This introduces strong variation at the binary level

4. **XOR Combination**

   * Combines values using:

     ```
     h = h ^ mixed
     ```
   * Ensures small changes spread across bits

5. **32-bit Limiting**

   * Keeps hash within fixed size:

     ```
     h = h & 0xFFFFFFFF
     ```

6. **Final Avalanche Mixing**

   * Additional mixing using shifts and multiplication:

     ```
     h ^= (h >> 16)
     h *= 0x45d9f3b
     h ^= (h >> 16)
     ```

7. **Output**

   * Returned as an **8-character hexadecimal value**

---

###  Key Idea

This hash function is inspired by:

* **Knuth’s multiplicative hashing**
* **Bit-level mixing techniques**

---

###  Important Properties

* Same input → Same hash
* Small change → Completely different hash
* Efficient and fast
* No built-in cryptographic libraries used

---

##  Program Flow

```text
Plaintext → Preprocess → Append Hash → Encrypt → Ciphertext
                                           ↓
                                      Decrypt → Verify Hash → Output
```

---

##  Example

### Input

```text
HELLO
```

### Step 1: Hash Generated

```text
8A1F3C2D   (example)
```

### Step 2: Combined Text

```text
HELLO8A1F3C2D
```

### Step 3: Encryption (Spiral Cipher)

```text
Ciphertext → (spiral transformed text)
```

### Step 4: Decryption

```text
Decrypted Text → HELLO
Status → VALID
```

##  Key Points

* Hash is appended before encryption
* Last 8 characters represent hash
* Grid uses `'X'` padding
* Spiral traversal ensures strong transformation
* Hash ensures tamper detection

