import pandas as pd
import plotly.graph_objs as go
import requests
import numpy as np
import plotly.colors
#from collections import OrderedDict
from pandas.io.json import json_normalize 


#country_default = OrderedDict([['Bulgaria', 'a'], ['Canada', 'h'], ['Croatia', 'g'], ['Cyprus', 'gh'], ['Egypt', 'hg'], ['France', 'go'], ['Germany', 'n'], ['Greece', 'gr'], ['Italy', 'it'], ['Jordan', 'j'], ['Kenya', 'ke'], ['Kuwait', 'ku'], ['Lebanon', 'lb'], ['Morocco', 'fg'], ['Romania', 'ro'], ['Russia', 'ru'], ['Spain', 'sp'], ['Turkey', 'tr'], ['UAE', 'ae'], ['UK', 'yl'], ['USA', 'usa'], ['Ukraine', 'uk']])
#countries=country_default
def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
  # when the countries variable is empty, use the country_default dictionary
    #if not bool(countries):
        #countries = country_default
    
    urls = []
    
    
    
    url = 'https://corona.lmao.ninja/v3/covid-19/countries'
    urls.append(url)
    r = requests.get(url)
    df = json_normalize(r.json())
    df = df.drop(['countryInfo._id', 'countryInfo.iso2', 'countryInfo.flag', 'updated','oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople'], axis=1)
    options = ['Bulgaria', 'Croatia', 'Cyprus', 'Egypt', 'France', 'Germany', 'Greece', 'Italy', 'Jordan', 'Kenya', 'Kuwait', 'Lebanon', 'Morocco', 'Romania', 'Russia', 'Spain', 'Turkey', 'UAE', 'Ukraine']
    df = df[df['country'].isin(options)]
    df = df.reset_index()
    df = df.drop('index', axis=1)
    country_list = df['country'].tolist()
    # first chart plots Today's: Cases, Deaths, Recovered  per Country 
    # as a relative bar chart
       
    graph_one = []
    df_one = pd.DataFrame(df)
    df_one.sort_values('todayCases', ascending=False, inplace=True)
    
    for country in country_list:
            x_val = df_one.country.tolist()
    graph_one.append(
      go.Bar(
      x = x_val,
      y = df_one.todayCases.tolist(),
      name = "Today's Cases"
      )
    )
    graph_one.append(go.Bar(
      x = x_val,
      y= df_one.todayDeaths.tolist(),
      name = "Today's Deaths"
      )
    )
    graph_one.append(go.Bar(
      x = x_val,
      y= df_one.todayRecovered.tolist(),
      name = "Today's Recovered",
      )
    )
        

    layout_one = dict(title = "Today's: Cases, Deaths, Recovered  per Country",
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Population'),
                barmode='relative',
                autosize=False,
                width=600,
                height=500
                )

    # second chart plots Cases, Deaths, Recovered and Critical per Country as a relative bar chart
    graph_two = []
    df_two = pd.DataFrame(df)
    df_two.sort_values('cases', ascending=False, inplace=True)
       
    for country in country_list:
        x_val = df_two.country.tolist()
    graph_two.append(
      go.Bar(
      x = x_val,
      y = df_two.cases.tolist(),
      name = 'Cases'
      )
    )
    graph_two.append(go.Bar(
      x = x_val,
      y= df_two.deaths.tolist(),
      name = 'Deaths'
      )
    )
    graph_two.append(go.Bar(
      x = x_val,
      y= df_two.recovered.tolist(),
      name = 'Recovered' 
      )
    )
    graph_two.append(go.Bar(
      x = x_val,
      y= df_two.critical.tolist(),
      name = 'Critical'  
      )
    )
        
    layout_two = dict(title = 'Cases, Deaths, Recovered and Critical per Country',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Population'),
                barmode='relative',
                autosize=False,
                width=600,
                height=500
                )


    
    # thirdrt plots ararble land for 2015 as a bar chart    
    graph_three = []
    df_three = pd.DataFrame(df)
    df_three.sort_values('casesPerOneMillion', ascending=False, inplace=True)
    
    for country in country_list:
            x_val = df_three.country.tolist()
    graph_three.append(
      go.Bar(
      x = x_val,
      y = df_three.casesPerOneMillion.tolist(),
      name = 'Cases Per One Million'
      )
    )
    graph_three.append(go.Bar(
      x = x_val,
      y= df_three.deathsPerOneMillion.tolist(),
      name = 'Deaths Per One Million' 
      )
    )
    graph_three.append(go.Bar(
      x = x_val,
      y= df_three.recoveredPerOneMillion.tolist(),
      name = 'Recovered Per One Million'
      )
    )

    layout_three = dict(title = 'Cases, Deaths, Recovered  Per One Million By Country',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Population'),
                barmode='relative',
                autosize=False,
                width=600,
                height=500
                )
    # second chart plots ararble land for 2015 as a bar chart    
    graph_four = []
    df_four = pd.DataFrame(df)
    df_four.sort_values('recoveredPerOneMillion', ascending=False, inplace=True)
    
    for country in country_list:
        x_val = df_four.country.tolist()
    graph_four.append(
      go.Bar(
      x = x_val,
      y = df_four.tests.tolist(),
      name = 'Tests'
      )
     )
    graph_four.append(go.Bar(
      x = x_val,
      y= df_three.testsPerOneMillion.tolist(),
      name = 'Tests Per One Million'
      )
    )
    
        
    layout_four = dict(title = 'Tests and Tests Per One Million By Country',
                xaxis = dict(title = 'Country'),
                yaxis = dict(title = 'Population'),
                barmode='stack',
                autosize=False,
                width=600,
                height=500
                )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))


    return figures