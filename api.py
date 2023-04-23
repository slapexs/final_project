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

class search_filter(BaseModel):
    sector: int
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
def findCompanyInCluster(cluster_id: str, sector = 5) -> list:
    north = ['กำแพงเพชร', 'เชียงราย','เชียงใหม่', 'ตาก', 'น่าน', 'พะเยา', 'พิจิตร', 'พิษณุโลก', 'เพชรบูรณ์', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'สุโขทัย', 'อุตรดิตถ์']
    east = ['จันทบุรี', 'ฉะเชิงเทรา', 'ชลบุรี', 'ตราด', 'นครนายก', 'ปราจีนบุรี', 'พัทยา', 'ระยอง', 'สระแก้ว']
    north_east = ['กาฬสินธุ์','ขอนแก่น','ชัยภูมิ','นครพนม','นครราชสีมา','บึงกาฬ','บุรีรัมย์','มหาสารคาม','มุกดาหาร','ยโสธร','ร้อยเอ็ด','เลย','ศรีสะเกษ','สกลนคร','สุรินทร์','หนองคาย','หนองบัวลำภู','อำนาจเจริญ','อุดรธานี','อุบลราชธานี']
    central = ['กรุงเทพมหานคร','กาญจนบุรี','ชัยนาท','นครปฐม','นครสวรรค์','นนทบุรี','ปทุมธานี','พระนครศรีอยุธยา','ราชบุรี','ลพบุรี','สมุทรปราการ','สมุทรสงคราม','สมุทรสาคร','สระบุรี','สิงห์บุรี','สุพรรณบุรี','อ่างทอง','อุทัยธานี']
    south = ['สุราษฎร์ธานี','ชุมพร','นครศรีธรรมราช','นราธิวาส','ประจวบคีรีขันธ์','ปัตตานี','พัทลุง','เพชรบุรี','ยะลา','สงขลา','สุราษฎร์ธานี','ประจวบคีรีขันธ์','หาดใหญ่', 'กระบี่', 'ตรัง', 'พังงา', 'ภูเก็ต', 'ระนอง', 'สตูล']
    summary = [north, east, north_east, central, south]
    if sector >= 5:
        company_in_cluster = client['final_project']['companies'].find(
            filter={'cluster': cluster_id},
            projection=project
        )
    else:
        company_in_cluster = client['final_project']['companies'].find(
            filter={'cluster': cluster_id, 'province_base': {'$in': summary[sector]}},
            projection=project
        )
    return list(company_in_cluster)

# Function search company filter by province
def findCompanyByProvince(province: str) -> list:
    company_in_province = client['final_project']['companies'].find(
        filter={'province_base': province},
        projection=project
    )
    return list(company_in_province)

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
async def searchAndResponseCompanyInCluster(request: search_filter):
    payload = {'keyword': request.keyword, 'sector': int(request.sector)}
    # Send data for calculate cosine similarity
    obj = Calculate_cosinesim(payload['keyword'], count_cluster, df_db)
    # Result cosine similarity values
    cosine_values = obj.response_cosine()
    # Response value
    response_data = findCompanyInCluster(str(cosine_values.index(max(cosine_values))), payload['sector'])
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

# Response get company filter ny province
@app.get('/company/province/{province}')
async def getCompanyByProvince(province:str):
    province_name = province
    return findCompanyByProvince(province_name)

# Function find company filter by sector [0-4]
def findCompanyBySector(sector):
    north = ['กำแพงเพชร', 'เชียงราย','เชียงใหม่', 'ตาก', 'น่าน', 'พะเยา', 'พิจิตร', 'พิษณุโลก', 'เพชรบูรณ์', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'สุโขทัย', 'อุตรดิตถ์']
    east = ['จันทบุรี', 'ฉะเชิงเทรา', 'ชลบุรี', 'ตราด', 'นครนายก', 'ปราจีนบุรี', 'พัทยา', 'ระยอง', 'สระแก้ว']
    north_east = ['กาฬสินธุ์','ขอนแก่น','ชัยภูมิ','นครพนม','นครราชสีมา','บึงกาฬ','บุรีรัมย์','มหาสารคาม','มุกดาหาร','ยโสธร','ร้อยเอ็ด','เลย','ศรีสะเกษ','สกลนคร','สุรินทร์','หนองคาย','หนองบัวลำภู','อำนาจเจริญ','อุดรธานี','อุบลราชธานี']
    central = ['กรุงเทพมหานคร','กาญจนบุรี','ชัยนาท','นครปฐม','นครสวรรค์','นนทบุรี','ปทุมธานี','พระนครศรีอยุธยา','ราชบุรี','ลพบุรี','สมุทรปราการ','สมุทรสงคราม','สมุทรสาคร','สระบุรี','สิงห์บุรี','สุพรรณบุรี','อ่างทอง','อุทัยธานี']
    south = ['สุราษฎร์ธานี','ชุมพร','นครศรีธรรมราช','นราธิวาส','ประจวบคีรีขันธ์','ปัตตานี','พัทลุง','เพชรบุรี','ยะลา','สงขลา','สุราษฎร์ธานี','ประจวบคีรีขันธ์','หาดใหญ่', 'กระบี่', 'ตรัง', 'พังงา', 'ภูเก็ต', 'ระนอง', 'สตูล']
    summary = [north, east, north_east, central, south]
    company = client['final_project']['companies'].find(
        filter={'province_base': {'$in': summary[sector]}},
        projection=project
    )
    return list(company)
    
# Find company by sector
@app.get('/company/sector/{sector}')
async def getCompanyBySector(sector):
    sector_index = int(sector)
    return findCompanyBySector(sector_index)

# Response list of clusters
@app.get('/cluster')
async def responseListOfCluster():
    return {'clusters': clusters}