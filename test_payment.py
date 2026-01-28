import requests
import json
import sys

URL = "http://localhost:8000/api/payment"

payloads = [
    # Teste 1: Padrão (9 digitos, float)
    {
        "description": "Phone 9 digits, Amount Float",
        "data": {
            "amount": 9.00,
            "method": "mbway",
            "payer": {
                "name": "Teste Bot",
                "phone": "910000000", 
                "document": "999999990"
            }
        }
    },
    # Teste 2: Phone com 351
    {
        "description": "Phone 12 digits (351), Amount Float",
        "data": {
            "amount": 9.00,
            "method": "mbway",
            "payer": {
                "name": "Teste Bot",
                "phone": "351910000000", 
                "document": "999999990"
            }
        }
    },
    # Teste 3: Amount String
    {
        "description": "Phone 9 digits, Amount String",
        "data": {
            "amount": "9.00",
            "method": "mbway",
            "payer": {
                "name": "Teste Bot",
                "phone": "910000000", 
                "document": "999999990"
            }
        }
    }
]

print("--- Iniciando Simulação de Deploy ---")
success = False

for p in payloads:
    print(f"\nTentando: {p['description']}")
    try:
        r = requests.post(URL, json=p['data'], timeout=20)
        print(f"Status: {r.status_code}")
        try:
            resp_json = r.json()
            print(f"Response: {json.dumps(resp_json, indent=2)}")
            if r.status_code == 200 and resp_json.get('success'):
                print(">>> SUCESSO CONFIRMADO! <<<")
                success = True
                break
        except:
            print(f"Response Text: {r.text}")
    except Exception as e:
        print(f"Erro de Conexão: {e}")

if not success:
    print("\nXXX FALHA EM TODOS OS CENÁRIOS XXX")
    sys.exit(1)
else:
    print("\nSistema Validado. Pronto para Deploy.")
