# Sistema de Login Personalizado - CRUD UAI

Este repositório faz parte do projeto **CRUD UAI**, desenvolvido para atender às necessidades de um importante veículo de comunicação de Minas Gerais. A aplicação inclui um **sistema de login personalizado**, projetado com características específicas solicitadas pelo contratante, proporcionando maior segurança, flexibilidade e adequação ao contexto do cliente.

## **Sobre o Projeto**

O sistema de login foi projetado para:

- Atender às especificidades do contratante, garantindo uma solução sob medida.
- Oferecer maior controle sobre autenticação e autorização de usuários.
- Facilitar a integração com o restante do sistema **CRUD UAI**, mantendo a coerência com os fluxos de trabalho do cliente.

### Principais características:

- **Personalização**: Interface e lógica de login desenvolvidas para refletir a identidade do contratante.
- **Segurança**: Implementação de práticas recomendadas para proteção de credenciais e autenticação.
- **Flexibilidade**: Suporte a diferentes níveis de acesso com base em permissões específicas.

## **Tecnologias Utilizadas**

- **Django** 4.x: Framework utilizado para backend e gerenciamento de usuários.
- **Bootstrap**: Para criar uma interface limpa e responsiva.
- **SQLite**: Banco de dados padrão para armazenar usuários e suas permissões durante o desenvolvimento.

## **Configuração e Uso**

### 1. Clone o repositório:

```bash
git clone https://github.com/carlosalbertoprojetos/crud_uai.git
cd crud_uai/usuario
```

### 2. Configure o ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Realize as migrações e crie um superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Inicie o servidor:

```bash
python manage.py runserver
```

### 5. Acesse no navegador:

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e explore o sistema de login personalizado.

## **Diferenciais do Sistema de Login**

- **Design Responsivo**: Interface adaptada para dispositivos móveis e desktops.
- **Múltiplos Níveis de Acesso**: Configuração granular de permissões por tipo de usuário.
- **Fluxo Personalizado**: Autenticação e registro ajustados para as necessidades específicas do contratante.

## **Futuras Implementações**

- Integração com autenticação de dois fatores (2FA).
- Logs de atividade detalhados para maior rastreabilidade.
- Suporte a Single Sign-On (SSO) em sistemas externos.

## **Licença**

Este projeto está licenciado sob a [Licença MIT](LICENSE). O código pode ser utilizado e adaptado para projetos similares, respeitando os termos da licença.

---

Desenvolvido por [Carlos Alberto Medeiros](https://www.linkedin.com/in/carlos-alberto-medeiros-29aa6258/)  
Adaptando soluções tecnológicas às demandas únicas de cada cliente!
