from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout 
import sys

class cadastrocliente(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(10,30,400,300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("cadastrar cliente")

        # GERENCIADOR DE LAYOUT VERTICAL 
        self.layout_v = QVBoxLayout()

        # labels para os dados do cliente
        self.label_nome = QLabel("nome do cliente:")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}") 

        self.label_email = QLabel("Email:")
        self.label_email.setStyleSheet("QLabel{font-size:12pt}") 
        
        self.label_telefone = QLabel("telefone:")
        self.label_telefone.setStyleSheet("QLabel{font-size:12pt}") 
        
        self.label_idade = QLabel("idade:")
        self.label_idade.setStyleSheet("QLabel{font-size:12pt}") 



        # LINEEDIT PARA O NOME DO CLIENTE
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_telefone = QLineEdit()
        self.edit_telefone.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_idade = QLineEdit()
        self.edit_idade.setStyleSheet("QLineEdit{font-size:12px}")

        self.button = QPushButton("cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red; color:white; font-size:12pt; font-weight:bold;}")

        # CHAMAR A FUNÇÃO CADASTRO DO CLIENTE AO CLICAR NO BOTÃO
        self.button.clicked.connect(cadastrar)

        # ADICIONAR O LABEL NOME E O LINEEDIT AO LAYOUT VERTICAL
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        self.layout_v.addWidget(self.label_email)
        self.layout_v.addWidget(self.edit_email)

        self.layout_v.addWidget(self.label_telefone)
        self.layout_v.addWidget(self.edit_telefone)

        self.layout_v.addWidget(self.label_idade)
        self.layout_v.addWidget(self.edit_idade)

        self.layout_v.addWidget(self.button)


        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)



app = QApplication(sys.argv)
# NSTANCIA DA CLASSE CADASTROCLIENTE PARA INICIAR A JANELA
tela = cadastrocliente()
# EXIBIR A TELA DURANTE A EXECUÇÃO
tela.show()
# AO CLICAR NO BOTAO FECHAR A TELA DEVE FECHAR A JANELA E SAIR DA MEMORIA
app.exec()


