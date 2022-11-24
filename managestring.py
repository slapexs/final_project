from pythainlp.tokenize import word_tokenize
import requests


class Manage_string:
    def __init__(self, text:str) -> None:
        self.text = text

    # Cut string
    def cut_string(self, engine:str, keepWiteSpace:bool = False):
        self.engine = engine
        self.keepWhiteSpace = keepWiteSpace
        self.tokenize = word_tokenize(
            text=self.text,
            engine=self.engine,
            keep_whitespace=self.keepWhiteSpace
        )

        return self.tokenize
    
    # Cut string with aiforthai (TLex+)
    def cut_with_aiforthai(self, apikey:str, type:str):
        '''
        Aiforthai Algorithm:
            Machine learning ใช้อัลกอริทึม Conditional Random Fields

        apikey (str):
            Apikey ที่ได้จากเว็บ aiforthai เพื่อใช้ส่ง requests
        
        type (str):
            tlexplus -> ระบบตัดคําทีเล็กซ์พลัส (TLex+)

            tpos -> ระบบตัดคําทีเล็กซ์พลัสพลัส (TLex++) ตัดคำพร้อมทั้งกำกับหน้าที่ของคำ (Part of speech)
        '''
        self.tlexplus_url = f'https://api.aiforthai.in.th/{type}'
        self.headers = {'Apikey': apikey}
        self.tlexplus_params = {'text': self.text}
        self.tlexplus_response = requests.get(
            self.tlexplus_url,
            params=self.tlexplus_params,
            headers=self.headers
        )

        return self.tlexplus_response.json()
