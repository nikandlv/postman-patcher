# Postman patcher

> Postman does not allow you to render javascript in your response previews, And thats for a good reason. they limit the scripts for security 

But what if you need to run your `react`, `vue` or any other javascript scripts. Saddly postman does not give you an option to allow or disallow javascript manually, So thats why this project exists

## Requirements

* Postman ^7.6.0
* Python3
* Mac or Linux versions

## Older versions

You can find the patcher for older versions of postman in their own release branch

## Patch it

```console
nikandlv@nikandlv.ir:~$ cd Postman
nikandlv@nikandlv.ir:~/Postman$ git clone https://github.com/nikandlv/postman-patcher.git
nikandlv@nikandlv.ir:~/Postman$ mv postman-patcher/* .
nikandlv@nikandlv.ir:~/Postman$ python3 patch.py
Patching RequesterModalContainer.js
-- loading needle for RequesterModalContainer.js
-- loading patch for RequesterModalContainer.js
Backing up RequesterModalContainer.js -> RequesterModalContainer.js.back
* applying patch on RequesterModalContainer.js
Patching vendor-shared.js
-- loading needle for vendor-shared.js
-- loading patch for vendor-shared.js
-- loading needle 1 for vendor-shared.js
-- loading patch 1 for vendor-shared.js
Backing up vendor-shared.js -> vendor-shared.js.back
* applying patch on vendor-shared.js
* applying patch 1 on vendor-shared.js
nikandlv@nikandlv.ir:~/Postman$
```

## Enable it

`File > Settings > USER INTERFACE > [Disable Sandbox] Allow javascript in previews (requires restart)`



## Restart and enjoy

## Images

![Settings](./settings.png)

#### Before

![Before](./before.png)

#### After

![After](./after.png)


## Restore

```console
nikandlv@nikandlv.ir:~/Postman$ python3 restore.py
* Restoring RequesterModalContainer.js
* Restored RequesterModalContainer.js
* Restoring vendor-shared.js
* Restored vendor-shared.js
nikandlv@nikandlv.ir:~/Postman$
```

# Important Note

This project is just a feature that we all need but they havent implemented this yet. theres also an issue from may that havent got anywhere

#### Postman updates itself so you probably need to patch again after an update

## Todo
- add windows support
