from uuid import uuid4
from models import ImageCode
from PIL import Image
import qrcode.image.svg
import os

datas = []
done = False
images_path = os.path.join(os.curdir, 'images')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)

while not done:
    print("""
    (1). Add Data
    (2). Show All Data
    (3). Show QR Code
    (q). Quit
    """)

    choice = input("Choose menu: ")

    if choice == '1':
        data_id = uuid4()
        name = input("Data name: ")
        value = input("Data value: ")

        qr.add_data(value)
        qr.make(fit=True)

        image_name = f"{str(data_id)}.png"
        img = qr.make_image()
        img.save(os.path.join(images_path, image_name))

        image_code = ImageCode(
            id=data_id,
            name=name,
            value=value,
            image=image_name
        )

        datas.append(image_code)
    elif choice == '2':
        for data in datas:
            print(f"{data.name}   {data.value}")
    elif choice == '3':
        data = {}

        data_name = input("Input your data name: ")

        for stored_data in datas:
            if stored_data.name == data_name:
                data = stored_data

        if data == {}:
            print("Data not found!")
        else:
            image_path = os.path.join(images_path, data.image)

            image = Image.open(image_path)
            image.show()
    elif choice == 'q':
        done = True
    else:
        done = True
