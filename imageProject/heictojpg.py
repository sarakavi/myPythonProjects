from PIL import Image
import pyheif
import os

def convert_heic_to_jpg(input_path, output_path):
    try:
        # Read HEIC file
        heif_file = pyheif.read(input_path)
        
        # Convert to PIL Image
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # Save as JPEG
        image.save(output_path, "JPEG")
        print(f"Converted and saved {input_path} to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get input and output paths from user
    input_path = input("Enter the path to the HEIC image: ")
    output_path = input("Enter the path to save the converted JPEG image: ")
    
    convert_heic_to_j
