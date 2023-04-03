# Visualization packages
import altair as alt
import plotly.graph_objects as go

# Dashboard packages
import dash
from dash import dcc
import dash_core_components as dcc
from dash import html
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Import functions from data_wrangling script
from data_wrangling import (
    get_year_stats,
    get_month_stats,
    get_year_data,
    get_month_data,
    left_hist_data,
    right_hist_data,
    get_guest_map_prices_busy_months,
    sherif_func
)
guest_map,prices,busy_months,total_bookings,cancelled_bookings,max_bookings_month,fig=get_guest_map_prices_busy_months()
length_of_stay,cancel_sizes,booking_Segment,booking_canceled=sherif_func()


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP], title="Super Hotel Management",suppress_callback_exceptions=True
)
server = app.server  # to deploy the app


# Global variables
columns = [
    "Reservations",
    "Average daily rate",
    "Adults",
    "Children",
    "Babies",
    "Required parking spaces",
    "Booking changes",
    "Special requests",
]
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
months_short = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
years = [2015, 2016, 2017]

collapse = html.Div(
    [
        dbc.Button(
            "Learn more",
            id="collapse-button",
            className="mb-3",
            outline=False,
            style={
                "margin-top": "10px",
                "width": "150px",
                "background-color": "white",
                "color": "black",
                "fontWeight": "bold",
                # "border": "0.5px solid #FFA500",
            },
        ),
    ]
)

instruction = html.Div(
    [
        dbc.Button(
            "Help",
            id="instruction-button",
            className="mb-3",
            outline=False,
            style={
                "margin-top": "10px",
                "width": "120px",
                "height": "35px",
                "background-color": "white",
                "color": "black",
                # "fontWeight": "bold",
                # "border": "0.5px solid #FFA500",
            },
        ),
    ]
)

card_top = dbc.Card(
    [
        dbc.CardHeader(
            [
                dbc.Row(
                    [
                        dbc.Col(md=1),
                        dbc.Col(
                            [
                                html.H5(
                                    "Select feature to plot:",
                                    style={
                                        "margin-top": "15px",
                                        # "color": "#023047",
                                    },
                                ),
                            ],
                            md=4,
                        ),
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    id="y-axis-dropdown",
                                    options=[
                                        {
                                            "label": column,
                                            "value": column,
                                        }
                                        for column in columns
                                    ],
                                    value=columns[0],
                                    multi=False,
                                    searchable=False,
                                    clearable=False,
                                    style={"margin-top": "10px"},
                                ),
                            ],
                            md=3,
                        ),
                        dbc.Col(),
                        dbc.Col(
                            [
                                instruction,
                                dbc.Collapse(
                                    html.P(
                                        "Starting using by selecting feature on the left, and interacting with plots by selecting legends and scrolling to zoom",
                                        className="lead",
                                    ),
                                    id="instruction",
                                ),
                            ],
                            md=3,
                        ),
                    ]
                )
            ],
            style={
                "background-color": "white",
            },
        ),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Iframe(
                                    id="year-plot",
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "375px",
                                    },
                                ),
                                html.P(
                                    id="year_stats_card",
                                    children="",
                                    style={
                                        "text-align": "center",
                                        "fontWeight": "bold",
                                        "color": "#537aaa",

                                    },
                                ),
                                html.P(
                                    id="year_stats_card2",
                                    children="",
                                    style={
                                        "text-align": "center",
                                         "fontWeight": "bold",
                                       "color": "#f9a200",
                                    },
                                ),
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Iframe(
                                    id="month-plot",
                                    style={
                                        "border-width": "0",
                                        "width": "100%",
                                        "height": "375px",
                                    },
                                ),
                                html.P(
                                    id="month_stats_card",
                                    children="",
                                    style={
                                        "text-align": "center",
                                         "fontWeight": "bold",
                                        "color": "#537aaa",
                                    },
                                ),
                                html.P(
                                    id="month_stats_card2",
                                    children="",
                                    style={
                                        "text-align": "center",
                                         "fontWeight": "bold",
                                        "color": "#f9a200",
                                    },
                                ),
                            ]
                        ),
                    ],
                ),
            ],
        ),
    ],
    className="w-100 mb-3",
    style={
        "border": "1px solid #d3d3d3",
        "margin-left": "0px",
        "margin-right": "0px",
    },
)

