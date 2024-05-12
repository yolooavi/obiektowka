import hashlib


class CipherFactory:
    _instances = {}

    @classmethod
    def get_instance(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            cls._instances[cls]._init()
        return cls._instances[cls]

    def _init(self):
        pass

    def create_cipher(self, cipher_type, *args, **kwargs):
        if cipher_type == "caesar":
            return CaesarCipher(*args, **kwargs)
        elif cipher_type == "substitution":
            return SubstitutionCipher(*args, **kwargs)
        elif cipher_type == "transposition":
            return TranspositionCipher(*args, **kwargs)
        else:
            raise ValueError("Invalid cipher type")


class Encryption:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.cipher = None

    def set_cipher(self, cipher):
        self.cipher = cipher

    def encrypt(self, text):
        if self.cipher:
            return self.cipher.encrypt(text)
        else:
            raise ValueError("Cipher not set")

    def decrypt(self, text):
        if self.cipher:
            return self.cipher.decrypt(text)
        else:
            raise ValueError("Cipher not set")

    def sha256_encrypt(self, text):
        return hashlib.sha256(text.encode()).hexdigest()

    def caesar_brute_force_decrypt(self, text):
        for shift in range(1, 26):
            cipher = CaesarCipher(shift)
            decrypted_text = cipher.decrypt(text)
            print(f"Próba z przesunięciem {shift}: {decrypted_text}")



    def encrypt_file(self, file_path, output_path):
        if self.cipher:
            try:
                with open(file_path, 'r') as file:
                    plaintext = file.read()
            except FileNotFoundError:
                raise FileNotFoundError("Plik nie istnieje.")
            except Exception as e:
                raise ValueError(f"Błąd odczytu pliku: {e}")

            encrypted_text = self.encrypt(plaintext)

            try:
                with open(output_path, 'w') as file:
                    file.write(encrypted_text)
            except Exception as e:
                raise ValueError(f"Błąd zapisu zaszyfrowanego pliku: {e}")
        else:
            raise ValueError("Cipher not set")

    def decrypt_file(self, file_path, output_path):
        if self.cipher:
            try:
                with open(file_path, 'r') as file:
                    ciphertext = file.read()
            except FileNotFoundError:
                raise FileNotFoundError("Plik nie istnieje.")
            except Exception as e:
                raise ValueError(f"Błąd odczytu pliku: {e}")

            decrypted_text = self.decrypt(ciphertext)

            try:
                with open(output_path, 'w') as file:
                    file.write(decrypted_text)
            except Exception as e:
                raise ValueError(f"Błąd zapisu odszyfrowanego pliku: {e}")
        else:
            raise ValueError("Cipher not set")


class Cipher:
    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass


class CaesarCipher(Cipher):
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, text):
        encrypted_text = ''
        for char in text:
            if char.isalpha():
                shifted = ord(char) + self.shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ''
        for char in text:
            if char.isalpha():
                if char.islower():
                    shifted = ord(char) - self.shift
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    shifted = ord(char) - self.shift
                    if shifted < ord('A'):
                        shifted += 26
                decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text


class SubstitutionCipher(Cipher):
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encrypted_text = ''
        for char in text:
            if char.lower() in alphabet:
                if char.islower():
                    encrypted_text += self.key[alphabet.index(char)]
                else:
                    encrypted_text += self.key[alphabet.index(char.lower())].upper()
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        decrypted_text = ''
        for char in text:
            if char.lower() in alphabet:
                if char.islower():
                    decrypted_text += alphabet[self.key.index(char)]
                else:
                    decrypted_text += alphabet[self.key.index(char.lower())].upper()
            else:
                decrypted_text += char
        return decrypted_text


