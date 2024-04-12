import os


# Function to rename directories
def rename_files(root_dir, names):
    for root, dirs, files in os.walk(root_dir):
        if len(dirs) == len(names):
            for d in dirs:
                # print(d)
                key = d.split(' ')[0]
                if key in names:
                    os.rename(os.path.join(root, d), os.path.join(root, names.get(key)))
                    print(f'{d} renamed to {names.get(key)}')


if __name__ == "__main__":
    # folder_path = input("Enter the path to the folder containing subfolders with .rar files: ")
    path = "G:\\Data_Selected"
    names = {'31': 'KhorasanRazavi', '32': 'KhorasanShomali', '33': 'KhorasanJonubi', '91': 'Ardebil',
             '36': 'Khuzetan', '67': 'Zanjan', '61': 'SistanAndBaluchestan', '26': 'AzarbayjanSharghi',
             '71': 'Kermanshah', '73': 'Kurdistan', '83': 'Ilam', '97': 'Golestan', '57': 'AzarbayjanQharbi',
             '54': 'Gilan'}
    # names1 = {'‫حجم تردد ساعتی‬': 'Hourly', '‫حجم تردد روزانه‬': 'Daily', 'Hourly Data': 'Hourly'}
    rename_files(path, names)
    print("Rename complete.")
