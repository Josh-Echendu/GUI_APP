import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive: # we use a read mode('r'), when we want to see the content of the zip file
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive(r"\Users\hp\Music\pythonprojects\Python for Image and Video Processing with OpenCV\todoapp\GUI\files\compressed.zip", r"\Users\hp\Music\pythonprojects\Python for Image and Video Processing with OpenCV\todoapp\GUI\files")
    
    