import os
import zipfile
import sys
import shutil

# Usage: python3 merge.py <epub to merge into> <epub with proper nav> <output filename(without extension)>

customCSS = '''
.d.m1 {
    border: none !important;
    cursor: default !important;
    pointer-events: none !important;
}
'''

assert isinstance(sys.argv[3], str)
workingDirectory = str(os.getcwd())

files = {
    'toMerge': os.path.join(workingDirectory, sys.argv[1]),
    'index': os.path.join(workingDirectory, sys.argv[2])
}

assert os.path.exists(files.values)

for fileType, fileName in files.items():
    fileToUnzip = zipfile.ZipFile(fileName)
    fileToUnzip.extractall(fileType)
    os.remove(fileName)

nav = open(os.path.join(workingDirectory, 'index', 'OEBPS', 'nav.xhtml'), 'r')
toMergeNavFile = open(os.path.join(workingDirectory, 'toMerge', 'OEBPS', 'nav.xhtml'), 'w')
styleFile = open(os.path.join(workingDirectory, 'toMerge', 'OEBPS', 'mybook.css'), 'a+')

toMergeNavFile.write(nav.read().replace('href=\"page', 'href=\"mybook0'))
styleFile.write(customCSS)
nav.close()
toMergeNavFile.close()
styleFile.close()

def zip_dir(path):
    zf = zipfile.ZipFile(sys.argv[3] + '.epub'.format(path), 'w', zipfile.ZIP_DEFLATED)
   
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if file_name == '.DS_Store':
                continue
            relativePath = str(root).replace(path, '')
            zf.write(os.path.join(root, file_name), os.path.join(relativePath, file_name))

zip_dir(os.path.join(workingDirectory, 'toMerge'))

for folder in files.keys():
    shutil.rmtree(os.path.join(workingDirectory, folder))
