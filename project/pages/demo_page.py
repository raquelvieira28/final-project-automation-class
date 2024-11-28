from pages.base_page import BasePage

class DemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.student_nome_id = "student-nome"
        self.student_btn_id = "student-btn"
        self.student_id = "student-id"
        self.course_nome_id = "course-nome"
        self.course_btn_id = "course-btn"
        self.course_id = "course-id"
        self.discipline_nome_id = "discipline-nome"
        self.course_discipline_id = "course-discipline-id"
        self.subscribe_student_id = "subscribe-student-id"
        self.subscribe_discipline_id = "subscribe-discipline-id"
        self.form_button_css = ".form-group:nth-child({}) > #course-btn"
        self.result_text_css = ".py-p:nth-child(1)"

    def adicionar_estudante(self, nome):
        self.preencher_campo(self.student_nome_id, nome)
        self.clicar_botao(self.student_btn_id, "id")

    def adicionar_curso(self, nome, course_id, click_duplo=False):
        self.preencher_campo(self.course_nome_id, nome, click_duplo)
        self.clicar_botao(self.course_btn_id, "id")

    def inscrever_estudante_no_curso(self, student_id, course_id):
        self.preencher_campo(self.student_id, student_id)
        self.preencher_campo(self.course_id, course_id)
        self.clicar_botao(self.form_button_css.format(4), "css")

    def adicionar_materia(self, nome, course_id, click_duplo=False):
        self.preencher_campo(self.discipline_nome_id, nome, click_duplo)
        self.preencher_campo(self.course_discipline_id, str(course_id))
        self.clicar_botao(self.form_button_css.format(5), "css")

    def inscrever_estudante_na_materia(self, student_id, discipline_id):
        self.preencher_campo(self.subscribe_student_id, student_id)
        self.preencher_campo(self.subscribe_discipline_id, discipline_id)
        self.clicar_botao(self.form_button_css.format(6), "css")
