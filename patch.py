import os.path
from shutil import copyfile
import fileinput

RequesterModalContainer = './app/resources/app/js/RequesterModalContainer.js'
RequesterModalContainerBackup = RequesterModalContainer + '.back'
print('Patching RequesterModalContainer.js')
if os.path.isfile(RequesterModalContainer):
  print('-- loading needle for RequesterModalContainer.js')
  with open('./patch/app/resources/app/js/RequesterModalContainer.js.needle', 'r') as file:
      requester_modal_container_needle = file.read()
  print('-- loading patch for RequesterModalContainer.js')
  with open('./patch/app/resources/app/js/RequesterModalContainer.js.patch', 'r') as file:
      requester_modal_container_patch = file.read()
  print('Backing up RequesterModalContainer.js -> RequesterModalContainer.js.back')
  copyfile(RequesterModalContainer, RequesterModalContainerBackup)
  for line in fileinput.input([RequesterModalContainer], inplace=True):
    print(line.replace(requester_modal_container_needle, requester_modal_container_patch), end='')
else:
  print('RequesterModalContainer.js Not found!')