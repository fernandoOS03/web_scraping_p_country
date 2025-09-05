import gspread
from oauth2client.service_account import ServiceAccountCredentials

   #--------------------------consideraciones antes de comenzar--------------------------
   #Cada vez que se vaya a crear un proyecto, se tiene que compartir con la cuenta de servicio de google cloud
   #Siempre cambiar el nombre de la hoja en la que se esta trabajando
    
scope =["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"]

credetials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

cliente = gspread.authorize(credetials)

sheet = cliente.open("population by country").sheet1
sheet2 = cliente.open("population by country").worksheet("gdp by country")
sheet3 = cliente.open("population by country").worksheet("retail_gators")


# primera_fila = sheet.row_values(1)
# primera_fila = sheet.row_values(1)
# print(f"Primera fila: {primera_fila}")