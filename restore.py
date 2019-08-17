import os
from shutil import copyfile

RequesterModalContainer = './app/resources/app/js/RequesterModalContainer.js'
RequesterModalContainerBackup = RequesterModalContainer + '.back'
print('* Restoring RequesterModalContainer.js')
if os.path.isfile(RequesterModalContainerBackup):
    os.remove(RequesterModalContainer)
    copyfile(RequesterModalContainerBackup, RequesterModalContainer)
    os.remove(RequesterModalContainerBackup)
    print('* Restored RequesterModalContainer.js')
else:
  print('RequesterModalContainer.js.back Not found!')

VendorShared = './app/resources/app/js/vendor-shared.js'
VendorSharedBackup = VendorShared + '.back'

print('* Restoring vendor-shared.js')
if os.path.isfile(VendorSharedBackup):
    os.remove(VendorShared)
    copyfile(VendorSharedBackup, VendorShared)
    os.remove(VendorSharedBackup)
    print('* Restored vendor-shared.js')
else:
  print('vendor-shared.js.back Not found!')