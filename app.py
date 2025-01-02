import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
app = Dash(__name__)
df = pd.read_csv("merged_economic_indicators_2000_2024.csv")
#creating dropdown options to select economic indicators
dropdown_options = [
    {'label': 'GDP (Current US$))', 'value': 'GDP (Current US$)'},
    {'label': 'Inflation Rate', 'value': 'Inflation Rate'},
    {'label': 'Unemployment Rate', 'value': 'Unemployment Rate'}
]
country_dropdown_options = [{'label': country, 'value': country} for country in df['Country Name'].unique()]

#dashboard layout
app.layout = html.Div([
    html.H1("Economic Indicator Dashboard"),
    html.Div([
        html.Label("Select Indicator:"),
        dcc.Dropdown(
            id='indicator-dropdown',
            options=dropdown_options,
            value="GDP (Current US$)"
        )
    ]),
    html.Div([
        html.Label("Select Country"),
        dcc.Dropdown(
            id="country-dropdown",
            options=country_dropdown_options,
            value= df['Country Name'].unique()[0]
        )
    ]),
    dcc.Graph("indicator-graph"),
])
#callback to update app
@app.callback(
    Output("indicator-graph", "figure"),
    [Input("indicator-dropdown","value"),
     Input("country-dropdown","value")]
)
def update_graph(selected_indicator, selected_country):
    #filter data for selected country
    filtered_df = df[df['Country Name']==selected_country]

    #create graph
    fig = px.line(
        filtered_df,
        x="Year",
        y=selected_indicator,
        title=f"{selected_indicator} in {selected_country} (2000-2024)",

    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)



