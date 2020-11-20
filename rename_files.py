import os

video_folder =  r'C:\Users\Luiza\Downloads\bob_esponja\1ª'

os.chdir(video_folder)

ep_num = 1
for file_name in os.listdir():

    # Getting title
    file_title, file_extension = os.path.splitext(file_name)

    if ep_num < 10:
        new_file_name = f'Bob_Esponja_1x0{ep_num}{file_extension}'
    else:
        new_file_name = f'Bob_Esponja_1x{ep_num}{file_extension}'

    ep_num = ep_num + 1 

    # Renaming the file
    os.rename(file_name, new_file_name)

print('Rename Successful!')