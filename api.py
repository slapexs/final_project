from fastapi import FastAPI
from tfidf_cosine_similarity import Calculate_cosinesim
import pandas as pd
from pydantic import BaseModel

df = pd.read_csv('./document/clustered_company.csv')

class Search_body(BaseModel):
    keyword: str

app = FastAPI()

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

    obj = Calculate_cosinesim(data['keyword'], 7, df)
    cosine_values = obj.response_cosine()
    list_cosinesim = [v for v in cosine_values]
    return {
        'cosine_similarity': list_cosinesim,
        'max_cosine_similarity': max(cosine_values),
        'cluster': cosine_values.index(max(cosine_values))
    }
    