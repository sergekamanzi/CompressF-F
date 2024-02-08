import os
import tarfile
import zipfile
from datetime import datetime

def get_filename(path, format):
    if format == 'tgz':
        dt = datetime.now().strftime("%Y_%m_%d")
        return f"{path}_{dt}.tgz"  
    else:
        return f"{path}.{format}"

def make_archive(path, format):
    filename = get_filename(path, format)
    print(f"Creating {filename}") 
    
    if format == 'zip':
        zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
        zipdir(path, zipf)
        zipf.close()
        
    elif format == 'tgz':
        tarf = tarfile.open(filename, 'w:gz')
        tarf.add(path)
        tarf.close()
        
    print(f"Compression of {path} to {filename} completed successfully!")
        
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
        
if __name__ == '__main__':
    
    path = input("Enter folder path to compress: ")
    formats = ['zip', 'tgz']
    
    print("Select compression format:")
    for i, f in enumerate(formats):
        print(f"{i}: {f}")
        
    format_idx = int(input("Enter option number: "))
    format = formats[format_idx]
    
    make_archive(path, format)
