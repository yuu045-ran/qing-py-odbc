import logging
import pypyodbc as pyodbc
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
 
  #  conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:qing-sql-server.database.windows.net,1433;Database=qing-db;Uid=yuran;Pwd=Yuukochan!1979;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:qing-server-pe.database.windows.net,1433;Database=qing-db;Uid=yuran;Pwd=Yuukochan1979;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
   
    cursor=conn.cursor()
    cursor.execute("SELECT @@version;")
    result=""
    row = cursor.fetchone()
    result = result + " " + row[0]
    #row = cursor.fetchone()
    
    

    print(result)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {row}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
