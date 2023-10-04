from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def image_scl(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value//range_width]
    return ascii_str

def iamge_to_ascii(image, new_width=100):
    image = image_scl(image)
    image = grayscale(image)
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return ascii_img

if __name__ == "__main__":
    image_path = "img path"  # Replace with the path to your image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        exit()
    
    ascii_img = iamge_to_ascii(image)
    print(ascii_img)
