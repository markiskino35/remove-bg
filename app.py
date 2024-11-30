from rembg import remove
from PIL import Image
import io

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_file:
        input_data = input_file.read()
        
    output_data = remove(input_data)

    # Save the output image
    with open(output_image_path, 'wb') as output_file:
        output_file.write(output_data)

    print(f"Background removed and saved as {output_image_path}")

# Use
remove_background("test.jpg", "output_image.png")
