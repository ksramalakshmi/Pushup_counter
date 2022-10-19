import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sheets_api.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Counter").sheet1

def entry(count):
    data = sheet.get_all_records()
    max_rows = len(sheet.get_all_values())

    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    insertRow = [date.isoformat(today), current_time, count]

    try:
        sheet.insert_row(insertRow, max_rows+1)  
    except:
        sheet.insert_row(insertRow, 1)  
    

