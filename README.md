# Postman patcher

> Postman does not allow you to render javascript in your response previews, And thats for a good reason. they limit the scripts for security 

But what if you need to run your `react`, `vue` or any other javascript scripts. Saddly postman does not give you an option to allow or disallow javascript manually, So thats why this project exists
## Requirements

* Postman
* Python3

## Usage

```console
nikandlv@nikandlv.ir:~$ cd Postman
nikandlv@nikandlv.ir:~/Postman$ git clone https://github.com/nikandlv/postman-patcher.git .
nikandlv@nikandlv.ir:~/Postman$ python3 patch.py
Patching RequesterModalContainer.js
-- loading needle for RequesterModalContainer.js
-- loading patch for RequesterModalContainer.js
Backing up RequesterModalContainer.js -> RequesterModalContainer.js.back
Patching vendor-shared.js
-- loading needle for vendor-shared.js
-- loading patch for vendor-shared.js
-- loading needle 1 for vendor-shared.js
-- loading patch 1 for vendor-shared.js
Backing up vendor-shared.js -> vendor-shared.js.back
nikandlv@nikandlv.ir:~/Postman$
```
