import os


def rename_images(folder_path):
    # Iterate through all files and subfolders in the folder
    for root, dirs, files in os.walk(folder_path):
        # Check if the directory contains the word "Mii"
        if "Mii" in root:
            print(f"Skipping directory: {root} (contains 'Mii')")
            continue

        for filename in files:
            # Check if the file is a webp or jpg image
            if filename.endswith(".webp") or filename.endswith(".jpg") or filename.endswith(".png"):
                # Extract the number n from the filename
                n = filename.split("(")[-1].split(")")[0]
                # Rename the file to "n.png"
                new_filename = f"{n}.png"
                # Rename the file
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                print(f"Renamed {filename} to {new_filename}")


# Specify the folder containing images (including subfolders)
folder_path = r"you\will\not\see\my\filepath.txt"

# Rename all images in all subfolders
rename_images(folder_path)
