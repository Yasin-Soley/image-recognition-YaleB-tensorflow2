from PIL import Image
import os

def convert_tif_to_jpg(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".tif"):
            # Construct the full path of the input file
            input_path = os.path.join(input_folder, filename)

            # Load the .tif image using Pillow
            img = Image.open(input_path)

            # Construct the full path of the output file with a .jpg extension
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)

            # Save the image in .jpg format
            img.save(output_path, "JPEG")

if __name__ == "__main__":
    # Replace 'input_folder' and 'output_folder' with your actual folder paths
    input_folder = "dataset/training_set/person_2"
    output_folder = "dataset/training_ds/person_2"

    convert_tif_to_jpg(input_folder, output_folder)
