# 🌐 Ai Trace – Site Oficial

Este repositório contém o código do **site oficial do projeto Ai Trace**, um Trabalho de Conclusão de Curso (TCC) que investiga o cenário atual da geração de imagens por Inteligência Artificial (IA) e como as pessoas percebem essas imagens.

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
