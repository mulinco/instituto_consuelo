from validador_senha import validador

def test_senha_valida():
    senha_boa = "SenhaForte123@"
    resultado = validador(senha_boa)
    assert resultado == True

def test_senha_muito_curta():
    senha_ruim = "venus2!"
    resultado = validador(senha_ruim)
    assert resultado == False

def test_senha_sem_masc():
    senha_sem_masc = "jupinho0305@"
    resultado = validador(senha_sem_masc)
    assert resultado == False

def test_senha_sem_num():
    senha_sem_num = "Gustavozeronove#"
    resultado = validador(senha_sem_num)
    assert resultado == False

def test_senha_sem_carac_esp():
    senha_sem_carac_esp = "Alana0801"
    resultado = validador(senha_sem_carac_esp)
    assert resultado == False