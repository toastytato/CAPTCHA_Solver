from pathlib import Path
import os
import matplotlib.pyplot as plt


data_dir = "/Users/andrewwhitaker/Downloads/Recaptcha Dataset/"
folder_names = ['Hydrant', 'Car', 'Bridge', 'Boat', 'Motorcycle', 'Bus', 'Tow Truck', 'Truck', 'Chimney',
                'Traffic Sign', 'Taxi', 'Bicycle', 'Mountain', 'Crosswalk', 'Stairs', 'Traffic Light', 'Palm']




        
        
for folder in folder_names:
    cur_directory = data_dir + folder + '/'
    img_ext = ["bmp", "gif", "jpeg", "png"]
    for filepath in Path(cur_directory).rglob("*"):
        try:
            img = plt.imread(filepath)
        except Exception as e:
            print(f'Except: {e}', filepath)
            #os.remove(filepath)

