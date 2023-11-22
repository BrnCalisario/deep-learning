# import os
# from PIL import Image
# import io


# def is_corrupted(image_path) -> bool:
#     try:
#         with Image.open(image_path) as img:
#             img.verify()
#         return False
#     except (IOError, SyntaxError):
#         return True

# def is_image(filename):
#     image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}

#     return any(filename.lower().endswith(ext) for ext in image_extensions)

# def delete_corrupted_images(root_dir):

#     for foldername, subfolders, filenames in os.walk(root_dir):
#         for filename in filenames:
#             file_path = os.path.join(foldername, filename)
#             if is_image(filename) and is_corrupted(file_path):
#                 print(f"Corrupted {file_path}")
#                 os.remove(file_path)
#                 print(f"{file_path} removed")
#         for subfolder in subfolders:
#             subfolder_path = os.path.join(foldername, subfolder)
#             delete_corrupted_images(subfolder_path)


# if __name__ == "__main__":
#     dirPath = "./images"
#     delete_corrupted_images(dirPath)