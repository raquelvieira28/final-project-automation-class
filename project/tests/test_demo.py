import time
import pytest
from selenium import webdriver
from pages.demo_page import DemoPage

class TestDemo:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.page = DemoPage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def acessar_pagina(self, url):
        self.driver.get(url)

    def test_demo(self):
        self.acessar_pagina("https://tdd-detroid.onrender.com/")
        time.sleep(10)

        # Teste 1: Adicionar estudante
        self.page.adicionar_estudante("douglas")
        texto_obtido = self.page.obter_texto(self.page.result_text_css)
        texto_esperado = self.page.construir_texto_esperado("INFO Added student id: 1, Name: {nome}", nome="douglas")
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)

        # Teste 2: Adicionar curso 1
        self.page.adicionar_curso("mat", 1)
        texto_obtido = self.page.obter_texto(self.page.result_text_css)
        texto_esperado = self.page.construir_texto_esperado("INFO Added course id: {course_id}, Nome: {nome}", course_id=1, nome="mat")
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)

        # Teste 3: Adicionar curso 2
        self.page.adicionar_curso("port", 2, click_duplo=True)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Added course id: {course_id}, Nome: {nome}", course_id=2, nome="port")
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)

        # Teste 4: Adicionar curso 3
        self.page.adicionar_curso("geo", 3, click_duplo=True)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Added course id: {course_id}, Nome: {nome}", course_id=3, nome="geo")
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)

        # Teste 5: Inscrever estudante no curso 1
        self.page.inscrever_estudante_no_curso(1,1)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Student id {student_id} subscribed to course id {course_id}", student_id=1, course_id=1)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado) 

        # Teste 6: Adicionar matéria 1 no curso 1
        self.page.adicionar_materia("mat",1)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Added discipline id: {discipline_id}, Name: {nome}, Course: {course_id}", discipline_id=1, nome="mat", course_id=1)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)

        # Teste 7: Adicionar matéria 2 no curso 1
        self.page.adicionar_materia("mat2", 1, click_duplo=True)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Added discipline id: {discipline_id}, Name: {nome}, Course: {course_id}", discipline_id=2, nome="mat2", course_id=1)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)
        
        # Teste 8: Adicionar matéria 3 no curso 1
        self.page.adicionar_materia("mat3", 1, click_duplo=True)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Added discipline id: {discipline_id}, Name: {nome}, Course: {course_id}", discipline_id=3, nome="mat3", course_id=1)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)
        
        # Teste 9: Inscrever estudante na matéria 1
        self.page.inscrever_estudante_na_materia(1,1)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(2)")
        texto_esperado = self.page.construir_texto_esperado("INFO Student id {student_id}, Name {nome} subscribed to discipline id {discipline_id}", student_id= 1, nome="douglas", discipline_id=1)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)
        
        # Teste 10: Inscrever estudante na matéria 2
        self.page.inscrever_estudante_na_materia(1,2)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(2)")
        texto_esperado = self.page.construir_texto_esperado("INFO Student id {student_id}, Name {nome} subscribed to discipline id {discipline_id}", student_id= 1, nome="douglas", discipline_id=2)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)

        # Teste 11: Inscrever estudante na matéria 3
        self.page.inscrever_estudante_na_materia(1,3)
        texto_obtido = self.page.obter_texto(".py-p:nth-child(1)")
        texto_esperado = self.page.construir_texto_esperado("INFO Student id {student_id}, Name {nome} subscribed to discipline id {discipline_id}", student_id= 1, nome="douglas", discipline_id=3)
        self.page.verificar_texto_ignorando_timestamp(texto_obtido, texto_esperado)



