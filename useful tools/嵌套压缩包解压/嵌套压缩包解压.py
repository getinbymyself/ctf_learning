import zipfile  
import tarfile  
import gzip
import py7zr
import os
def unzip_file(zip_file_path, destination_path):  
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:  
        zip_ref.extractall(destination_path)  
        file_names = zip_ref.namelist()  
    return file_names  
def extract_tar_gz(tar_gz_file, destination_folder):  
    with tarfile.open(tar_gz_file, 'r:gz') as tar:  
        tar.extractall(destination_folder)  
        extracted_files = tar.getnames()  
    return extracted_files 
def extract_tar(tar_file, destination_folder):  
    with tarfile.open(tar_file, 'r') as tar:  
        tar.extractall(destination_folder)  
        extracted_files = tar.getnames()  
    return extracted_files
def extract_7z(archive_file, destination_folder):  
    with py7zr.SevenZipFile(archive_file, mode='r') as archive:  
        archive.extractall(path=destination_folder)  
        extracted_files = archive.getnames()  
    return extracted_files
def delete_file(file_path):
    if os.path.exists(file_path):  
        os.remove(file_path)
#路径
part_of_file_path='/mnt/d/下载/unzip/'
destination_path = '/mnt/d/下载/unzip'
next='shell1.tar.gz'
for i in range(2):
    file_path = part_of_file_path + next
    if file_path.endswith("zip"):
        unzipped_files = unzip_file(file_path, destination_path)  
        next=unzipped_files[0]  
    elif file_path.endswith("gz"):    
        extracted_files = extract_tar_gz(file_path, destination_path)  
        next=extracted_files[0]
    elif file_path.endswith("tar"):
        extracted_tar_files = extract_tar(file_path, destination_path)  
        next=extracted_tar_files[0]
    elif file_path.endswith("7z"):    
        extracted_7z_files = extract_7z(file_path, destination_path)  
        next=extracted_7z_files[0]
    else:
        break
    #delete_file(file_path)