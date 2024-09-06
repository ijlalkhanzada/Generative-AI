# Hello world with Fastapi
1. `poetry new fastapi-helloworld`
2. `cd fastapi-helloworld`
3. Select your project with VScode
4. open file `pyproject.toml`
```
[tool.poetry]
name = "fastapi-helloworld-online"
version = "0.1.0"
description = ""
authors = ["Sir Qasim <m.qasim077@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
5. install new packages in poetry project
    `poetry add fastapi "uivcorn[standard]"`
    ```
    [tool.poetry.dependencies]
    python = "^3.11"
    fastapi = "^0.110.0"
    uvicorn = {extras = ["standard"], version = "^0.29.0"}
    ```

5. create `main.py` location `fastapi_helloworld/main.py`
```
from fastapi import FastAPI


app  = FastAPI()

@app.get("/")
def index():
    return {"Hello": "world"}

@app.get("/piaic/")
def piaic():
    return {"organization": "piaic"}

```
6. run server
    `poetry run uvicorn fastapi_helloworld.main:app --reload`

7. `http://127.0.0.1:8000/`
    * `http://127.0.0.1:8000/piaic/`
8. `http://127.0.0.1:8000/docs`

9. write your own test
    * `test/test_main.py`
    ```
   from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app  = FastAPI()

@app.get("/" , response_class=HTMLResponse)
def index():
        return "<h1>Hello world</h1>"

@app.get("/piaic/")
def piaic():
    return {"organization": "piaic"}

@app.get("/ijlal/")
def ijlal():
    return {"Muhammad": "Khanzada"}

    ```

    10. `poetry run test -v`
