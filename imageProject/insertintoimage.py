from PIL import Image
import os

def insert_image_to_directory(insert_path, directory, output_directory):
    try:
        # Open the insert image
        insert = Image.open(insert_path)
        insert_width, insert_height = insert.size
        
        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                # Open the background image
                background_path = os.path.join(directory, filename)
                background = Image.open(background_path)
                bg_width, bg_height = background.size

                # Calculate position: top right corner
                position = (bg_width - insert_width, 0)

                # Paste the insert image onto the background image
                background.paste(insert, position, insert if insert.mode == 'RGBA' else None)

                # Save the resulting image in the output directory
                output_path = os.path.join(output_directory, filename)
                background.save(output_path)
                print(f"Saved the output image at: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Paths to the images
    insert_path = input("Enter the path to the image to insert: ")
    directory = input("Enter the path to the directory containing the images: ")
    output_directory = input("Enter the path to save the output images: ")

    insert_image_to_directory(insert_path, directory, output_directory)
