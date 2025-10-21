import json
 
from app.main import app

openapi_data = app.openapi()

with open("app/docs/api/openapi.json", "w") as f:
    json.dump(openapi_data, f, indent=2)

print("OpenAPI exportado com sucesso!")