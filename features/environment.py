from selenium import webdriver
#from selenium import webdriver_manager
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
#service = Service(ChromeDriverManager().install())
#navegador = webdriver.Chrome(service=service)

# Inicio

def before_all(context):   # Antes de Tudo
    #Declarar o SE, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('Driver_Chrome_Manager/chromedriver.exe')

    # Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - Antes de Tudo')

# Fim
def after_all(context):     # Depois de tudo
    # Desligar / Destruir o objeto do SE
    context.driver.quit()










