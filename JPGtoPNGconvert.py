import sys
import os
from PIL import Image

if __name__ == '__main__':

    source_file = sys.argv[1]
    target_file = sys.argv[2]
    current_dir = os.getcwd()
    print(f'current_dir---> {current_dir}')
    path_target= os.path.join(current_dir, target_file)
    print(f'path_target---> {path_target}')
    if os.path.isdir(path_target):
        print('path exists')
    else:
        print('path does not exist')
        os.makedirs(path_target)

    path_source = os.path.join(current_dir, source_file)
    print(f'path_source---> {path_source}')
    if not os.path.isdir(path_source):
        print('Source path does not exist')
    else:
        print('path exists')
        image_list = []
        for item in os.listdir(path_source):
            image_list.append(item)
        print(f'image_list---> {image_list}')

        path_source_list = []

        for item in image_list:
            path_source_list.append(os.path.join(path_source, item))

        print(f'path_source_list---> {path_source_list}')
        png_image_list = image_list[:]
        png_image_list = [item.replace('jpg', 'png') for item in png_image_list]
        print(f'png_image_list_source---> {png_image_list}')

        path_target_list = []
        for item in png_image_list:
            path_target_list.append(os.path.join(path_target,item))

        print(f'path_target_list---> {path_target_list}')

        tuppled_list = []
        tuppled_list = list(zip(path_source_list, path_target_list))
        print(f'tuppled_list---> {tuppled_list}')


        for item in tuppled_list:
            print(item[0])
            print(item[1])
            img = Image.open(item[0])
            img.save(item[1], 'png')

    print('done with the transfer of file with png format.')

