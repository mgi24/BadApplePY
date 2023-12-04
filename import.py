from PIL import Image
import time
import pygetwindow as gw
import pyautogui
from pywinauto.keyboard import send_keys

def image_to_ascii(image_path, output_width=100, ascii_chars="@%#*+=-:. "):
    # Buka gambar
    img = Image.open(image_path)
    
    # Hitung aspek rasio gambar
    #img.width #img.height
    aspect_ratio = 1 / 5.5
    
    # Sesuaikan lebar gambar
    output_height = int(output_width * aspect_ratio)
    img = img.resize((output_width, output_height))
    
    # Konversi ke citra hitam putih
    img = img.convert("L")
    
    # Ambil data piksel sebagai array
    pixels = img.getdata()
    
    # Ubah nilai piksel menjadi karakter ASCII
    ascii_image = ""
    for pixel_value in pixels:
        ascii_index = int(pixel_value / 255 * (len(ascii_chars) - 1))
        ascii_image += ascii_chars[ascii_index]
    
    # Bagi hasil ke dalam baris sesuai lebar gambar
    lines = [ascii_image[i:i+output_width] for i in range(0, len(ascii_image), output_width)]
    ascii_image = "\n".join(lines)
    
    return ascii_image

totalimage=13147;
i=0;
while(i<totalimage):
    frame_number_str = f"{i:05d}"
    input_image_path = f"D:/upload yt/badframe/0{frame_number_str}.png"
    output_ascii = image_to_ascii(input_image_path, output_width=1850)#1924

    output_file_path = f"D:/upload yt/badascii/0{frame_number_str}.txt"
    with open(output_file_path, 'w') as file:
        file.write(output_ascii);

    with open(output_file_path, 'r') as file:
        file_content = file.read()
        #print(file_content)
        print(i)
    i+=1