card_left = dbc.Card(
    [
        dbc.CardBody(
            html.Iframe(
                id="hist1",
                style={
                    "border-width": "0",
                    "width": "120%",
                    "height": "300px",
                },
            ),
        ),
    ],
    className="w-100 mb-3",
    style={"border": "1.5px solid #d3d3d3"},
)

card_right = dbc.Card(
    [
        dbc.CardBody(
            html.Iframe(
                id="hist2",
                style={
                    "border-width": "0",
                    "width": "100%",
                    "height": "300px",
                },
            ),
        ),
    ],
    className="w-100 mb-3",
    style={"border": "1.5px solid #d3d3d3"},
)

jumbotron = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H1(
                                    "Super Hotel Management",
                                    className="display-4",
                                    style={
                                        "text-align": "left",
                                        "font-size": "45px",
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                ),
                                dbc.Collapse(
                                    html.P(
                                        "This is an interactive dashboard based on the data from the Hotel Booking Demand dataset. Start using the dashboard by selecting specific year, month and hotel type",
                                        className="lead",
                                        style={"width": "65%"},
                                    ),
                                    id="collapse",
                                ),
                            ],
                            md=10,
                        ),
                        dbc.Col([collapse]),
                    ]
                )
            ],
            fluid=True,
                style={
                    "padding": 0,
                    "height": "150px"
                },
        )

info_area = dbc.Container(
    [
        dbc.Row(
            [
                # First column with control widgets
                dbc.Col(
                    [
                        html.H4(
                            "Global controls",
                            # style={"color": "#023047"}
                        ),
                        html.Br(),
                        html.H5("Select year",
                                #style={"color": "#023047"}
                                ),
                        dcc.Dropdown(
                            id="year-dropdown",
                            options=[{"label": year, "value": year} for year in years],
                            value=2015,
                            multi=False,
                            searchable=False,
                            clearable=False,
                        ),
                        html.Br(),
                        html.H5(
                            "Select month",
                            # style={"color": "#023047"}
                        ),
                        dcc.Dropdown(
                            id="month-dropdown",
                            value=7,
                            multi=False,
                            searchable=False,
                            clearable=False,
                        ),
                        html.Br(),
                        html.H5(
                            "Select Hotel Type",
                            # style={"color": "#023047"}
                        ),
                        dcc.RadioItems(
                            id="hotel-type-selection",
                            options=[
                                {"label": " All Hotels", "value": "All"},
                                {"label": " Resort Hotel", "value": "Resort"},
                                {"label": " City Hotel", "value": "City"},
                            ],
                            value="All",
                            labelStyle={"display": "block"},
                        ),
                    ],
                    md=2,
                    style={
                        "background-color": "white",
                        "padding": 10,
                        "border-radius": 5,
                        "margin-right": "10px",
                        "border": "1.5px solid #d3d3d3",
                    },
                ),
                # 2nd column with plots
                dbc.Col(
                    [
                        dbc.Row([card_top]),
                        dbc.Row(
                            [
                                dbc.Col([card_left]),
                                dbc.Col([card_right]),
                            ],
                        ),
                    ],
                    style={"margin-left": "5px", "margin-right": "5px"},
                ),
            ],
        ),
    ],
)

footer = dcc.Markdown(
    """This dashboard is made by NC Team (Sherif, Ola and Nouran) [Link to GitHub source](https://github.com/sherif17/Hotel-Dasboard). The data has been sourced from [Link to data source](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand).""",
    style={"text-align": "center"},
)

##************************************************************************************************************************

bins=html.Div([
    #html.H1('Hotel Booking Demand Dashboard'),
    dbc.Row([
        dbc.Col([dbc.Card([dcc.Graph(
                id='total-bookings',
                figure={
                    'data': [
                        go.Indicator(
                            mode='number',
                            value=total_bookings,
                            title='Total Bookings',
                        )
                    ],
                    'layout': go.Layout(
                        height=200,
                        width=350,
                        margin=dict(t=1, b=1),
                    )
                }
            )])]),
        dbc.Col([dbc.Card([dcc.Graph(
                id='cancelled-bookings',
                figure={
                    'data': [
                        go.Indicator(
                            mode='number',
                            value=cancelled_bookings,
                            title='Cancelled Bookings',
                        )
                    ],
                    'layout': go.Layout(
                        height=200,
                        width=350,
                        margin=dict(t=1, b=1),
                    )
                }
            )])]),
        dbc.Col([dbc.Card([dcc.Graph(
                id='busiest-month',
                figure={
                    'data': [
                        go.Indicator(
                            mode='number',
                            value=max_bookings_month,
                            title='Busiest Month',
                        )
                    ],
                    'layout': go.Layout(
                        height=200,
                        width=350,
                        margin=dict(t=1, b=1),
                    )
                }
            )])])
    ])
])


