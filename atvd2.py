class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos_lecionados = []

    def designar_curso(self, curso):
        self.cursos_lecionados.append(curso)
        curso.designar_professor(self)

    def listar_cursos(self):
        print(f'Cursos lecionados por {self.nome}:')
        for curso in self.cursos_lecionados:
            print(f'- {curso.nome}')


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

    def designar_professor(self, professor):
        self.professor = professor

professor1 = Professor("Prof. Silva")
professor2 = Professor("Prof. Santos")

curso1 = Curso("Matemática")
curso2 = Curso("História")

professor1.designar_curso(curso1)
professor2.designar_curso(curso2)

curso1.designar_professor(professor2)

professor1.listar_cursos()
professor2.listar_cursos()
