
import unittest
import adicionar
import editar
import remover
import pesquisar
import atendimentos

class TestGestaoAtendimentos(unittest.TestCase):

    def setUp(self):
        # Criar lista inicial de atendimentos vazia
        self.atendimentos = []

    def test_adicionar_atendimento_valido(self):
        atendimento = {"id": 1, "nome": "João", "descricao": "Consulta"}
        adicionar.adicionar_atendimento(self.atendimentos, atendimento)
        self.assertIn(atendimento, self.atendimentos)

    def test_adicionar_atendimento_vazio(self):
        atendimento = {"id": 2, "nome": "", "descricao": ""}
        with self.assertRaises(ValueError):
            adicionar.adicionar_atendimento(self.atendimentos, atendimento)

    def test_pesquisar_atendimento_existente(self):
        atendimento = {"id": 3, "nome": "Maria", "descricao": "Exame"}
        self.atendimentos.append(atendimento)
        resultado = pesquisar.pesquisar_atendimento(self.atendimentos, "Maria")
        self.assertIn(atendimento, resultado)

    def test_pesquisar_atendimento_inexistente(self):
        resultado = pesquisar.pesquisar_atendimento(self.atendimentos, "Carlos")
        self.assertEqual(len(resultado), 0)

    def test_editar_atendimento_existente(self):
        atendimento = {"id": 4, "nome": "Pedro", "descricao": "Raio-X"}
        self.atendimentos.append(atendimento)
        editar.editar_atendimento(self.atendimentos, 4, {"descricao": "Ultrassom"})
        self.assertEqual(self.atendimentos[0]["descricao"], "Ultrassom")

    def test_editar_atendimento_inexistente(self):
        with self.assertRaises(KeyError):
            editar.editar_atendimento(self.atendimentos, 99, {"descricao": "Novo exame"})

    def test_remover_atendimento_existente(self):
        atendimento = {"id": 5, "nome": "Ana", "descricao": "Vacina"}
        self.atendimentos.append(atendimento)
        remover.remover_atendimento(self.atendimentos, 5)
        self.assertNotIn(atendimento, self.atendimentos)

    def test_remover_atendimento_inexistente(self):
        with self.assertRaises(KeyError):
            remover.remover_atendimento(self.atendimentos, 100)

    def test_listar_todos_atendimentos(self):
        atendimentos_iniciais = [
            {"id": 6, "nome": "Clara", "descricao": "Check-up"},
            {"id": 7, "nome": "Lucas", "descricao": "Cirurgia"}
        ]
        self.atendimentos.extend(atendimentos_iniciais)
        resultado = atendimentos.listar_atendimentos(self.atendimentos)
        self.assertEqual(len(resultado), 2)

    def test_fluxo_completo(self):
        # Adicionar
        atendimento = {"id": 8, "nome": "Diego", "descricao": "Dentista"}
        adicionar.adicionar_atendimento(self.atendimentos, atendimento)

        # Editar
        editar.editar_atendimento(self.atendimentos, 8, {"descricao": "Retorno"})
        self.assertEqual(self.atendimentos[0]["descricao"], "Retorno")

        # Remover
        remover.remover_atendimento(self.atendimentos, 8)
        self.assertEqual(len(self.atendimentos), 0)

if __name__ == "__main__":
    unittest.main()