card_top2 = dbc.Card(
    [
        dbc.Row(
            [
                dcc.Graph(figure=guest_map),
               # dcc.Graph(figure=prices),
                dcc.Graph(figure=busy_months)

            ],
        )
    ],
    className="w-100 mb-3",
    style={
        "border": "1.5px solid #d3d3d3",
        "margin-left": "15px",
        "margin-right": "15px",
    },
)

card_left2 = dbc.Card(
    [
        dbc.CardBody(
            html.Iframe(
                id="hist1",
                style={
                    "border-width": "0",
                    "width": "120%",
                    "height": "300px",
                },
            ),
        ),
    ],
    className="w-100 mb-3",
    style={"border": "1.5px solid #d3d3d3"},
)

card_right2 = dbc.Card(
    [
        dbc.CardBody(
            html.Iframe(
                id="hist2",
                style={
                    "border-width": "0",
                    "width": "100%",
                    "height": "300px",
                },
            ),
        ),
    ],
    className="w-100 mb-3",
    style={"border": "1.5px solid #d3d3d3"},
)


info_area2 = dbc.Container(
    [
        dbc.Row([
        dbc.Card([bins],
            className="w-100 mb-3",
            style={
                "border": "1.5px solid #d3d3d3",
                "margin-left": "15px",
                "margin-right": "15px",
            },
        )
    ]),

    dbc.Row([
        dbc.Card([
        html.H1(children='Home country of guests', style={'textAlign': 'center'}),
        dcc.Graph(figure=guest_map)],
            className="w-100 mb-3",
            style={
                "border": "1.5px solid #d3d3d3",
                "margin-left": "15px",
                "margin-right": "15px",
            },
        )
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
            html.H1(children='Bookings per market segment', style={'textAlign': 'center'}),
            dcc.Graph(figure=booking_Segment)],
                  className="w-100 mb-3",
                 style={
                    "border-width": "0",
                    "width": "400px",
                    "height": "300px",
                 },
            )
        ]),
        dbc.Col([
            dbc.Row([
            dbc.Card([
            html.H1(children='Cancellation sizes', style={'textAlign': 'center'}),
            dcc.Graph(figure=cancel_sizes)],
                 className="w-100 mb-3",
                style={
                    "border-width": "0",
                    "width": "600px",
                    "height": "300px",
                },
        )
    ])
        ])

    ])

])
##************************************************************************************************************************

card_top3 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Card([  html.H1(children='Cancelations per month', style={'textAlign': 'center'}),dcc.Graph(figure=booking_canceled)])
            ],
        )
    ],
    className="w-100 mb-3",
    style={
        "border": "1.5px solid #d3d3d3",
        "margin-left": "15px",
        "margin-right": "15px",
    },
)
card_top31 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Card([  html.H1(children='Average number of guests per month', style={'textAlign': 'center'}),
                            dcc.Graph(figure=busy_months)])
            ],
        )
    ],
    className="w-100 mb-3",
    style={
        "border": "1.5px solid #d3d3d3",
        "margin-left": "15px",
        "margin-right": "15px",
    },
)
card_left3 = dbc.Card(
    [
        dbc.Row(
            [
        # html.H1(children='Length of stay for guests', style={'textAlign': 'center'}),
                dbc.Card([dcc.Graph(figure=length_of_stay)])
            ],
        )
    ],
    className="w-100 mb-3",
    style={"border": "1.5px solid #d3d3d3",
           "width": "130px"},
)

card_right3 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Card([dcc.Graph(figure=fig)])
            ],
        )
    ],
    className="w-100 mb-3",
    style={"border": "1.5px solid #d3d3d3",
           "width": "130px"},
)


info_area3 = dbc.Container(
    [
        dbc.Col(
                    [
                        dbc.Row([card_top31]),
                        dbc.Row([card_top3]),
                        dbc.Row(
                            [
                                dbc.Col([card_left3],
                                        style={"width":"130px"}),
                                dbc.Col([card_right3],
                                        style={"width":"130px"}),
                            ],
                        ),
                    ],
                    style={"margin-left": "5px", "margin-right": "5px"},
                )

    ]
)

