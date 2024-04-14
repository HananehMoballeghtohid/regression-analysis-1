import os


# Function to rename directories
def rename_files(root_dir, names):
    for root, dirs, files in os.walk(root_dir):
        if len(dirs) == 2:
            for d in dirs:
                key = d
                # key = d.split(' ')[0]
                if key in names:
                    os.rename(os.path.join(root, d), os.path.join(root, names.get(key)))
                    print(f'{d} renamed to {names.get(key)}')


if __name__ == "__main__":
    # folder_path = input("Enter the path to the folder containing subfolders with .rar files: ")
    path = "G:\\Data_Selected"
    names = {'61': 'SistanAndBaluchestan', '26': 'AzarbayjanSharghi','57': 'AzarbayjanQharbi',
             '11': 'Tehran', '54' : 'Gilan', '91' : 'Ardebil'}
    names1 = {'‫حجم تردد ساعتی‬': 'Hourly', '‫حجم تردد روزانه‬': 'Daily', 'Hourly Data': 'Hourly'}
    rename_files(path, names1)
    print("Rename complete.")
