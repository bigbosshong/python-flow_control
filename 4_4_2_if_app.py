input_id = input('id : ')
id = 'bigboss'
input_password = input('password : ')
password = '1111111'
if input_id == id:
    if input_password == password:
        print('Welcome')
    else:
        print('Wrong Password!')
else:
    print("Wrong ID")