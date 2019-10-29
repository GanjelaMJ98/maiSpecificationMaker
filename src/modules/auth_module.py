from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.app import App
import time as t
import json

                                                    # Размер окна
Config.set('graphics','resizable', 0)
Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 400)

pars_string = None                                  # Информация о учетных записях в JSON
log_path = None                                     # Путь до журнала безопасности
user_name = None                                    # Имя пользователя/Login
user_status = None                                  # Флаг привилегии

def authentication(path_config = "config.json", path_log = "auth.log", test = None):

    if test is not None:
        return "Pavel", "Test"

    global user_name
    global user_status
    global log_path
    global pars_string
                                                    # парсинг JSON
    log_path = path_log
    file = open(path_config,"r+")
    pars_string = json.load(file)
                                                    # Запуск модуля
    AuthenticationApp().run()
                                                    # Возврат логина и флага в случае успешной аутентификации
    if user_name is None or user_status is None:
        return 0,0
    else:
        return user_name,user_status

class AuthenticationApp(App):
    login = None                                    # Логин
    password = None                                 # Пароль
    N = 0                                           # Счетчик попыток входа в систему


    def add_login(self):                            # Чтение логина и пароля \ проверка на пустоту
        self.login = self.txt_login.text
        if self.login != "":
            return 0
        else:
            return 1

    def add_password(self):
        self.password = self.txt_password.text
        if self.password != "":
            return 0
        else:
            return 1 

    def check(self,login,password):                 # Сравнение введенных данных с записями в файле
        i = 0
        global pars_string
        while i < len(pars_string["whitelist"]):
            if login == pars_string["whitelist"][i]["login"] and password == pars_string["whitelist"][i]["password"]:
                return pars_string["whitelist"][i]["status"]
            else:
                i=i+1
        return 1

    def start(self,instance):                       # Обработчик кнопки
        global user_name
        global user_status
        log = open(log_path, 'a')
        if self.N < 2:
            if self.add_login() == 0 and self.add_password() == 0:
                status = self.check(self.login,self.password)
                if(status != 1):
                    self.info.text = "Ok"
                    log.write(str(t.ctime(t.time())) + "\tLog: {0:<15} Pass: {1:<15} {2:10}\n".format(self.login,self.password,status))
                    user_name = self.login
                    user_status = status
                    AuthenticationApp().stop()
                else:                               # Пользователь не найден TODO: Уведомление "User not found"
                    self.info.text = "Error"
                    log.write(str(t.ctime(t.time())) + "\tLog: {0:<15} Pass: {1:<15} {2:10}\n".format(self.login, self.password,"ERROR"))
                    self.N += 1
                return 1
            else:                                   # Отсутсвуют логин и пароль TODO: Уведомление "Error, login or password incorrect"
                self.info.text = "Error"
                self.N += 1
        else:                                       # Более 3х попыток
            self.info.text = "FATAL ERROR"
            log.write(str(t.ctime(t.time())) + "\tLog: {0:<15} Pass: {1:<15} {2:10}\n".format(self.login, self.password,"ERROR"))
            AuthenticationApp().stop()
            return 1

                                                    # Checkbox с возможностью отображения введённого пароля
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.txt_password.password = False
        else:
            self.txt_password.password = True
        
    def build(self):                                # Отрисовка виджетов
        al = AnchorLayout(padding = 25)
        bl = BoxLayout(orientation = 'vertical', size_hint = [.7,.7], spacing = 5)

        # lable Login
        self.lbl_login = Label(text = "Login" , text_size = (400 -50,30))
        bl. add_widget(self.lbl_login)

        # text Login
        self.txt_login = TextInput(multiline=False)
        bl.add_widget(self.txt_login)

        # lable Password
        self.lbl_password = Label(text = "Password",text_size = (400 -50,30))
        bl. add_widget(self.lbl_password)

        # text Password
        self.txt_password = TextInput(multiline=False,password = True)
        bl.add_widget(self.txt_password)

        # footer
        bl_start = BoxLayout(orientation='horizontal', )

        # checkbox
        self.checkbox = CheckBox()
        self.checkbox.bind(active=self.on_checkbox_Active)
        bl_start.add_widget(self.checkbox)

        # info
        self.info = Label()
        bl_start.add_widget(self.info)

        # button Start
        self.btn_start = Button(text = 'Start',on_press = self.start)
        bl_start.add_widget(self.btn_start)
        bl.add_widget(bl_start)

        al.add_widget(bl)

        return al

#if __name__ == "__main__":
    #module("config.json","log.txt")