# Bilgi Shuttle API

<p align="center">
  <img src="http://autodevbot.com/assets/images/animated_gifs/Taff-shirt-3-29.gif" alt="mdegis"/>
</p>

Please note that it is API for Bilgi Shuttle cross-platform app.

- Web version: [bilgi-shuttle-webapp](https://github.com/bilgishuttle/bilgi-shuttle-webapp)
- iOS version: [bilgi-shuttle-ios](https://github.com/bilgishuttle/bilgi-shuttle-ios)
- Android version: [bilgi-shuttle-android](https://github.com/bilgishuttle/bilgi-shuttle-android)

## Installation:
``` bash
# Clone the Project
$ git clone https://github.com/bilgishuttle/bilgi-shuttle-api.git

# in Virtual Environment
$ pip install -r requirements.txt
$ python manage.py runserver
```

## Usage:
``` bash
## List of all nodes:
http://127.0.0.1:8000/index.json

## List of shuttle routes from specific node:
http://127.0.0.1:8000/santral.json
http://127.0.0.1:8000/dolapdere.json
http://127.0.0.1:8000/kustepe.json
http://127.0.0.1:8000/kabatas.json
http://127.0.0.1:8000/halicioglu.json
http://127.0.0.1:8000/pangalti.json
http://127.0.0.1:8000/mecidiyekoy.json

## Check database version for cache:
http://127.0.0.1:8000/database_check.json

## Fetch database:
http://127.0.0.1:8000/database_fetch_all.json

## [Advanced] Update database with text file:
http://127.0.0.1:8000/upload

## Example format of text file:
http://127.0.0.1:8000/static/raw.txt
```

## Licence

	Copyright [2016] [Melih Değiş]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
