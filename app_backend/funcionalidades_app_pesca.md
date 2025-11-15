# Funcionalidades e User Stories da Aplicação de Pesca com Barco

## Backend
### 1. Gestão de Embarcação e Documentos Legais
- **US04:** Registar dados da embarcação (matrícula, lotação, arqueação).
- **US05:** Carregar documentos fiscais anuais e licenças da embarcação.  
     - criar filtros para os documentos(entidade responsavel,ano que termina)
- **US06:** Alertas automáticos de renovação de licenças.


### 2. Diário de Bordo / Registo de Capturas
- **US07:** Registar cada captura com espécie, peso, coordenadas GPS e método de captura.
- **US08:** Visualizar histórico de todas as capturas.
- **US09:** Gerar relatório em PDF das capturas.

### 3. Dados Ambientais em Tempo Real
- **US10:** Consultar marés, direção do vento e temperatura da água em tempo real.
- **US11:** Alertas de condições meteorológicas adversas.

### 4. Área Fiscal e Relatórios
- **US16:** Emitir relatórios fiscais de atividade da embarcação.
- **US17:** Exportar documentos em PDF.

### 5. Integração com Equipamentos Náuticos
- **US14:** Conectar a *fish-finder* via Bluetooth ou Wi-Fi.
- **US15:** Importar dados sonar.

### 6. Mapas e Rotas de Pesca
- **US12:** Visualizar no mapa os "spots" de pesca mais populares.
- **US13:** Gravar rotas e exportar ficheiros GPX.

### 7. Funcionalidades Offline
- **US18:** Registar capturas mesmo sem acesso à internet.
- **US19:** Sincronizar dados automaticamente quando a ligação for restabelecida.

### 8. Perfil e Estatísticas
- **US20:** Visualizar estatísticas de desempenho (capturas por espécie, local, mês).
- **US21:** Competir em rankings com outros pescadores.

### 9. Notificações e Alertas Inteligentes
- **US22:** Receber alertas de renovação de documentos legais.
- **US23:** Receber recomendações de pesca com base nas marés e fases da lua.

### 10. Registo e Autenticação (última fase)
- **US01:** Criar conta com email, número de licença marítima e NIF.
- **US02:** Autenticação com *login* e *token* JWT.
- **US03:** Recuperar palavra-passe por email.

## Frontend
> Todas as funcionalidades consumirão as APIs do backend e se focam em interface de utilizador:
- Formulários de registo e login.
- Upload de documentos e licenças.
- Visualização de capturas, mapas, rotas e estatísticas.
- Alertas visuais de notificações e condições meteorológicas.
- Exportação de PDFs e ficheiros GPX.
- Integração com dispositivos náuticos via interface gráfica.