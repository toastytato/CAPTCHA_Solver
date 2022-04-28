import os

extensions = [".jpg",".jpeg",".png"]
path = '/Users/andrewwhitaker/Downloads/Recaptcha Dataset/'
folder_names = ['Hydrant', 'Car', 'Bridge', 'Boat', 'Motorcycle', 'Bus', 'Tow Truck', 'Truck', 'Chimney', 'Traffic Sign', 'Taxi', 'Bicycle', 'Mountain', 'Crosswalk', 'Stairs', 'Traffic Light', 'Palm']

for i, folder in enumerate(folder_names):
    file_names = os.listdir(path + folder + '/')
    for image in file_names:
        if not any(x in image for x in extensions):
            print(image + ':' + folder_names[i])

#os.remove('/Users/andrewwhitaker/Downloads/Recaptcha Dataset/Bicycle/.DS_Store')

        