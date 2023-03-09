import os
import datetime

# create folder with today's date
today = datetime.date.today()
folder_name = today.strftime('%Y-%m-%d')
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

while True:
    # get user input
    name = input('Enter name: ')
    surname = input("Enter surname: ")
    id_number = input('Enter personal ID number: ')

    # create file name
    file_name = f"{id_number}.txt"

    # check if file already exists for this ID in today's folder
    file_path = os.path.join(folder_name, file_name)
    if os.path.exists(file_path):
        print('File already exists for this ID in today folder.')
        continue

    # save user info in file
    with open(file_path, 'w') as f:
        f.write(f'Name: {name}\n')
        f.write(f'Surname: {surname}\n')
        f.write(f'ID number: {id_number}\n')

    # ask user if they want to enter more info
    again = input('Do you want to enter more information? (y/n): ')
    if again.lower() != 'y':
        break
