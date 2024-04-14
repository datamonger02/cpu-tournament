from PIL import Image
import os


def convert_images_to_png(folder_path):
    # Iterate through all files and subfolders in the folder
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # Check if the file is a webp or jpg image
            if filename.endswith(".webp") or filename.endswith(".jpg"):
                # Open the image
                with Image.open(os.path.join(root, filename)) as img:
                    # Remove the extension from the filename and save as png
                    png_filename = os.path.splitext(filename)[0] + ".png"
                    img.save(os.path.join(root, png_filename), "PNG")
                    print(f"Converted {filename} to {png_filename}")


# Specify the folder containing webp images
folder_path = r"Alt Renders"

# Convert webp images to png
convert_images_to_png(folder_path)
