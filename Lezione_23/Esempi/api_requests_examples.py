import requests
# va installato con 'pip install requests'
import json

if __name__ == "__main__":
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    # ESEMPIO DI GET
    response = requests.get(
        url="http://localhost:5000/libri",
        headers=headers
    )
    print("Risposta GET:", response.json())

    # ESEMPIO DI POST
    payload = {
        "nome": "Marco",
        "cognome": "Cascio"
    }

    # SENZA JSON DUMPS
    response_post = requests.post(
        url="http://localhost:5000/api/utenti",  # esempio di endpoint
        json=payload,
        headers=headers
    )

    print("Risposta POST:", response_post.json())

    # CON DUMPS
    response_post_dumps = requests.post(
        url="http://localhost:5000/api/utenti",  # esempio di endpoint
        data=json.dumps(payload),
        headers=headers
    )

    print("Risposta POST:", response_post_dumps.json())

