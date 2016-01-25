# Bilgi Shuttle API

<p align="center">
  <img src="http://autodevbot.com/assets/images/animated_gifs/Taff-shirt-3-29.gif" alt="mdegis"/>
</p>

Please note that it is API for Bilgi Shuttle cross-platform app. If you want to check web version please see [bilgi-shuttle-webapp](https://github.com/zebrasinpyjamas/bilgi-shuttle-webapp).

## Installation:

```
git clone https://github.com/mdegis/bilgi-shuttle.git
(venv) pip install -r requirements.txt
(venv) python manage.py runserver
```

## Usage:

- List of all nodes:

http://127.0.0.1:8000/index.json

- List of shuttle routes from specific node:

http://127.0.0.1:8000/santral.json
http://127.0.0.1:8000/dolapdere.json
http://127.0.0.1:8000/kustepe.json
http://127.0.0.1:8000/kabatas.json
http://127.0.0.1:8000/halicioglu.json
http://127.0.0.1:8000/pangalti.json
http://127.0.0.1:8000/mecidiyekoy.json

- [Advanced] Update database with text file:

http://127.0.0.1:8000/upload

    * Example format of text file:

    http://127.0.0.1:8000/static/raw.txt

## Licensing
Copyright 2016 Melih Değiş

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [LICENSE.md](https://github.com/mdegis/bilgi-shuttle/LICENSE.md) file.
