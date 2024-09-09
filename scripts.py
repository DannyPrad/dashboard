import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Dados simulados para o dashboard
vendas_totais = 50000
pedidos_totais = 850
valor_medio_pedidos = vendas_totais / pedidos_totais
clientes_novos = 300
clientes_recorrentes = 150
produtos_em_baixa = 12
taxa_abandono_carrinho = 0.25  # 25%
lucro_liquido = 15000
gastos_frete = 5000
custo_produtos_vendidos = 20000

# Criando o layout do dashboard com 2 linhas e 3 colunas
fig = make_subplots(
    rows=2, cols=3,
    specs=[[{"type": "indicator"}, {"type": "indicator"}, {"type": "indicator"}],
           [{"type": "bar"}, {"type": "bar"}, {"type": "pie"}]],
    subplot_titles=("Vendas Totais", "Pedidos Totais", "Valor Médio por Pedido",
                    "Clientes Novos vs Recorrentes", "Produtos em Baixa", "Distribuição de Gastos")
)

# Adicionando os indicadores de vendas, pedidos e valor médio
fig.add_trace(go.Indicator(
    mode="number",
    value=vendas_totais,
    title={"text": "Vendas Totais (R$)"}), row=1, col=1)

fig.add_trace(go.Indicator(
    mode="number",
    value=pedidos_totais,
    title={"text": "Pedidos Totais"}), row=1, col=2)

fig.add_trace(go.Indicator(
    mode="number",
    value=valor_medio_pedidos,
    title={"text": "Valor Médio por Pedido (R$)"}), row=1, col=3)

# Adicionando gráfico de barras de clientes
fig.add_trace(go.Bar(
    x=["Clientes Novos", "Clientes Recorrentes"],
    y=[clientes_novos, clientes_recorrentes],
    name="Clientes"), row=2, col=1)

# Adicionando gráfico de barras de produtos em baixa
fig.add_trace(go.Bar(
    x=["Produtos em Baixa"],
    y=[produtos_em_baixa],
    name="Estoque"), row=2, col=2)

# Adicionando gráfico de pizza para distribuição de gastos
fig.add_trace(go.Pie(
    labels=["Lucro Líquido", "Gastos com Frete", "Custo de Produtos Vendidos"],
    values=[lucro_liquido, gastos_frete, custo_produtos_vendidos],
    name="Gastos"), row=2, col=3)

# Layout geral
fig.update_layout(height=600, width=1000, title_text="Dashboard de E-commerce")

# Exibir o dashboard
fig.show()
