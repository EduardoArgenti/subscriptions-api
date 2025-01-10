# Projeto API de Planos de Assinatura - FastAPI

## Como utilizar:

Execute os comandos:

```bash
pip install -r requirements.txt
cd app
uvicorn main:app --reload
```

Na raiz do projeto, adicione um .env no seguinte formato:

```bash
BASIC_AUTH_USERNAME={USUARIO}
BASIC_AUTH_PASSWORD={SENHA}
```
Substitua os valores em chaves pelas credenciais de sua preferência.

Você pode utilizar o próprio Swagger da FastAPI para testar as rotas, acessando /docs. Clique em **Authorize** e logue com as credenciais que informou no .env, ou então utilize o BasicAuth de seu client HTTP (Insomnia, Postman, etc.).

![image](https://github.com/user-attachments/assets/cd4b13bc-59de-466e-8a1c-14960e36ee75)

## Decisões de projeto:

* O projeto não requer explicitamente um banco de dados para persistir as informações, mas o SQLite foi utilizado por ser simples e fácil de configurar, não necessitar de um servidor dedicado, ideal para aplicações pequenas e protótipos, e baixo custo.
* O modelo entidade-relacionamento implementado nos dados de aplicação tem a cardinalidade 1:N nos Planos e Produtos. Isto é, um plano está associado a N produtos, e um produto está associado a somente um plano (pois cada produto deve ser criado com um ID gerado automaticamente).
* Logs são enfileirados e executados em segundo plano para não interferir no tempo de resposta da API.

## Melhorias futuras:

* Alterar banco de dados de SQLite para Postgres para garantir escalabilidade. O uso do SQLAlchemy traz uma abstração que torna esse processo facilitado no código.
* Aprimorar autenticação para JWT com Oauth2 para mais segurança e escalabilidade, e armazenar usuários no banco.
* Os logs foram armazenados junto com os dados de aplicação neste teste para fins de praticidade, mas o ideal é armazenar estes dados em um banco separado, garantindo desempenho, escalabilidade, segurança e conformidade. Como os logs podem ter um aspecto não estruturado, talvez bancos não-relacionais como MongoDB sejam uma boa opção para este projeto.
* Filas em SQS (ou outro gerenciador de queues) ao invés de serem gerenciadas pela própria aplicação. As mensagens seriam processadas por workers dedicados, como funções Lambda da AWS.
* Transformar a cardinalidade em N:M no relacionamento entre Planos e Produtos, pois a aplicação pode conter produtos idênticos em milhares de planos. Exemplo: diversos planos podem ter o produto **Internet Fibra**, e o mesmo pode ter seu preço atualizado após um tempo.
