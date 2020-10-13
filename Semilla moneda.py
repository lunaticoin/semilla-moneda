import hashlib
import binascii

### INPUT DE ENTROPÍA BINARIA
binario = input('Introduce los 128, 160, 192, 224 o 256 bits de entropia: ')
# Ejemplo 256 bits
# binario = '0011001010000101011111010000101111111111101000001001000001001010110100010101111001001011000100111100011110001001111011110111011010010100110011001110111001100010111011010010101101010011110100100110101111110001100101011001000110100010000110110001100101110001'
## Ejemplo 128 bits
# binario = '00110010100001010111110100001011111111111010000010010000010010101101000101011110010010110001001111000111100010011110111101110110'

### DEFINIENDO VARIABLES DEL BIP39
binario_len= len(binario) #ENT en el BIP39
cs = binario_len//32 #CS en BIP39 
palabras_totales = int((binario_len+cs)//11) #MS en BIP39

#Otras variables
modulo = int(binario_len%11) #bits de la última palabra no pertenecientes al checksum
extra_checksum_bits = binario[(binario_len-modulo):binario_len] #Los bits del checksum
print('\nLa longitud de la entropia introducida es de: ' + str(binario_len) + '\n-- ¡ATENCIÓN! Verifica que tu entropía tenga una de estas longitudes: 128, 160, 192, 224, 256')

### CONVERSIONES Y HASH
random_hex = hex(int(binario,2))[2:] #se pone lo de [2:] para que en el string no se almacene el 0x del inicio. Sino da errores
random_bin = binascii.unhexlify(random_hex)
numbytes = len(random_bin)

hashed_sha256 = hashlib.sha256(random_bin).hexdigest()
checksum = bin(int(hashed_sha256, 16))[2:].zfill(256)[: numbytes * 8 // 32]
binario_completo = binario + checksum
ultima_palabra_bits = str(extra_checksum_bits)+ str(checksum)


### LEER PALABRAS DEL ARCHIVO bip39words.txt
index_list =[]
with open ('bip39words.txt', 'r', encoding='utf-8') as f:
    for w in f.readlines():
        index_list.append(w.strip())

wordlist = []
for i in range(len(binario_completo)//11):
    index = int(binario_completo[i*11 : (i+1)*11], 2)
    wordlist.append(index_list[index])

semilla = " ".join(wordlist)



print('\nRESULTADOS\n-- El binario de tu palabra número ' + str(palabras_totales) + ' es:  ' + str(ultima_palabra_bits))
print('-- Tu última palabra tiene el valor decimal de:  '+ str(int(ultima_palabra_bits,2)))
print('-- ¡ATENCIÓN! Si en tu lista de palabras del BIP39 la palabra \'abandon\' aparece en la posición 1 (y no 0) tu palabra es entonces la número:  '+ str(int(ultima_palabra_bits,2)+1))
print('\n-- La palabra del checksum es:  ' + str(wordlist[palabras_totales-1]))
print('\nTu semilla completa es: '+ '\n-----------------------------------------------------------------\n' + str(semilla) + '\n-----------------------------------------------------------------\n')