import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:image/png;base64,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')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="No of countries")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="No of countries")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="No of countries")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'), annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=temp_df, x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)



