from PIL import Image
import os


def get_png_from_subdirectory(subdirectory, number):

    current_directory = os.getcwd()
    # Construct the path to the subdirectory
    subdirectory_path = os.path.join(current_directory, "Alt Renders", subdirectory)

    # Check if the subdirectory exists
    if not os.path.isdir(subdirectory_path):
        print(f"Error: Subdirectory '{subdirectory}' not found")
        return None

    # Get a list of all .png files in the subdirectory
    png_files = [file for file in os.listdir(subdirectory_path) if file.endswith(".png")]

    # Check if the number is within the range of available .png files
    if number < 1 or number > len(png_files):
        print(f"Error: There is no .png file with index {number} in '{subdirectory}'")
        return None

    # Sort the list of .png files alphabetically
    png_files.sort()

    # Get the filename of the desired .png file
    png_filename = png_files[number - 1]

    # Open and return the specified .png file
    png_file_path = os.path.join(subdirectory_path, png_filename)
    return Image.open(png_file_path)


# Example usage:
subdirectory = "ZSS"
number = 4
resulting_image = get_png_from_subdirectory(subdirectory, number)
if resulting_image:
    resulting_image.show()  # Display the image
