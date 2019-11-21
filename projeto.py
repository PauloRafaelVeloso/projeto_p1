import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown

class FormularioDenuncia(Screen):
    sm = ScreenManager()
    Window.size = (1000,600)
    def __init__(self,**kwargs):
        super(FormularioDenuncia, self).__init__(**kwargs)

        def ArquivarDenuncia(self,*args):
            servico = str(entry_servico.text)
            entry_servico.text=''
            horario = str(entry_hora_ocorrido.text)
            entry_hora_ocorrido.text=''
            data = str(entry_data_ocorrido.text)
            entry_data_ocorrido.text=''
            descricao = str(entry_descricao.text)
            entry_descricao.text=''
            suspeitos = str(entry_suspeitos.text)
            entry_suspeitos.text=''

            arquivoUsuarios = open("Denuncias.txt","a")
            arquivoUsuarios.write('\nÓrgão: ')
            arquivoUsuarios.write(servico)
            arquivoUsuarios.write('\nHora do ocorrido: ')
            arquivoUsuarios.write(horario)
            arquivoUsuarios.write('\nData do ocorrido: ')
            arquivoUsuarios.write(data)
            arquivoUsuarios.write('\nDescrição do ocorrido: ')
            arquivoUsuarios.write(descricao)
            arquivoUsuarios.write('\nDescrição dos suspeitos: ')
            arquivoUsuarios.write(suspeitos)
            arquivoUsuarios.write('\n')
            arquivoUsuarios.close()

            

            ScreenManager()
            sm.current = 'menuprincipal'

        layout = GridLayout(cols=2, rows=10)
        self.add_widget(layout)
        label_escolher_servico = Label(text='Para qual serviço deseja cadastrar a denúncia?\n(Ex.: CELPE, Polícia Civil, Delegacia da mulher...)')
        layout.add_widget(label_escolher_servico)
        entry_servico = TextInput(font_size=25,multiline=False,write_tab=False)
        layout.add_widget(entry_servico)

        label_hora_ocorrido = Label(text='Horário em que o fato ocorreu:\n(separe utilizando ":")')
        layout.add_widget(label_hora_ocorrido)
        entry_hora_ocorrido = TextInput(font_size=25,multiline=False,write_tab=False,hint_text='hh:mm')
        layout.add_widget(entry_hora_ocorrido)

        label_data_ocorrido = Label(text='Data em que o fato ocorreu:\n(separe utilizando "/")')
        layout.add_widget(label_data_ocorrido)
        entry_data_ocorrido = TextInput(font_size=25,multiline=False,write_tab=False,hint_text='dd/mm/yyyy')
        layout.add_widget(entry_data_ocorrido)
        

        label_descricao = Label(text='Descreva o fato ocorrido de forma resumida: ')
        layout.add_widget(label_descricao)
        entry_descricao = TextInput(font_size=25,multiline=True,write_tab=False)
        layout.add_widget(entry_descricao)

        label_suspeitos = Label(text='Poderia descrever as características dos suspeitos?')
        layout.add_widget(label_suspeitos)
        entry_suspeitos = TextInput(font_size=25,multiline=True,write_tab=False)
        layout.add_widget(entry_suspeitos)
        
        
        

        
        
        
        label_organizar = Label(text='')
        layout.add_widget(label_organizar)
        bt_continuar_denun = Button(text='Finalizar Denúncia',background_color=[1,2,1,1], on_press = ArquivarDenuncia,pos_hint={'left':0.6},pos=[100,400],size_hint=(None,None), size=(200,90))
        layout.add_widget(bt_continuar_denun)
        
        
        
class MenuPrincipal(Screen):
    sm = ScreenManager()
    
    def __init__(self,**kwargs):
        super(MenuPrincipal, self).__init__(**kwargs)

        def MudarParaCadastroDenuncia(self,*args):
                ScreenManager()
                sm.current = 'formulariodenuncia'
        def FazerLogout(self,*args):
            username_OK = False
            password_OK = False
            ScreenManager()
            sm.current = 'telainicial'
            

        layout = GridLayout(cols=1, rows=10)
        self.add_widget(layout)

        label_atend = Label(text='Telefones de Emergência:\nPor favor, não passe trote a serviços de urgência/emergência!')
        layout.add_widget(label_atend)
        
        bt_bombeiros = Button(text='Corpo de Bombeiros (193)')
        '''bt_bombeiros.bind(on_press = )'''
        layout.add_widget(bt_bombeiros)
        
        bt_del_mulh = Button(text='Delegacia da mulher (180)')
        '''bt_del_mulh.bind(on_press = )'''
        layout.add_widget(bt_del_mulh)
        
        bt_samu = Button(text='SAMU (192)')
        '''bt_samu.bind(on_press = )'''
        layout.add_widget(bt_samu)
        
        bt_disk_den = Button(text='Disque-Denúncia (181)')
        '''bt_disk_den.bind(on_press = )'''
        layout.add_widget(bt_disk_den)
        
        bt_pol_civ = Button(text='Polícia Civil (197)')
        '''bt_pol_civ.bind(on_press = )'''
        layout.add_widget(bt_pol_civ)
        
        bt_pol_mil = Button(text='Polícia Militar (190)')
        '''bt_pol_mil.bind(on_press = bt_pol_mil)'''
        layout.add_widget(bt_pol_mil)
        
        bt_realizar_denuncia = Button(text='Gostaria de registrar uma denúncia?\n                  Clique aqui',background_color=[4,1,1,1])
        bt_realizar_denuncia.bind(on_press = MudarParaCadastroDenuncia)
        layout.add_widget(bt_realizar_denuncia)

        bt_logout = Button(text='Fazer logout')
        bt_logout.bind(on_press = FazerLogout)
        layout.add_widget(bt_logout)
                
        
