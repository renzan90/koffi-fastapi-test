from fastapi import FastAPI
import json
import requests
import datetime

app = FastAPI()

req = {
    'scheme_code':int,
    'start_date': str,
    'end_date': str,
    'capital': float
}

@app.get("/profit")
async def calculate_MFreturns(scheme_code:int, start_date:str, end_date:str, capital:float):



    try:
        api = f'https://api.mfapi.in/mf/{scheme_code}'
        response = requests.get(api)
        dict_response = json.loads(response.text)

        dict_response = dict_response["data"]

        for onedict in dict_response:
            if onedict['date'] == start_date:
                start_NAV = onedict['nav']
            if onedict['date'] == end_date:
                end_NAV = onedict['nav']
        
        #return start_NAV, end_NAV
        initial_alloted_units = float(capital/start_NAV)

        val_of_units_on_redemption_date = initial_alloted_units*end_NAV

        final_profit = val_of_units_on_redemption_date - capital

        return final_profit
    
    except Exception as e:
        print(e)