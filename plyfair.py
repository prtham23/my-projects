def encrypt(key, message):
    # Prepare the matrix
    matrix = prepare_matrix(key)

    # Prepare the message
    message = prepare_message(message)

    # Encrypt the message
    encrypted = []
    for i in range(0, len(message), 2):
        a, b = message[i:i+2]
        row1, col1 = get_position(a, matrix)
        row2, col2 = get_position(b, matrix)

        if row1 == row2:
            encrypted.append(matrix[row1][(col1 + 1) % 5])
            encrypted.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted.append(matrix[(row1 + 1) % 5][col1])
            encrypted.append(matrix[(row2 + 1) % 5][col2])
        else:
            encrypted.append(matrix[row1][col2])
            encrypted.append(matrix[row2][col1])

    return ''.join(encrypted)

def decrypt(key, encrypted):
    # Prepare the matrix
    matrix = prepare_matrix(key)

    # Decrypt the message
    decrypted = []
    for i in range(0, len(encrypted), 2):
        a, b = encrypted[i:i+2]
        row1, col1 = get_position(a, matrix)
        row2, col2 = get_position(b, matrix)

        if row1 == row2:
            decrypted.append(matrix[row1][(col1 - 1) % 5])
            decrypted.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted.append(matrix[(row1 - 1) % 5][col1])
            decrypted.append(matrix[(row2 - 1) % 5][col2])
        else:
            decrypted.append(matrix[row1][col2])
            decrypted.append(matrix[row2][col1])

    return ''.join(decrypted)

def prepare_matrix(key):
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(key[i*5 + j])
        matrix.append(row)
    return matrix

def prepare_message(message):
    message = message.replace(' ', '').upper()
    if len(message) % 2 == 1:
        message += 'X'
    return message

def get_position(c, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return (i, j)

# print(encrypt(key,message))
# print(decrypt(key,encrypted))