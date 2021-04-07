import os
import cv2
from shutil import copyfile

DOCUMENTS_WHATS_ = "C:\\Users\\victor.macedo\\Documents\\whats\\"
DOCUMENTS_WHATS_UNIQUE_ = "C:\\Users\\victor.macedo\\Documents\\whats\\unique-file\\"

all_files = os.listdir(DOCUMENTS_WHATS_)

for file in [file for file in all_files if '-STICKER-' not in file]:
    if file != 'unique-file':
        os.remove(DOCUMENTS_WHATS_ + file)

files_with_sticker_in_name = [file for file in all_files if '-STICKER-' in file]

for file in files_with_sticker_in_name:
    split_file_name = file.split(sep=".")
    os.rename(DOCUMENTS_WHATS_ + file, DOCUMENTS_WHATS_ + split_file_name[0] + ".jpeg")

unique_stikers = os.listdir(DOCUMENTS_WHATS_UNIQUE_)
images_read = [cv2.imread(DOCUMENTS_WHATS_UNIQUE_ + file) for file in unique_stikers]

for idx, file in enumerate(files_with_sticker_in_name):
    print(str(idx) + "/" + str(len(files_with_sticker_in_name)))
    has_image = False
    image_1 = cv2.imread(DOCUMENTS_WHATS_ + file)
    for image in images_read:
        try:
            diff = cv2.subtract(image_1, image)
            has_image = not diff.any()
            if has_image:
                break
        except:
            has_image = True
            break
    if not has_image:
        images_read.insert(0, cv2.imread(DOCUMENTS_WHATS_ + file))
        copyfile(DOCUMENTS_WHATS_ + file, DOCUMENTS_WHATS_UNIQUE_ + file)

unique_stikers = os.listdir(DOCUMENTS_WHATS_UNIQUE_)

for idx, file in enumerate(unique_stikers):
    os.rename(DOCUMENTS_WHATS_UNIQUE_ + file, DOCUMENTS_WHATS_UNIQUE_ + str(idx + 1) + ".jpeg")

unique_stikers = os.listdir(DOCUMENTS_WHATS_UNIQUE_)

images_read = [cv2.imread(DOCUMENTS_WHATS_ + file) for file in files_with_sticker_in_name]

for idx, image_u in enumerate(unique_stikers):
    print(str(idx) + "/" + str(len(unique_stikers)))
    image_1 = cv2.imread(DOCUMENTS_WHATS_UNIQUE_ + image_u)
    count = 0
    for idx_i, image in enumerate(images_read):
        if image is None:
            continue
        try:
            diff = cv2.subtract(image_1, image)
            equals_image = not diff.any()
            if equals_image:
                count = count + 1
        except:
            print("Erro" + str(idx_i))
    split_file_name = image_u.split(sep=".")
    os.rename(DOCUMENTS_WHATS_UNIQUE_ + image_u,DOCUMENTS_WHATS_UNIQUE_ + str(count) + "_" + split_file_name[0] + ".jpeg")