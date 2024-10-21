from PyQt5.QtWidgets import QWidget
from ui.from_ttk import Ui_FormCalcTTK
from utils.message import Message
from utils.constant import LIST_COINS
from utils.requests import AppRequest
from utils.functions import convertPrince, converttk,formatted_coin
import json

class WindowTKK(QWidget, Ui_FormCalcTTK):
    
    def __init__(self, parent=None):
        super(WindowTKK, self).__init__(parent)
        self.setupUi(self)
        self.cbx_local_coin.addItems(LIST_COINS)
        self.cbx_prince_coin.addItems(LIST_COINS)
        self.btn_calc_coin.clicked.connect(self.action_calc)
    
    def getcoin(self, coins):
        requests = AppRequest()
        response = requests.execute('get',f'https://economia.awesomeapi.com.br/last/{coins}')
        return response
    
    
    def action_calc(self):
        if not self.cbx_local_coin.currentText().strip():
            Message.warning('Escolha a moeda local','Atenção')
            return
        
        if not self.cbx_prince_coin.currentText().strip():
            Message.warning('Escolha a moeda de cotação','Atenção')
            return
        
        if self.cbx_prince_coin.currentText().strip() == self.cbx_local_coin.currentText().strip():
            Message.warning('Falhar ao converte, Selecione pares diferentes','Atenção')
            return
            
        
        coins = f"{self.cbx_prince_coin.currentText().strip()}-{self.cbx_local_coin.currentText().strip()}"
        coins_name = f"{self.cbx_prince_coin.currentText().strip()}{self.cbx_local_coin.currentText().strip()}"
        
        # Faz a requisição para obter a cotação
        response = self.getcoin(coins)
        if response:
            try:
                # Converte a string JSON em dicionário
                response_dict = json.loads(response)
                
                # Usa coins_name para encontrar a cotação no JSON
                response_coins = response_dict.get(coins_name)
                
                if response_coins:
                    response_bid = response_coins['bid']
                    self.txt_prince.setText(
                        formatted_coin(self.cbx_local_coin.currentText(),response_bid)
                        )
                    
                    if not self.txt_ttk_coin.text().strip() or float(self.txt_ttk_coin.text()) == 0:
                        Message.error('Informe a quantidade de moedas ttk')
                        return
                    
                    total_ttk_convert = converttk(self.txt_ttk_coin.text())
                    total_coins = convertPrince(ttk=total_ttk_convert, rate=response_bid)
                    
                    self.txt_ttk_prince.setText(
                        formatted_coin(self.cbx_prince_coin.currentText(),total_ttk_convert)
                        )
                    
                    if self.calc_percent_ttk.isChecked():                   
                        self.txt_total_coin.setText(
                            formatted_coin(self.cbx_local_coin.currentText(),total_coins / 2)
                            )
                    else:
                        self.txt_total_coin.setText(
                            formatted_coin(self.cbx_local_coin.currentText(),total_coins)
                            )
                        
                    
                else:
                    Message.show(f"Cotação para {coins_name} não encontrada.")
            except json.JSONDecodeError:
                Message.show("Erro ao decodificar a resposta do servidor.")
        else:
            Message.show('Resposta não encontrada')
