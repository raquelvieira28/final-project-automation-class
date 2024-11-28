import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clicar_botao(self, seletor, tipo_seletor):
        time.sleep(2)
        if tipo_seletor == "id":
            botao = self.wait.until(EC.element_to_be_clickable((By.ID, seletor)))
        elif tipo_seletor == "css":
            botao = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, seletor)))
        botao.click()

    def preencher_campo(self, campo_id, valor, click_duplo=False):
        campo = self.wait.until(EC.element_to_be_clickable((By.ID, campo_id)))
        if click_duplo:
            actions = ActionChains(self.driver)
            actions.double_click(campo).perform()
        campo.clear()
        campo.send_keys(valor)

    def obter_texto(self, seletor):
        elemento = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
        texto = elemento.text
        texto_sem_timestamp = texto.split('.')[0] + texto[texto.index(" INFO"):]  # Ajuste para remover milissegundos
        return texto_sem_timestamp

    def verificar_texto_ignorando_timestamp(self, texto_obtido, texto_esperado):
        texto_obtido_sem_timestamp = " ".join(texto_obtido.split(" ")[1:])
        texto_esperado_sem_timestamp = " ".join(texto_esperado.split(" ")[1:])
        assert texto_obtido_sem_timestamp == texto_esperado_sem_timestamp, \
            f"Texto esperado não encontrado. Obtido: '{texto_obtido}', Esperado: '{texto_esperado}'"

    def construir_texto_esperado(self, mensagem, **kwargs):
        hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{hora_atual} {mensagem.format(**kwargs)}"
