from dash import Dash,  html, dcc, Output,Input
import pandas as pd
import plotly.express as px

#Estrutura 

#Layout -Tudo que vai ser visualizado 

#Callback - Funcionalidades que voce tera do dash

app = Dash(__name__)

df  = pd.read_excel("vendas_consoles_atualizada.xlsx")
# Esta linha le o arquivo do Excel e armazena os dados em uma variavel chamada df

fig = px.bar_polar(df,x="Console", y="Vendas (milhões)", color = "Empresa", barmode="group")

opcoes = list(df['Empresa'].unique())
#Essa linha adiciona a struing todas as lojas ao final da lista de opcoes 
opcoes.append("Todas as Empresas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Empresas'),
    html.H2(children='Gráfico com o faturamento de todos os consoles separados por empresas'),
    dcc.Dropdown(opcoes, value= 'Todas as Empresas', id='lista_empresa'),

    dcc.Graph(
        id='grafico_quantidade_produto',
        figure=fig
    )



])

@app.callback(
    Output('grafico_quantidade_produto','figure'),
    Input('lista_empresa','value')
)

def update_output(value):
    if value == 'Todas as Empresas':
        fig = px.bar(df, x="Console",y="Vendas (milhões)", color ="Empresa", barmode="group")
    else:
        tabela_filtrada =df.loc[df['Empresa'] == value, :]
        fig = px.bar(tabela_filtrada, x="Console",y="Vendas (milhões)", color ="Ano de Lançamento", barmode="group")
    return fig 


if __name__ == '__main__':
    app.run(debug=True)
