# 🐟 Aplicação de Gestão de Embarcações de Pesca

Este projeto tem como objetivo desenvolver uma aplicação completa para auxiliar proprietários de embarcações de pesca na gestão diária e legal da sua atividade.

O sistema é composto por:
- **Backend em FastAPI**
- **Frontend em Flutter**  
Com foco em simplicidade, eficiência e apoio à conformidade legal.

---

## 🎯 Objetivos Principais

- Registar e gerir dados das embarcações (e.g., matrícula, lotação, arqueação).
- Carregar e organizar documentos legais e fiscais, como licenças e certificados obrigatórios.
- Enviar alertas automáticos para renovações de documentos e prazos importantes.
- Guardar ficheiros de forma local e segura, registando os metadados na base de dados.
- Notificar o utilizador diretamente no telemóvel ou computador.
- Suportar funcionalidades offline, como lembretes locais.

---

## 🛠️ Tecnologias Utilizadas

| Componente  | Tecnologia      |
|-------------|-----------------|
| **Backend** | FastAPI + PostgreSQL |
| **Frontend** | Flutter (Android, iOS, Web e Windows) |
| **Notificações** | Firebase Cloud Messaging (ou alternativa offline no dispositivo) |
| **Autenticação** | JWT (planeado) |

---

## 📌 Funcionalidades Incluídas

- Cadastro de embarcações  
- Upload de documentos fiscais e legais  
- Alertas automáticos de renovação  
- API REST documentada com Swagger  
- Suporte multi-plataforma (Android/Windows/Web)

---

## 🚧 Estado do Projeto

- [x] Backend inicializado com FastAPI  
- [x] Base de dados Postgres configurada  
- [x] Upload e gestão de documentos legais  
- [ ] Sistema de alertas para renovação de documentos  
- [ ] Notificações mobile e desktop  
- [ ] Autenticação de utilizadores  
- [ ] Interface em Flutter  

---

## 📝 Como Executar o Backend

```sh
cd app_backend
uvicorn app.main:app --reload
