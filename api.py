from fastapi import FastAPI
from tfidf_cosine_similarity import Calculate_cosinesim
from pydantic import BaseModel
from pymongo import MongoClient
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv('MONGODB_USERNAME')
db_password = os.getenv('MONGODB_PASSWORD')
db_cluster = os.getenv('CLUSTER')

client = MongoClient(f'mongodb+srv://{db_username}:{db_password}@{db_cluster}.qw7l19b.mongodb.net/?retryWrites=true&w=majority')
db = client.test
filter={}

project = {'_id': 0}

result = client['final_project']['companies'].find(
  filter=filter,
  projection=project,
)

df_db = pd.DataFrame(list(result))
cluster = 7
class Search_body(BaseModel):
    keyword: str

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["GET", "POST"],
    allow_credentials = True,
    allow_headers = ['*']
)

@app.get('/')
async def rootPage():
    return {
        'detail': 'This is home page API',
        'document': 'ดูข้อมูลการใช้งานได้ที่ /docs หรือไม่ก็ /redoc',
    }


@app.post('/search')
async def search_body(req: Search_body):
    data = {
        'keyword': req.keyword
    }

    obj = Calculate_cosinesim(data['keyword'], cluster, df_db)
    cosine_values = obj.response_cosine()
    list_cosinesim = [v for v in cosine_values]
    return {
        'cosine_similarity': list_cosinesim,
        'max_cosine_similarity': max(cosine_values),
        'cluster': cosine_values.index(max(cosine_values))
    }
    