from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router import api

description = """
------------------------------
**Username and password for Admin**
* Login: **admin**
* Parol: **admin123**
------------------------------
"""

app = FastAPI(
    description=description,
    contact={
        'name': "Asilbek Tojialiyev's telegram account url for questions",
        'url': 'https://t.me/tojaliyev13',
    },
    docs_url='/',
    redoc_url='/redoc',
)

app.include_router(api)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )


# pip install passlib[bcrypt]
# pip install python-jose
