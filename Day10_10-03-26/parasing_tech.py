## dumps(): Encryption
## loads(): Decryption


'''
1. JSON convert data into str
2. pickle convert data into binary
'''
# import json

# file = open('temp3.txt', 'a+')
# data = {
#   'Fullname': 'Adamya Gupta',
#   'userid': 1234567890,
#   'password': '******'
# }

# # print(f'Original Data: {data}')
# # print(f'Type of orginal data: {type(data)}')

# enc_data = json.dumps(data)
# # print(f'Encrypted Data: {enc_data}')
# # print(f'Type of encrypted data: {type(enc_data)}')

# # dec_data = json.loads(enc_data)
# # print(f'Decrypted Data: {dec_data}')
# # print(f'Type of Decrypted data: {type(dec_data)}')

# file.write(enc_data)

# file.seek(0)
# enc_data1 = file.read()
# print(type(enc_data1))

# ori_data = json.loads(enc_data1)
# print(type(ori_data))


# file.close()


import pickle

file = open('temp4.txt', 'ab+')
data = {
  'Fullname': 'Adamya Gupta',
  'userid': 1234567890,
  'password': '******'
}

# print(f'Original Data: {data}')
# print(f'Type of orginal data: {type(data)}')

enc_data = pickle.dumps(data)
# print(f'Encrypted Data: {enc_data}')
# print(f'Type of encrypted data: {type(enc_data)}')

# dec_data = json.loads(enc_data)
# print(f'Decrypted Data: {dec_data}')
# print(f'Type of Decrypted data: {type(dec_data)}')

file.write(enc_data)

file.seek(0)
enc_data1 = file.read()
print(type(enc_data1))

ori_data = pickle.loads(enc_data1)
print(type(ori_data))


file.close()