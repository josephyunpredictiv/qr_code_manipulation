# -*- coding: utf-8 -*-
"""
Original file is located at (not publicly avalible)
    https://colab.research.google.com/drive/1udDjeIurmMMVUpZYapC8vOP0B_QM3YZd
"""

!pip install qrcode[pil]
import qrcode
from PIL import Image, ImageOps

###### replace color
icon_path = "/content/spiralv41.webp"  # Replace with the actual path to your icon image
icon_img = Image.open(icon_path)
img = icon_img.convert("RGB")

pixels = img.load()
(val1, val2, val3)=(18, 4, 36)
width, height = img.size
tolerance=60

## Replaces color with another color. Edit tolerance accordingly.
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        #if (r, g, b) == (255, 255, 255):
        #if (r, g, b) == (181, 215, 168):
        #if 230 <= r <= 255 and 230 <= g <= 255 and 230 <= b <= 255:
        if val1-tolerance <= r <= val1+tolerance and val2-tolerance <= g <= val2+tolerance and val3-tolerance <= b <= val3+tolerance:
        #if (r, g, b) == (247, 247, 247):
            icon_img.putpixel((x, y), (0,0,0))

icon_img

####### Black and white. 
img = icon_img.convert("RGB")
pixels = img.load()
(val1, val2, val3)=(184, 182, 175)
width, height = img.size
tolerance=10
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        if (r, g, b) != (255, 255, 255):
        #if (r, g, b) == (181, 215, 168):
        #if 230 <= r <= 255 and 230 <= g <= 255 and 230 <= b <= 255:
        #if val1!=255 and val2!=255 and val3!=255:
        #if (r, g, b) == (247, 247, 247):
            icon_img.putpixel((x, y), (255,255,255))
        else:
          icon_img.putpixel((x, y), (0,0,0))

icon_img


###### transparent for one color
def replace_color_with_transparent(input_image_path, output_image_path, target_color, tolerance=0):
    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Convert the image to RGBA mode (if not already)
    image = image.convert("RGBA")

    # Extract the target color components
    target_r, target_g, target_b = target_color

    # Create a transparent image with the same size
    transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Iterate through the pixels and copy them to the transparent image
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            r, g, b, a = pixel

            # Check if the pixel color is within the specified tolerance range of the target color
            if (
                abs(r - target_r) <= tolerance and
                abs(g - target_g) <= tolerance and
                abs(b - target_b) <= tolerance
            ):
                # If within the tolerance, set the pixel's alpha channel to 0 (transparent)
                pixel = (r, g, b, 0)

            # Paste the pixel onto the transparent image
            transparent_image.putpixel((x, y), pixel)

    # Save the result to the output file
    transparent_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "/content/img2.png"  # Replace with your input image path
    output_image_path = "/content/output.png"  # Replace with your desired output image path
    target_color = (248, 246, 245)  # Replace with the RGB color you want to replace
    tolerance = 30  # Tolerance value for color matching (adjust as needed)

    replace_color_with_transparent(input_image_path, output_image_path, target_color, tolerance)



###### greyscale
icon_path = "/content/img.png"

# Load the icon image
icon_img = Image.open(icon_path)
img = icon_img.convert("RGB")
icon_img = icon_img.convert("L")
# Convert the icon image to grayscale
icon_img = ImageOps.grayscale(icon_img)
icon_img

# Define the content for the QR code
qr_content = "https://lucid.app/lucidspark/2331a208-7781-40dc-a96b-abfc17d5329f/edit?viewport_loc=98%2C94%2C1873%2C1043%2C0_0&invitationId=inv_b3e3dbb0-c367-451e-80f0-a44faacd26a4"

# Define the size of the QR code and the icon
qr_size = 300*2*20  # Set the size of the QR code (square)
icon_size = 80*40  # Set the size of the icon (square)

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(qr_content)
qr.make(fit=True)



###### Create a QR code image
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img = qr_img.resize((qr_size, qr_size))

icon_path = "/content/jamboard_logo.png"  # Replace with the actual path to your icon image
icon_img = Image.open(icon_path)
icon_img = icon_img.resize((icon_size, icon_size))
img = icon_img.convert("RGB")

pixels = img.load()

# Define the color to replace (pure white)
target_color = (255, 255, 255)

# Loop through each pixel and replace pure white with black
'''width, height = img.size
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        if (r, g, b) == (255, 255, 255):
            icon_img.putpixel((x, y), (0, 0, 0))
        else:
            icon_img.putpixel((x, y), (255, 255, 255))'''
# Invert the grayscale image (white becomes black, black becomes white)
icon_img = icon_img.convert("L")
# Convert the icon image to grayscale
icon_img = ImageOps.grayscale(icon_img)

# Invert the grayscale image (light becomes dark, and dark becomes light)
icon_img = ImageOps.invert(icon_img)
# Calculate the position to place the icon in the center of the QR code
qr_width, qr_height = qr_img.size
icon_width, icon_height = icon_img.size
position = ((qr_width - icon_width) // 2, (qr_height - icon_height) // 2)

# Create a new image with the QR code and icon
qr_with_icon = qr_img.copy()
qr_with_icon.paste(icon_img, position)

# Display the QR code with the Discord icon
qr_with_icon.show()


####### Define the content for the QR code
qr_content = "http://127.0.0.1:5000/ID/P09611"
qrCode = qrcode.make(qr_content)

qrCode

