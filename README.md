# <img src="../Ai_Trace/assents/logo.svg" alt="Logo" width="25"/> Ai Trace


Este repositório corresponde ao desenvolvimento do **Ai Trace**, uma ferramenta web capaz de identificar a procedência de imagens, classificando-as como criadas por seres humanos ou geradas por inteligência artificial. 

O sistema permite que usuários façam upload de imagens para análise. Caso a imagem seja detectada como gerada por IA, o sistema também tenta identificar qual modelo de IA foi responsável pela sua geração.

O objetivo principal do projeto é fornecer uma solução acessível para detecção de conteúdo sintético, contribuindo para a compreensão dos limites atuais da inteligência artificial na geração de imagens e seus impactos no cenário digital.

Este repositório contém exclusivamente o código da aplicação web que executa essa análise. 

## 🧠 Sobre o projeto

**Ai Trace** é um projeto acadêmico dividido em fases, que combina tecnologia, design e análise de comportamento humano para entender a capacidade humana de distinguir imagens criadas por IA.

Esta é a **fase 1** do projeto, com foco em:

- Desenvolver a base do site institucional e da votação
- Estruturar o dataset que será usado na etapa seguinte
- Coletar respostas reais para treinar e validar futuros modelos

> A etapa de **identificação automática das imagens por IA** será desenvolvida posteriormente com o uso de redes neurais treinadas.

## 🚀 Tecnologias utilizadas

- **Django** (estrutura do site)
- **HTML + CSS** (frontend)
- (Futuramente) Estilização com **TailwindCSS** ou **Bootstrap**

## 📁 Estrutura do Repositório

```bash
ai_trace/
│
├── site_oficial/         # App Django do site institucional
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── ai_trace/             # Configuração principal do Django
│
├── manage.py
└── README.md