class TelaLogin(Screen):
    sm = ScreenManager()
    
    def __init__(self,**kwargs):
        super(TelaLogin, self).__init__(**kwargs)

        def ValidarLogin(self,*args):
            username = str(entry_username.text)
            password = str(entry_senha.text)
            username_OK = False
            password_OK = False 

            for linha in open('Usuários.txt','r').readlines():
                login_info = linha.split(',')
                login_info[-1] = login_info[-1].strip()
                if len(login_info) > 1:
                    cont=0
                    unmasked = ''
                    unmasked_caractere = ''
                    
                    while cont < len(login_info):
                        unmasked_caractere = chr((int(login_info[cont]))^1144%1073)
                        unmasked += unmasked_caractere
                        cont+=1
                        
                        if username == unmasked:
                            username_OK = True
                        elif password == unmasked:
                            password_OK = True

            if username_OK and password_OK:
                
                entry_username.text=''
                entry_senha.text=''
                ScreenManager()
                sm.current = 'menuprincipal'
            else:
                invalid_user_or_password = Popup(auto_dismiss=True, title='Usuário e/ou senha inválidos!',size_hint=(None,None), size=(150,140))
                invalid_user_or_password.open()
                entry_username.text=''
                entry_senha.text=''
                fechar_popup = Button(text='OK',on_press=invalid_user_or_password.dismiss,size_hint=(None,None), size=(120,50))
                invalid_user_or_password.add_widget(fechar_popup)
                                
            #FIM DA VALIDAÇÃO DE LOGIN  
            

        layout = GridLayout(cols=2, rows=4)
        self.add_widget(layout)

        label_username = Label(text='Usuário: ')
        layout.add_widget(label_username)
        entry_username = TextInput(font_size=25,multiline=False,write_tab=False)
        layout.add_widget(entry_username)
        
        
        label_senha = Label(text='Senha: ')
        layout.add_widget(label_senha)
        entry_senha = TextInput(font_size=25,multiline=False, password=True,write_tab=False)
        
        layout.add_widget(entry_senha)

        label_organizar = Label(text='')
        layout.add_widget(label_organizar)

        bt_finalizar_login = Button(text='Entrar',background_color=[1,1,2,1])
        bt_finalizar_login.bind(on_press = ValidarLogin)
        layout.add_widget(bt_finalizar_login)
        