class TranspositionCipher(Cipher):
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        encrypted_text = [''] * self.key
        for col in range(self.key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += self.key
        return ''.join(encrypted_text)

    def decrypt(self, text):
        num_of_cols = (len(text) + self.key - 1) // self.key
        num_of_rows = self.key
        num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(text)
        decrypted_text = [''] * num_of_cols
        col = 0
        row = 0
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0
                row += 1
        return ''.join(decrypted_text)


def main():
    cipher_factory = CipherFactory.get_instance()
    encryption = Encryption()
    while True:
        print("Wybierz opcję szyfrowania:")
        print("1. Szyfr Cezara")
        print("2. Szyfr podstawieniowy")
        print("3. Szyfr przestawieniowy")
        print("4. Szyfrowanie SHA-256")
        print("5. Łamanie szyfru Cezara brute force")
        print("6. Szyfrowanie pliku tekstowego")
        print("7. Deszyfrowanie pliku tekstowego")
        print("8. Wyjdź")

        choice = input("Wybierz opcję (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            try:
                shift = int(input("Podaj przesunięcie dla szyfru Cezara (liczba całkowita): "))
                encryption.set_cipher(cipher_factory.create_cipher("caesar", shift))
            except ValueError:
                print("Niepoprawny format. Podaj liczbę całkowitą.")
                continue
            plaintext = input("Podaj tekst do zaszyfrowania: ")
            encrypted_text = encryption.encrypt(plaintext)
            print("Zaszyfrowany tekst: ", encrypted_text)

            if input("Czy chcesz użyć innego szyfru? (tak/nie): ").lower() == 'tak':
                continue
            else:
                break

        elif choice == '2':
            key = input("Podaj klucz szyfru podstawieniowego (26 różnych liter alfabetu w kolejności zastępowania): ")
            if len(key) != 26 or not key.isalpha() or len(set(key.lower())) != 26:
                print("Niepoprawny format klucza. Podaj 26 różnych liter alfabetu.")
                continue

            encryption.set_cipher(cipher_factory.create_cipher("substitution", key))
            plaintext = input("Podaj tekst do zaszyfowania: ")
            encrypted_text = encryption.encrypt(plaintext)
            print("Zaszyfrowany tekst: ", encrypted_text)

            if input("Czy chcesz użyć innego szyfru? (tak/nie): ").lower() == 'tak':
                continue
            else:
                break

        elif choice == '3':
            plaintext = input("Podaj tekst do zaszyfrowania: ")
            try:
                default_key = int(len(plaintext) ** 0.5)
            except ValueError:
                print("Długość tekstu jest nieprawidłowa. Podaj tekst do zaszyfrowania.")
                continue

            key_choice = input(f"Podaj liczbę kolumn (domyślnie {default_key}): ")
            if not key_choice.isdigit():
                print("Niepoprawny format klucza. Podaj liczbę całkowitą.")
                continue

            key = int(key_choice)
            encryption.set_cipher(cipher_factory.create_cipher("transposition", key))
            encrypted_text = encryption.encrypt(plaintext)
            print("Zaszyfrowany tekst: ", encrypted_text)

            if input("Czy chcesz użyć innego szyfru? (tak/nie): ").lower() == 'tak':
                continue
            else:
                break

        elif choice == '4':
            plaintext = input("Podaj tekst do zaszyfrowania: ")
            encrypted_text = encryption.sha256_encrypt(plaintext)
            print("SHA-256 skrót: ", encrypted_text)

            if input("Czy chcesz użyć innego szyfru? (tak/nie): ").lower() == 'tak':
                continue
            else:
                break

        elif choice == '5':
            ciphertext = input("Podaj zaszyfrowany tekst do złamania: ")
            shift = int(input("Podaj przesunięcie dla szyfru Cezara (liczba całkowita): "))
            cipher = cipher_factory.create_cipher("caesar", shift)
            encryption.set_cipher(cipher)
            encryption.caesar_brute_force_decrypt(ciphertext)

            if input("Czy chcesz użyć innego szyfru? (tak/nie): ").lower() == 'tak':
                continue
            else:
                break


        elif choice == '6':

            file_path = input("Podaj ścieżkę do pliku tekstowego do zaszyfrowania: ")
            output_path = input("Podaj ścieżkę do zapisania zaszyfrowanego pliku: ")

            try:
                encryption.encrypt_file(file_path, output_path)

            except FileNotFoundError:
                print("Plik nie istnieje.")

            except ValueError as e:
                print(e)

        elif choice == '7':

            file_path = input("Podaj ścieżkę do zaszyfrowanego pliku tekstowego: ")
            output_path = input("Podaj ścieżkę do zapisania odszyfrowanego pliku: ")

            try:
                encryption.decrypt_file(file_path, output_path)

            except FileNotFoundError:
                print("Plik nie istnieje.")

            except ValueError as e:
                print(e)


        elif choice == '8':
            print("Do widzenia!")
            break

        else:
            print("Niepoprawny wybór. Wybierz 1, 2, 3, 4, 5 lub 6.")


if __name__ == "__main__":
    main()
