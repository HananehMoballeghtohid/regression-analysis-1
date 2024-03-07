import os
import subprocess


# Function to extract .rar files in subfolders
def extract_rar_files(root_dir, valid_prefix):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.rar') and any(file.startswith(x) for x in valid_prefix):
                rar_file = os.path.join(root, file)

                r = root.split('\\')
                r[1] = 'Data_Selected'
                wd = '\\'.join(r)

                if not os.path.exists(wd):
                    os.makedirs(wd)

                os.chdir(wd)
                subprocess.call(['C:\Program Files\WinRAR\Rar.exe', 'x', rar_file])
                print(f"Extracted {file} into {wd}")


if __name__ == "__main__":
    # folder_path = input("Enter the path to the folder containing subfolders with .rar files: ")
    folder_path = "G:\\Data"
    destination_path = "G:\\Data_Selected"
    valid_prefixes = ['31', '32', '33', '91', '36', '67', '61', '26', '71', '73', '83', '97']
    extract_rar_files(folder_path, valid_prefixes)
    print("Extraction complete.")
