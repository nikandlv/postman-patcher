print('Patching RequesterModalContainer.js')
for line in fileinput.input(['RequesterModalContainer.js'], inplace=True):
    print(line.replace('old stuff', 'shiny new stuff'), end='')