##************************************************************************************************************************

#app.layout = html.Div([jumbotron, info_area, html.Hr(), footer])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "14rem",
    "margin-right": "1rem",
    "padding": "1rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("🏨", className="display-1",style={'textAlign': 'center'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Overview" + " 📘", href="/", active="exact", style={'height': "5vw"}),
                dbc.NavLink("Data Matrix" + " 📈", href="/Maps", active="exact", style={'height': "5vw"}),
                dbc.NavLink("Visualization" + " 📊", href="/Visualization", active="exact", style={'height': "5vw"}),


            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
              html.Div([jumbotron, info_area2, html.Hr(), footer])
        ]
    elif pathname == "/Maps":
        return [
            html.Div([jumbotron, info_area, html.Hr(), footer])

        ]
    elif pathname == "/Visualization":
        return [
            html.Div([jumbotron, info_area3, html.Hr(), footer])
        ]
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),

        ]
    )

click = alt.selection_multi(fields=["Line"], bind="legend")

# Callbacks and back-end


@app.callback(Output("month-dropdown", "options"), [Input("year-dropdown", "value")])
def update_date_dropdown(year):
    """removes the months from the month-dropdown for which no data is  available
    ----------
     year:        the year selected from "year-dropdown"
    Returns
    -------
    updated month-dropdown options
    """
    if year == 2015:
        return [{"label": months[i], "value": i + 1} for i in range(6, 12)]
    if year == 2017:
        return [{"label": months[i], "value": i + 1} for i in range(8)]
    return [{"label": months[i], "value": i + 1} for i in range(12)]


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    """toggle the collapse button to display app information
    ------
    n: check if there is input on the button
    Returns
    -------
    expand the information area
    """
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("instruction", "is_open"),
    [Input("instruction-button", "n_clicks")],
    [State("instruction", "is_open")],
)
def toggle_collapse(n, is_open):
    """toggle the collapse button to display app instructions
    ------
    n: check if there is input on the button
    Returns
    -------
    expand the instruction area
    """
    if n:
        return not is_open
    return is_open


################################### Top plots ################################
@app.callback(
    Output("year-plot", "srcDoc"),
    Output("year_stats_card", "children"),
    Output("year_stats_card2", "children"),
    Input("hotel-type-selection", "value"),
    Input("y-axis-dropdown", "value"),
    Input("year-dropdown", "value"),
)
def plot_year(hotel_type="All", y_col="Reservations", year=2016):
    """Updates the `year-plot` information in `year_stats_card` and `year_stats_card2`
    Parameters
    ----------
    hotel_type : dataframe produced by `get_year_data()`
    y_col:       the variable to be plotted, selectedfrom  "y-axis-dropdown"
    year:        the year selected from "year-dropdown"
    Returns
    -------
    plot for `year-plot`, 2 strings for `year_stats_card` and `year_stats_card2`
    """
    df = get_year_data(hotel_type, y_col, year)
    stats_current = get_year_stats(df, "current", y_col, year)
    stats_all = get_year_stats(df, "all_time", y_col, year)
    df = get_year_data(hotel_type, y_col, year)
    df["Arrival month"] = df["Arrival month"].replace(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], months_short
    )
    lines = (
        alt.Chart(df, title=y_col + " for " + str(year))
        .mark_line()
        .encode(
            alt.X(
                "Arrival month",
                sort=months_short,
                title="Month",
                axis=alt.Axis(grid=False, labelAngle=-30),
            ),
            alt.Y(y_col, title=y_col, scale=alt.Scale(zero=True)),
            alt.Color("Line"),
            alt.Tooltip(y_col),
            opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
        )
    )
    chart = (
        (lines + lines.mark_circle())
        .properties(width=295, height=250)
        .configure_axis(labelFontSize=13, titleFontSize=17, grid=False)
        .configure_title(fontSize=23)
        .configure_legend(
            strokeColor="gray",
            fillColor="#e9ecef",
            padding=10,
            cornerRadius=10,
            orient="bottom-right",
        )
        .interactive()
        .add_selection(click)
    )
    return chart.to_html(), stats_current, stats_all


