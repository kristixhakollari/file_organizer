import os
import shutil 


def modify(source_folder):

    for item in os.listdir(source_folder):

        item_path = os.path.join(source_folder,item)

        if os.path.isfile(item_path):

            extension = os.path.splitext(item_path)[1].lower()

            if extension:

                destination_folder = os.path.join(source_folder,extension[1:])

            else:

                destination_folder = os.path.join(source_folder, "no extension")

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            shutil.move(item_path,os.path.join(destination_folder,item))
            print (f"Moved {item} to {destination_folder}")

        elif os.path.isdir(item_path):
            modify(item_path)

if __name__ == "__main__":
    folder = input("Write the path of the folder here: ")

    modify(folder)
