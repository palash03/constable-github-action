import requests
from constants import FIREBASE_BASE_URL
import json

class Badge:
    def get_shield_url(self, _path: str, grade: str) -> str:   
        """
        _path: username/repositoryname/branch 
        e.g: ayushjain94/constable/master
        grade: A+
        """     

        payload = {"grade": grade}
        url = FIREBASE_BASE_URL + '/' +_path + '.json'
        r = requests.put(url, data = json.dumps(payload)) 
        shield = "https://img.shields.io/badge/dynamic/json?label=Constable&query=$.grade&url={data_url}".format(data_url = url)
        return shield

        
