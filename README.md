## Nome Dos Integrantes

Gabriel Dias Ramire - 202210108

Guilherme Leme - 202010173

Renan Beinotte - 202210297

## Estrutura do Projeto

```text
securechain/
├── blockchain/
│   ├── blockchain.py
│   └── chain.json
├── auditoria/
│   ├── auditor.py
│   └── relatorios/
├── backup/
│   └── backup.sh
├── logs/
├── documentos/
├── usuarios/
└── README.md
```
## Divisão das atividades

Trabalho feito em uma única maquina, commit colocado a partir dela para não ter problema com carregamentos desnecessário no site. Foi feito uma divisão para os seguintes tópicos

Código Backup seguro com AES-256, Blockchain. Autores: Gabriel Dias Ramire

Código: Auditoria do sistema operacional, Autenticação com bcrypt. Autores: Renan Beinotte

Código: Auditoria do sistema operacional, Monitoramento de integridade. Autores: Guilherme Leme

## Ambiente utilizado

Sistema Operacional: Debian GNU/Linux 13 (trixie)

Python: 3.13.5

Bash: version 5.2.37(1)-release (x86_64-pc-linux-gnu)

Git: 2.47.3

OpenSSL: 3.5.6 7 Apr 2026 (Library: OpenSSL 3.5.6 7 Apr 2026)

Nmap: 7.95

## Controle de usuários Linux

Foram criados os usuários administrador, analista e visitante. Também foram criados grupos específicos: secure_admin, secure_analista e secure_visitante.

O administrador representa o perfil de acesso total, o analista representa o perfil de execução e leitura dos módulos, e o visitante representa o acesso restrito aos relatórios.

Esse controle demonstra o princípio do menor privilégio, separação de funções e controle de acesso com grupos do Linux.

## Zero Trust Security

O sistema aplica o conceito de Zero Trust porque nenhum usuário é considerado confiável por padrão. Cada acesso exige autenticação, cada perfil possui permissões específicas e todas as ações relevantes são registradas na blockchain.

A identidade dos usuários é verificada no login. As permissões são controladas pelos perfis admin, analista e visitante e também pelos grupos do Linux. O princípio do menor privilégio foi aplicado limitando o acesso conforme a função de cada usuário. As ações importantes, como login, alteração de arquivo e backup, são registradas de forma imutável na blockchain.
