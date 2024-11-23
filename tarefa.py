import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv('ecommerce_estatistica.csv')

def cria_grafico(df):
    # Gráfico 3D
    fig1 = px.scatter_3d(
        df,
        x='Qtd_Vendidos',
        y='N_Avaliações',
        z='Nota',
        color='Preço',
        hover_name='Desconto',
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    fig1.update_layout(
        title='Gráfico 3D: Análise de Vendas',
        scene=dict(
            xaxis_title='Qtd Vendidos',
            yaxis_title='N Avaliações',
            zaxis_title='Nota'
        ),
        paper_bgcolor='rgba(220, 230, 240, 1)',
    )
    return fig1

def cria_app(df):
    # Criar App
    app = dash.Dash(__name__)
    fig1 = cria_grafico(df)

    app.layout = html.Div(
        children=[
            dcc.Graph(
                figure=fig1,
                style={
                    'height': '100%',  # 100% da altura
                    'width': '100%'    # 100% da largura
                }
            )
        ],
        style={
            'width': '100vw',  # 100% da largura da janela
            'height': '100vh',  # 100% da altura da janela
            'margin': '0',  # Remove margens
            'padding': '0',  # Remove espaçamento interno
        }
    )
    return app

if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)