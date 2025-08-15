from PIL import Image, ImageOps
import sys
import os

user_input = sys.argv
if len(user_input) == 3:
    file1, file2 = user_input[1], user_input[2]
    ext1, ext2 = os.path.splitext(file1)[1], os.path.splitext(file2)[1]
    if ext1 in ('.jpg', '.jpeg', '.png') and ext2 in ('.jpg', '.jpeg', '.png'):
        try:
            with Image.open(f'{file1}') as file1:
                user_img_overlay = Image.open(f'{file2}')
                file1 = ImageOps.fit(image=file1, size=[600, 600])
                overlay = Image.open('shirt.png')
                file1.paste(im=overlay, box=(0,0), mask=user_img_overlay)
                file1.save(fp='after1.jpg', format='JPEG')
                print('Sucsess!!!')
        except FileNotFoundError as e:
            file = os.path.basename(e.filename)
            sys.exit(f'Can not open file {file}')
elif len(user_input) < 3: 
    sys.exit('Too few command-line arguments')
else:
    sys.exit('Too many command-line arguments')

    
