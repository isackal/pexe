import base64
import getpass
import hashlib
import hmac
import pyperclip
import sys

def main(args: list[str]):
    # Prompt the user for a domain
    domain = args[0]
    # Prompt the user for a secret, masked
    secret = getpass.getpass("Enter the secret: ")

    # Convert domain and secret to bytes using UTF-8 encoding
    domain_bytes = domain.encode('utf-8')
    null_domain_bytes = b''
    secret_bytes = secret.encode('utf-8')

    # Create HMAC-SHA256 object with the secret as key
    hmac_obj = hmac.new(secret_bytes, digestmod=hashlib.sha256)

    # Compute the HMAC-SHA256 hash of the domain
    hmac_obj.update(domain_bytes)
    hash_bytes = hmac_obj.digest()

    # Compute the HMAC-SHA256 hash of the null domain
    hmac_obj_null = hmac.new(secret_bytes, digestmod=hashlib.sha256)
    hmac_obj_null.update(null_domain_bytes)
    proof_bytes = hmac_obj_null.digest()

    # Take the first 20 bytes of the hash for the main password
    partial_hash = hash_bytes[:20]

    # Take the first 6 bytes of the null-domain hash for the "proof"
    partial_proof = proof_bytes[:6]

    # Encode them in Base64
    psw = base64.b64encode(partial_hash).decode('utf-8')
    proof = base64.b64encode(partial_proof).decode('utf-8')

    # Copy the password to the clipboard
    pyperclip.copy(psw)

    # Print a confirmation message and the proof
    print(proof)
    print("\nPassword has been copied to your clipboard.")

if __name__ == "__main__":
    main(sys.argv[1:])