@app.callback(
    Output("month-plot", "srcDoc"),
    Output("month_stats_card", "children"),
    Output("month_stats_card2", "children"),
    Input("hotel-type-selection", "value"),
    Input("y-axis-dropdown", "value"),
    Input("year-dropdown", "value"),
    Input("month-dropdown", "value"),
)
def plot_month(hotel_type="All", y_col="Reservations", year=2016, month=1):
    """Updates the `month-plot` information in `month_stats_card` and `month_stats_card2`
    Parameters
    ----------
    hotel_type : dataframe produced by `get_month_data()`
    y_col:       the variable to be plotted, selected from "y-axis-dropdown"
    month:        the month selected from "month-dropdown"
    Returns
    -------
    plot for `year-plot`, 2 strings for `year_stats_card` and `year_stats_card2`
    """
    df = get_month_data(hotel_type, y_col, year, month)

    stats_current = get_month_stats(df, "current", y_col, year, month)
    stats_all = get_month_stats(df, "all_time", y_col, year, month)

    lines = (
        alt.Chart(df, title=y_col + " for " + months_short[month - 1] + " " + str(year))
        .mark_line()
        .encode(
            alt.X("Arrival day", title="Date", axis=alt.Axis(grid=False)),
            alt.Y(y_col, title=y_col, scale=alt.Scale(zero=True)),
            alt.Color("Line"),
            alt.Tooltip([y_col, "Arrival day of week"]),
            opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
        )
    )
    chart = (
        (lines + lines.mark_circle())
        .properties(width=300, height=250)
        .configure_axis(labelFontSize=13, titleFontSize=17, grid=False)
        .configure_title(fontSize=23)
        .configure_legend(
            strokeColor="gray",
            fillColor="#e9ecef",
            padding=10,
            cornerRadius=10,
            orient="bottom-right",
        )
        .interactive()
        .add_selection(click)
    )
    return chart.to_html(), stats_current, stats_all


################################### Histograms ################################
@app.callback(
    Output("hist1", "srcDoc"),
    Input("hotel-type-selection", "value"),
    Input("year-dropdown", "value"),
    Input("month-dropdown", "value"),
)
# Function to plot the bottom left histogram using selected hotel type and dates
def histogram_1(hotel_type, year, month):
    """Updates the `hist1` histogram on the bottom left of the app, showing the
    country of origin of guests
    Parameters
    ----------
    hotel_type : dataframe produced by `get_month_data()`
    year:        the year selected from "year-dropdown"
    month:        the month selected from "month-dropdown"
    Returns
    -------
    plot for `hist1`
    """
    df = left_hist_data(hotel_type, year, month)
    top_countries = (
        alt.Chart(
            df,
            title="Countries of origin "
            + str(months_short[month - 1])
            + " "
            + str(year),
        )
        .mark_bar( size=15)
        .encode(
            alt.Y("Country of origin", sort="-x", title="Country"),
            alt.X("counts", title="Reservations"),
            alt.Tooltip("Country of origin"),
        )
        .properties(width=300, height=200)
        .configure_axis(labelFontSize=10, titleFontSize=15, grid=False)
        .configure_title(fontSize=19)
    )
    return top_countries.to_html()


@app.callback(
    Output("hist2", "srcDoc"),
    Input("hotel-type-selection", "value"),
    Input("year-dropdown", "value"),
    Input("month-dropdown", "value"),
)

# Function to plot the bottom right plot using selected hotel type
def histogram_2(hotel_type, year, month):
    """Updates the `hist2` histogram on the bottom left of the app, showing the
    duration of guest stay
    Parameters
    ----------
    hotel_type : dataframe produced by `get_month_data()`
    year:        the year selected from "year-dropdown"
    month:        the month selected from "month-dropdown"
    Returns
    -------
    plot for `hist2`
    """
    df = right_hist_data(hotel_type, year, month)
    stay = (
        alt.Chart(
            df,
            title="Lengths of Stay " + str(months_short[month - 1]) + " " + str(year),
        )
        .mark_bar(clip=True, size=25)
        .encode(
            alt.X(
                "Total nights",
                title="Length of stay",
                scale=alt.Scale(domain=(1, 7)),
            ),
            alt.Y("Percent of Reservations", title="Percent of Reservations"),
            alt.Tooltip("Percent of Reservations"),
        )
        .properties(width=300, height=200)
        .configure_axis(labelFontSize=10, titleFontSize=15, grid=False)
        .configure_title(fontSize=19)
    )
    return stay.to_html()


if __name__ == "__main__":
    app.run_server(debug=True)