import base64
import zlib
import codecs

# Load the encoded content from the file
file_path = input(" File Enc : ")

def decrypt_file(file_path, output_path):
    with open(file_path, "r", encoding="utf-8") as f:
        encoded_content = f.read()
    
    # Extract the encoded data from the exec() call
    encoded_data = encoded_content.split("codecs.decode('")[1].split("'[::-1], 'rot_13'))))")[0]
    
    # Reverse ROT13 decoding
    decoded_rot13 = codecs.decode(encoded_data[::-1], "rot_13")
    
    # Base64 decode and Zlib decompress
    decoded_bytes = zlib.decompress(base64.b64decode(decoded_rot13))
    
    # Convert bytes to string 
    decoded_script = decoded_bytes.decode("utf-8")
    
    # Save the decoded script to a new file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(decoded_script)
    
    return output_path

# Define output file path
decrypted_file_path = input("output File dec: ")

decrypt_file(file_path, decrypted_file_path)

print(f"Decryption completed. File saved to: {decrypted_file_path}")
