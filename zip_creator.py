import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive: #when you want to create a zip file you use a write mode("w")
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name )


if __name__ == "__main__":
    make_archive(filepaths=["gui.py", "guiB.py"], dest_dir="dest" )
    
#this is how you create a back end function, you create
# the function then you test the function with if
# statement above to run the function    