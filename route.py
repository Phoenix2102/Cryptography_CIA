import math
def compute_hash(text):
    h = 2654435769  
    for i, ch in enumerate(text):
        val = ord(ch)
        mixed = ((h << 5) + (h >> 2) + val + i)
        h = h ^ mixed
        h = h & 0xFFFFFFFF 
    h = h ^ (h >> 16)
    h = (h * 0x45d9f3b) & 0xFFFFFFFF
    h = h ^ (h >> 16)
    return hex(h)[2:].upper().zfill(8)  
def get_dimensions(n):
    if n == 0:
        return 0, 0

    r = math.ceil(math.sqrt(n))
    c = math.ceil(n / r)
    return r, c
def make_grid(r, c, fill='X'):
    return [[fill for _ in range(c)] for _ in range(r)]
def spiral_read(grid):
    r, c = len(grid), len(grid[0])
    res = ""
    top, bot = 0, r - 1
    left, right = 0, c - 1
    while top <= bot and left <= right:
        for j in range(left, right + 1):
            res += grid[top][j]
        top += 1
        for i in range(top, bot + 1):
            res += grid[i][right]
        right -= 1
        if top <= bot:
            for j in range(right, left - 1, -1):
                res += grid[bot][j]
            bot -= 1
        if left <= right:
            for i in range(bot, top - 1, -1):
                res += grid[i][left]
            left += 1
    return res
def spiral_fill(grid, text):
    r, c = len(grid), len(grid[0])
    k = 0
    top, bot = 0, r - 1
    left, right = 0, c - 1
    while top <= bot and left <= right:
        for j in range(left, right + 1):
            grid[top][j] = text[k]
            k += 1
        top += 1
        for i in range(top, bot + 1):
            grid[i][right] = text[k]
            k += 1
        right -= 1
        if top <= bot:
            for j in range(right, left - 1, -1):
                grid[bot][j] = text[k]
                k += 1
            bot -= 1
        if left <= right:
            for i in range(bot, top - 1, -1):
                grid[i][left] = text[k]
                k += 1
            left += 1
def encrypt(text):
    text = text.replace(" ", "")
    h = compute_hash(text)
    combined = text + h
    r, c = get_dimensions(len(combined))
    grid = make_grid(r, c)
    k = 0
    for i in range(r):
        for j in range(c):
            if k < len(combined):
                grid[i][j] = combined[k]
                k += 1
    return spiral_read(grid)
def decrypt(cipher):
    r, c = get_dimensions(len(cipher))
    grid = make_grid(r, c)
    spiral_fill(grid, cipher)
    combined = ""
    for i in range(r):
        for j in range(c):
            combined += grid[i][j]

    combined = combined.rstrip('X')
    if len(combined) < 8:
        return combined, False
    text = combined[:-8]
    extracted_hash = combined[-8:]
    valid = (compute_hash(text) == extracted_hash)
    return text, valid
if __name__ == "__main__":
    msg = input("Enter text: ")
    cipher = encrypt(msg)
    print("\nEncrypted:", cipher)
    plain, status = decrypt(cipher)
    print("Decrypted:", plain)
    if status:
        print("Status: VALID")
    else:
        print("Status: TAMPERED")