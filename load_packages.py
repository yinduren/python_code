import os
import sys

def create_import_module(file_path):
    module_name = file_path.split('.')[0].replace('/', '.')
    print(f"{module_name}")
    import_file.write(f'import {module_name}\n')


def create_import_file(path):
    for dir_path, subpaths, files in os.walk(package_path, topdown=False):
        for file in files:
            file_path=os.path.join(dir_path, file)
            if file_path.split('.')[1] == "py":
                if file_path.find('__init__', 0, len(file_path)) == -1:
                   create_import_module(file_path)



if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage:")
        print("Python3 load_packages.py old_test_main_file new_test_main_file your_package_path")
        sys.exit()

    pytest_main_file = open(sys.argv[1], 'r')
    pytest_main_file_merged = open(sys.argv[2], 'w')
    package_path = sys.argv[3]

    import_file = open("./import_file", "w")

    create_import_file(package_path)

    import_file.close()

    import_file_inserted = 0

    for line in pytest_main_file:
        if import_file_inserted == 0 and line.find('import', 0, len(line)) != -1:
            import_file = open("./import_file", "r")

            for import_line in import_file:
                pytest_main_file_merged.write(import_line)

            import_file.close()

            import_file_inserted = 1

        pytest_main_file_merged.write(line)
                
                
            

    
    

