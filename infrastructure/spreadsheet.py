from dataclasses import asdict

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("./client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("kurashiru_fav_recipe").sheet1


def update(recipes):
    columns = list(asdict(recipes[0]).keys())
    init(columns)

    urls = set(sheet.col_values(1)[1:])
    row_index = len(urls) + 2
    for recipe in recipes:
        if recipe.url not in urls:
            row = [asdict(recipe)[c] for c in columns]
            sheet.insert_row(row, row_index)
            row_index += 1


def init(columns):
    if sheet.row_values(1):
        return

    sheet.insert_row(columns, 1)
