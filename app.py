import streamlit as st
import pandas as pd
import pickle

teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Punjab Kings',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals',
         'Lucknow Super Giants',
         'Gujarat Titans']

cities = ['Ahmedabad', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah',
          'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad', 'Visakhapatnam',
          'Chandigarh', 'Bengaluru', 'Kolkata', 'Jaipur', 'Indore',
          'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
          'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
          'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Win Predictor')
st.image("https://i1.wp.com/crickettimes.com/wp-content/uploads/2023/03/IPL-2023-broadcast-and-streaming-details-1260x657.jpg?strip=all")

col1, col2 = st.columns(2)

with col1:
    BattingTeam = st.selectbox('Batting Team', sorted(teams))
with col2:
    BowlingTeam = st.selectbox('Bowling Team', sorted(teams))

selected_city = st.selectbox('Select Venue', sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs Completed')
with col5:
    wickets = st.number_input('Wickets')

if st.button('Predict'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({'BattingTeam': [BattingTeam], 'BowlingTeam': [BowlingTeam],
                         'City': [selected_city], 'runs_left': [runs_left], 'balls_left': [balls_left],
                         'wickets_left': [wickets], 'total_run_x': [target], 'crr': [crr], 'rrr': [rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(BattingTeam + "- " + str(round(win * 100)) + "%")
    st.header(BowlingTeam + "- " + str(round(loss * 100)) + "%")
