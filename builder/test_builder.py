from pytest import fixture, mark

from builder import ConcreteUserBuilder, UserDirector


@fixture
def builder():
    return ConcreteUserBuilder()


@fixture
def director(builder):
    return UserDirector(builder)


@mark.parametrize(
    'name',
    ['Teste1', 'Teste2', 'Teste3', 'Teste4']
)
def test_criar_usuario_apenas_com_primeiro_nome(builder, name):
    builder.add_first_name(name)
    user = builder.result
    assert user.first_name == name


@mark.parametrize(
    'primeiro_nome, ultimo_nome',
    [('Albert', 'Einstein'), ('Marie', 'Curie'), ('Stephen', 'Hawking'), ('Carl', 'Sagan')]
)
def test_criar_usuario_com_primeiro_e_segundo_nome(builder, primeiro_nome, ultimo_nome):
    builder.add_first_name(primeiro_nome)
    builder.add_last_name(ultimo_nome)
    user = builder.result
    assert (user.first_name, user.last_name) == (primeiro_nome, ultimo_nome)


@mark.parametrize(
    'idade',
    [20, 30, 40, 50]
)
def test_criar_usuario_com_idade(builder, idade):
    builder.add_age(idade)
    user = builder.result
    assert user.age == idade


def test_criar_usuario_com_idade_primeiro_e_ultimo_nome(director):
    user = director.with_age(first_name='Teste', last_name='Teste2', age=25)
    assert (user.first_name, user.last_name, user.age) == ('Teste', 'Teste2', 25)


def test_criar_usuario_com_idade_primeiro_e_ultimo_nome_e_endereco(director):
    user = director.with_age_and_address(first_name='Teste', last_name='Teste2', age=25, address='Rua de Teste')
    assert (user.first_name, user.last_name, user.age, user.addresses[0]) == ('Teste', 'Teste2', 25, 'Rua de Teste')

