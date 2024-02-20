import os
import shutil

shutil.rmtree('buttons')

for dirpath, dirnames, filenames in os.walk('assets'):
    if len(filenames) > 0:
        new_dir_path = '/'.join(dirpath.replace('assets', 'buttons').split('\\')[:-1])
        py_path = new_dir_path + '/assets_' + dirpath.replace('assets', 'buttons').split('\\')[-1] + '.py'
        if not os.path.exists(new_dir_path):
            os.mkdir(new_dir_path)
        with open(py_path, 'w', encoding='utf-8') as f:
            for filename in filenames:
                name = filename.split('.')[0]
                asset_path = dirpath.replace('\\', '/') + '/' + filename
                f.write(f"{name.upper().replace('-','_')} = '{asset_path}'\n")