class TelaCadastro(Screen):
    sm = ScreenManager()

    def __init__(self,**kwargs):
        super(TelaCadastro, self).__init__(**kwargs)

        def ArquivarCadastro(self,*args):
                
            nome = str(entry_nome.text)
            entry_nome.text=''
            

            cpf = str(entry_CPF.text)
            entry_CPF.text=''
            

            email = str(entry_email.text)
            entry_email.text=''
            

            telefone = str(entry_telefone.text)
            entry_telefone.text=''
            
            
            data_de_nasc = str(entry_datanasc.text)
            entry_datanasc.text=''
            
            
            

            #Criptografia do login e senha
            login = str(entry_username.text)
            entry_username.text=''
            cript_Login = []
            for caractereL in login:
                maskL = str((ord(caractereL)^71)%1073)
                cript_Login.append(maskL)
            contL = 0
            final_cript_Login = ''
            while contL < len(cript_Login):
                final_cript_Login+= cript_Login[contL]
                final_cript_Login+=','
                contL+=1
            final_cript_Login = final_cript_Login[:-1]
            contL=0
            #Fim_login
            
            #Senha            
            senha = str(entry_password.text)
            entry_password.text=''
            cript_Senha = []
            for caractereS in senha:
                maskS = str((ord(caractereS)^71)%1073)
                cript_Senha.append(maskS)
            
            contS = 0
            final_cript_Senha = ''
            while contS < len(cript_Senha):
                final_cript_Senha += cript_Senha[contS]
                final_cript_Senha+=','
                contS+=1
            final_cript_Senha = final_cript_Senha[:-1]
            contS=0
            
            #Fim_senha
            
            
            
            arquivoUsuarios = open("Usuários.txt","a")
            arquivoUsuarios.write('\nNome: ')
            arquivoUsuarios.write(nome)
            arquivoUsuarios.write('\nCPF: ')
            arquivoUsuarios.write(cpf)
            arquivoUsuarios.write('\nE-mail: ')
            arquivoUsuarios.write(email)
            arquivoUsuarios.write('\nTelefone: ')
            arquivoUsuarios.write(telefone)
            arquivoUsuarios.write('\nData de nascimento: ')
            arquivoUsuarios.write(data_de_nasc)
            arquivoUsuarios.write('\nLogin:\n')
            arquivoUsuarios.write(final_cript_Login)
            arquivoUsuarios.write('\nSenha:\n')
            arquivoUsuarios.write(final_cript_Senha)
            arquivoUsuarios.write('\n')
            arquivoUsuarios.close()
            
            #Resetando as listas de criptografia de login e senha
            cript_Senha = []
            cript_Login = []
            final_cript_Login = ''
            final_cript_Senha = ''
            

            
            #Alternando para tela inicial após finalizar manuseio dos dados do cadastro
            ScreenManager()
            sm.current = 'telainicial'

            #FIM_ARQUIVAR_CADASTRO            


        
        layout = GridLayout(cols=2, rows=10)
        self.add_widget(layout)

        label_nome = Label(text='Nome completo: ')
        layout.add_widget(label_nome)
        entry_nome = TextInput(font_size=25,multiline=False,text='',write_tab=False)
        layout.add_widget(entry_nome)
        
        
        label_CPF = Label(text='CPF (apenas números): ')
        layout.add_widget(label_CPF)
        entry_CPF = TextInput(font_size=25,multiline=False,write_tab=False)
        
        layout.add_widget(entry_CPF)

        label_email = Label(text='E-mail: ')
        layout.add_widget(label_email)
        entry_email = TextInput(font_size=25,multiline=False,write_tab=False)
        layout.add_widget(entry_email)

        label_telefone = Label(text='Telefone (apenas números): ')
        layout.add_widget(label_telefone)
        entry_telefone = TextInput(font_size=25,multiline=False,write_tab=False)
        layout.add_widget(entry_telefone)

        label_datanasc = Label(text='Data de Nascimento:\n(Utilize "/" para separar) ')
        layout.add_widget(label_datanasc)
        entry_datanasc = TextInput(font_size=25,multiline=False,write_tab=False,hint_text='dd/mm/yyyy')
        layout.add_widget(entry_datanasc)
                      
        label_username = Label(text='Escolha um nome de usuário: ')
        layout.add_widget(label_username)
        entry_username = TextInput(font_size=25,multiline=False,write_tab=False)
        layout.add_widget(entry_username)

        label_password = Label(text='Digite uma senha: ')
        layout.add_widget(label_password)
        entry_password = TextInput(font_size=25,multiline=False,password=True,write_tab=False)
        layout.add_widget(entry_password)

        label_espaco = Label(text='')
        layout.add_widget(label_espaco)
        bt_cadastrar = Button(text='Finalizar', size_hint_x=None)
        bt_cadastrar.bind(on_press = ArquivarCadastro)
        layout.add_widget(bt_cadastrar)

       
        


class TelaInicial(Screen):
    sm = ScreenManager()
    
    def __init__(self,**kwargs):
        super(TelaInicial, self).__init__(**kwargs)          
        layout = BoxLayout(orientation ='horizontal')
        self.add_widget(layout)

        
        bt_fazer_login = Button(text='Já possui cadastro? Fazer login')
        bt_fazer_login.bind(on_press = self.MudarParaLogin)
        layout.add_widget(bt_fazer_login)
        
        bt_fazer_cadastro = Button(text='Cadastrar usuário')
        bt_fazer_cadastro.bind(on_press = self.MudarParaCadastro)
        layout.add_widget(bt_fazer_cadastro)

        

    def MudarParaCadastro(self,*args):
        ScreenManager()
        sm.current = 'telacadastro'

    def MudarParaLogin(self,*args):
        ScreenManager()
        sm.current = 'telalogin'


sm = ScreenManager()
sm.add_widget(TelaInicial(name='telainicial'))
sm.add_widget(TelaCadastro(name='telacadastro'))
sm.add_widget(TelaLogin(name='telalogin'))
sm.add_widget(MenuPrincipal(name='menuprincipal'))
sm.add_widget(FormularioDenuncia(name='formulariodenuncia'))
class ProjetoP1(App):
    def build(self):       
        return sm


ProjetoP1().run()



