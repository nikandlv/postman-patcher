import os.path
from shutil import copyfile
import fileinput

# Patch RequesterModalContainer
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

# Patch 
VendorShared = './app/resources/app/js/vendor-shared.js'
VendorSharedBackup = VendorShared + '.back'
print('Patching vendor-shared.js')
if os.path.isfile(VendorShared):

  print('-- loading needle for vendor-shared.js')
  with open('./patch/app/resources/app/js/vendor-shared.js.needle', 'r') as file:
      vendor_shared_needle = file.read()

  print('-- loading patch for vendor-shared.js')
  with open('./patch/app/resources/app/js/vendor-shared.js.patch', 'r') as file:
      vendor_shared_patch = file.read()
  
  print('-- loading needle 1 for vendor-shared.js')
  with open('./patch/app/resources/app/js/vendor-shared.js.1.needle', 'r') as file:
      vendor_shared_needle_1 = file.read()

  print('-- loading patch 1 for vendor-shared.js')
  with open('./patch/app/resources/app/js/vendor-shared.js.1.patch', 'r') as file:
      vendor_shared_patch_1 = file.read()  

  print('Backing up vendor-shared.js -> vendor-shared.js.back')
  copyfile(VendorShared, VendorSharedBackup)

  for line in fileinput.input([VendorShared], inplace=True):
    print(line.replace(vendor_shared_needle, vendor_shared_patch), end='')

  for line in fileinput.input([VendorShared], inplace=True):
    print(line.replace(vendor_shared_needle_1, vendor_shared_patch_1), end='')

else:
  print('vendor-shared.js Not found!')