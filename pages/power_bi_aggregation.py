import dash
from dash import html, dcc
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px
import base64
import io


app = dash.Dash()
server=app.server

# create app layout
app.title="Query Builder"
app.layout = html.Div([
    # create initial data inputs for query. Allow user to input previous table name, grouping var, and whether to keep first/last entries
    # all the above are needed in the final query
    html.Div([
        html.H1("Power BI Data Aggregation Query Builder"),
        html.H3("Enter Previous Table Name:"),
        dcc.Input(id='previous_table_name', value="Pivoted Table"),
        html.H3("Enter Variable To Group By:"),
        dcc.Input(id='group_by_variable', value="ProjectID"),
        html.H3("Enter whether to keep First or Last value inputs:"),
        dcc.Dropdown([{'label':'First','value':'First'},{'label':'Last','value':'Last'}],value="Last",id="first_last",style={'width':'177px'}),
        html.H3("Enter whether to add an Index to re-named field:"),
        dcc.Dropdown([{'label':'Yes','value':'Yes'},{'label':'No','value':'No'}],value='Yes',id="name_index",style={'width':'177px'})]),
    # section to upload an excel or csv file with column names to include in the query
    html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    #section within the div that will return the final query output
    html.H2("Final Query Result:"),
    html.Div(id='output-data-upload'),
    ])
])

# function, from plotly docs, that will read in data
# added in sections after the exception block where the query itself is built out
# used within the update_output function below
def parse_contents(contents, prev_table,group_by_table,first_last,name_index,filename):
    content_type, content_string = contents.split(',')
    print(prev_table,group_by_table,first_last)
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    # builds first section of query from user input of previous table name, grouping, first/last preference
    first_part_of_query = '=Table.Group(#\"'+prev_table+'", {"'+group_by_table+'"},{'
    # initiates empty string for the second part of query
    column_list_string_query = ''
    # make a df in dict format to access data, and find the relevant col name to search through
    df2=df.to_dict()
    column_name = list(df2.keys())[0]
    #for loop to go through each row of the data, transform it to be in the right format for the query, and append to the query string
    for row in range(len(df)):
        if row>=0:
            if name_index=='Yes':

                datum = df2[column_name][row]
                column_list_string_query+='{"'+str(row+1)+'_'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'
            else:
                datum = df2[column_name][row]
                column_list_string_query+='{"'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'
    # combining all portions of the query
    column_list_string_query=first_part_of_query+column_list_string_query[:-1]+'})'

    # returns the query result generated above
    return html.Div([
        html.P(column_list_string_query),
        html.Hr()
    ])

# callback to call in the user inputs and data upload
# function update_output takes in the inputs/uploads, runs parse_contents function and returns its output
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              [Input('previous_table_name', 'value')],
              [Input('group_by_variable', 'value')],
              [Input('first_last', 'value')],
              [Input('name_index', 'value')],
              State('upload-data', 'filename'),
              )
def update_output(list_of_contents, prev_table,group_by_table,first_last,name_index,list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c,prev_table,group_by_table,first_last,name_index, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children

if __name__=="__main__":
    app.run_server()