from pathlib import Path
import imghdr
import os
import matplotlib.pyplot as plt


data_dir = "/Users/andrewwhitaker/Downloads/Recaptcha Dataset/"
image_extensions = [".png", ".jpg"]
folder_names = ['Hydrant', 'Car', 'Bridge', 'Boat', 'Motorcycle', 'Bus', 'Tow Truck', 'Truck', 'Chimney',
                'Traffic Sign', 'Taxi', 'Bicycle', 'Mountain', 'Crosswalk', 'Stairs', 'Traffic Light', 'Palm']



# for folder in folder_names:
#     cur_data_dir = data_dir + folder + '/'
#     img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
#     for filepath in Path(cur_data_dir).rglob("*"):
#         if filepath.suffix.lower() in image_extensions:
#             img_type = imghdr.what(filepath)
#             if img_type is None:
#                 print(f"{filepath} is not an image")
#             elif img_type not in img_type_accepted_by_tf:
#                 print(f"{filepath} is a {img_type}, not accepted by TensorFlow")
#             # if img_type is None:
#             #     os.remove(filepath)
#             # elif img_type not in img_type_accepted_by_tf:
#             #     os.remove(filepath)
        
        
for folder in folder_names:
    cur_data_dir = data_dir + folder + '/'
    img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
    for filepath in Path(cur_data_dir).rglob("*"):
        try:
            img = plt.imread(filepath)
        except Exception as e:
            print(f'Except: {e}', filepath)
            #os.remove(filepath)

