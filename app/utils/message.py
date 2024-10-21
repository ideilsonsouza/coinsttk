from PyQt5.QtWidgets import QMessageBox

class Message:
    
    @staticmethod
    def show(message, title='Mensagem', icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(buttons)
        return msg_box.exec_()
    
    @staticmethod
    def error(message, title='Error'):
        return Message.show(message=message, title=title, icon=QMessageBox.Warning, buttons=QMessageBox.Ok)
    
    @staticmethod
    def success(message, title='Sucesso'):
        return Message.show(message=message, title=title, icon=QMessageBox.Information, buttons=QMessageBox.Ok)
    
    @staticmethod
    def warning(message, title='Aviso'):
        return Message.show(message=message, title=title, icon=QMessageBox.Warning, buttons=QMessageBox.Ok)
    
    @staticmethod
    def question(message, title='Confirmação'):
        return Message.show(message=message, title=title, icon=QMessageBox.Question, buttons=QMessageBox.Yes | QMessageBox.No)