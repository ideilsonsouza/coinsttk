import requests
import json
from utils.message import Message

class AppRequest:
    def __init__(self):
        self.data_response = None
        self.response_obj = None

    def make_headers(self, isJson=True, files=None):
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'COINS TTK 1.0 - BY Ideilson Souza',
        }

        if isJson and not files:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        return headers

    def execute(self, method='get', path=None, data=None, files=None, timeout=10):
        if not path:
            Message.error("URL não especificada.")
            return None

        headers = self.make_headers(files=files)
        json_data = None
        if data and not files:
            json_data = json.dumps(data)

        try:
            method = method.lower()
            if method == 'get':
                response = requests.get(url=path, headers=headers, timeout=timeout)
            elif method == 'post':
                response = requests.post(url=path, headers=headers, data=json_data, files=files, timeout=timeout)
            elif method == 'put':
                response = requests.put(url=path, headers=headers, data=json_data, files=files, timeout=timeout)
            elif method == 'delete':
                response = requests.delete(url=path, headers=headers, timeout=timeout)
            else:
                Message.error(f"Método HTTP {method} não reconhecido. Usando GET por padrão.")
                response = requests.get(url=path, headers=headers, timeout=timeout)

            self.data_response = response.text
            self.response_obj = response  # Guarda a resposta completa para outros usos, como status
            return self.data_response

        except requests.RequestException as req_err:
            Message.error(f"Erro na requisição {method.upper()} para {path}: {req_err}")
        except Exception as e:
            Message.error(f"Ocorreu um erro inesperado: {e}")
        return None

    @property
    def response(self) -> dict:
        try:
            return json.loads(self.data_response) if self.data_response else {}
        except json.JSONDecodeError:
            Message.error("Erro ao decodificar a resposta como JSON.")
            return {}

    @property
    def response_status(self) -> int:
        return self.response_obj.status_code if self.response_obj else 0
