import os
import hashlib
from semilla_moneda import dir_path

BITS_POR_PALABRA = 11



def main():
    ### INPUT DE ENTROPÍA BINARIA
    binario = input("Introduce los 128, 160, 192, 224 o 256 bits de entropia: ")
    # Ejemplo 256 bits
    # binario = '0011001010000101011111010000101111111111101000001001000001001010110100010101111001001011000100111100011110001001111011110111011010010100110011001110111001100010111011010010101101010011110100100110101111110001100101011001000110100010000110110001100101110001'
    ## Ejemplo 128 bits
    # binario = '00110010100001010111110100001011111111111010000010010000010010101101000101011110010010110001001111000111100010011110111101110110'

    ### DEFINIENDO VARIABLES DEL BIP39
    binario_len = len(binario)  # ENT en el BIP39
    cs = binario_len // 32  # CS en BIP39
    palabras_totales = int((binario_len + cs) // BITS_POR_PALABRA)  # MS en BIP39

    # Otras variables
    modulo = int(binario_len % BITS_POR_PALABRA)  # bits de la última palabra no pertenecientes al checksum
    extra_checksum_bits = binario[(binario_len - modulo) : binario_len]  # Los bits del checksum
    print(
        f"\nLa longitud de la entropia introducida es de: {binario_len}"
        f"\n-- ¡ATENCIÓN! Verifica que tu entropía tenga una de estas longitudes: 128, 160, 192, 224, 256"
    )

    ### CONVERSIONES Y HASH
    random_hex = f"{int(binario, 2):x}"
    random_bin = bytes.fromhex(random_hex)
    numbytes = len(random_bin)

    hashed_sha256 = hashlib.sha256(random_bin).hexdigest()
    checksum = bin(int(hashed_sha256, 16))[2:].zfill(256)[: numbytes * 8 // 32]
    binario_completo = binario + checksum
    ultima_palabra_bits = str(extra_checksum_bits) + str(checksum)

    ### LEER PALABRAS DEL ARCHIVO bip39words.txt
    index_list = []

    with open(os.path.join(dir_path, "bip39words.txt"), "r", encoding="utf-8") as f:
        for w in f.readlines():
            index_list.append(w.strip())

    wordlist = []
    for i in range(len(binario_completo) // BITS_POR_PALABRA):
        index = int(binario_completo[i * BITS_POR_PALABRA : (i + 1) * BITS_POR_PALABRA], 2)
        wordlist.append(index_list[index])

    semilla = " ".join(wordlist)

    print(f"\nRESULTADOS\n-- El binario de tu palabra número {palabras_totales} es:  {ultima_palabra_bits}")
    print(f"-- Tu última palabra tiene el valor decimal de:  {int(ultima_palabra_bits, 2)}")
    print(
        f"-- ¡ATENCIÓN! Si en tu lista de palabras del BIP39 la palabra 'abandon' aparece en la posición 1 (y no 0) tu "
        f"palabra es entonces la número:  {int(ultima_palabra_bits, 2) + 1}"
    )
    print(f"\n-- La palabra del checksum es:  {wordlist[palabras_totales - 1]}")
    print(
        "\nTu semilla completa es: "
        "\n-----------------------------------------------------------------\n"
        f"{semilla}"
        f"\n-----------------------------------------------------------------\n"
    )


if __name__ == '__main__':
    main()