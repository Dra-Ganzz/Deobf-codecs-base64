import base64
import marshal
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Kunci dan IV (sesuaikan dengan yang di enc .py)
key = b'I\x0e\x88\x91\xad\xf2\xc1\x0c,+\x0e\xb3\x06\xdc\xfdd'
iv = b'\x92\xb6 \x1f\xc6\xba\xfa!\xecYY:\xd1\xf66\x92'

# Nama file input dan output
input_file = input("File enc : ")
output_file = "memek_decrypted.py"
debug_file = "debug_decrypted.bin"

# Membaca isi file terenkripsi
with open(input_file, "r") as f:
    encrypted_data = f.read()

try:
    # Ekstraksi cipher_text dari base64
    cipher_text = base64.b64decode(encrypted_data.split("b64decode('")[1].split("')")[0])

    # Dekripsi AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(cipher_text), AES.block_size)

    # Simpan hasil dekripsi ke file debug untuk analisis manual
    with open(debug_file, "wb") as f:
        f.write(decrypted_data)

    print(f"Debugging file saved as: {debug_file}")

    # Coba unmarshal data
    decoded_code = marshal.loads(decrypted_data)

    # Simpan hasil dekripsi ke file baru
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decoded_code if isinstance(decoded_code, str) else repr(decoded_code))

    print(f"Decryption successful! File saved as: {output_file}")

except Exception as e:
    print(f"Error: {e}")
