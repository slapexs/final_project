from fastapi import FastAPI
from tfidf_cosine_similarity import Calculate_cosinesim
from pydantic import BaseModel
from pymongo import MongoClient
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

# Read value from .env file
config_env = dict(dotenv_values('.env'))

db_username = config_env['MONGODB_USERNAME']
db_password = config_env['MONGODB_PASSWORD']
db_cluster = config_env['CLUSTER']

# Connect to mongodb
client = MongoClient(f'mongodb+srv://{db_username}:{db_password}@{db_cluster}.qw7l19b.mongodb.net/?retryWrites=true&w=majority')

# All Clusters
clusters = list(client['final_project']['companies'].distinct('cluster'))

# For get data from mongodb assign to projection attr
project = {'_id': 0}

# Variable get all companies
res_allcompany = list(client['final_project']['companies'].find(projection=project))

df_db = pd.DataFrame(res_allcompany)
count_cluster = len(clusters)
class Search_body(BaseModel):
    keyword: str

# Instance FastAPI
app = FastAPI()

# Config middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ["GET", "POST"],
    allow_credentials = True,
    allow_headers = ['*']
)

# Root page
@app.get('/')
async def rootPage():
    return {
        'detail': 'This is home page API',
        'document': 'ดูข้อมูลการใช้งานได้ที่ /docs หรือไม่ก็ /redoc',
    }

# Function find company in cluster
def findCompanyInCluster(cluster_id: str) -> list:
    company_in_cluster = client['final_project']['companies'].find(
        filter={'cluster': cluster_id},
        projection=project
    )
    return list(company_in_cluster)

# Response Calculate cosine similarity
@app.post('/search')
async def search_body(req: Search_body):
    data = {'keyword': req.keyword}
    # Send data for calculate cosine similarity
    obj = Calculate_cosinesim(data['keyword'], count_cluster, df_db)
    # Result cosine similarity values
    cosine_values = obj.response_cosine()
    # Append values into list
    list_cosinesim = [v for v in cosine_values]
    # Response value
    return {
        'cosine_similarity': list_cosinesim,
        'max_cosine_similarity': max(cosine_values),
        'cluster': cosine_values.index(max(cosine_values))
    }

# Response calculate cosine similarity and then response company in cluster
@app.post('/searchcompany')
async def searchAndResponseCompanyInCluster(request: Search_body):
    payload = {'keyword': request.keyword}
    # Send data for calculate cosine similarity
    obj = Calculate_cosinesim(payload['keyword'], count_cluster, df_db)
    # Result cosine similarity values
    cosine_values = obj.response_cosine()
    # Response value
    response_data = findCompanyInCluster(str(cosine_values.index(max(cosine_values))))
    return response_data

# Response get all companies from mongodb
@app.get('/allcompanies')
async def responseAllCommpany():
    return res_allcompany
    
# Response get company in cluster
@app.get('/company/{cluster}')
async def getCompanyByCluster(cluster: str):
    cluster_id = cluster
    return findCompanyInCluster(cluster_id)

# Response list of clusters
@app.get('/cluster')
async def responseListOfCluster():
    return {'clusters': clusters}