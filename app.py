import random
# from turtle import bgcolor
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from fpdf import FPDF
import plotly.graph_objects as go
# Load model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Team logo and color dictionary
team_logos = {
    "Sunrisers Hyderabad": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFNUOHxX-5sofC3Iioht3A6_naxWEImhNUKs6eU6xqjxYJjOa1OLc_hxKRkckg_F6bnG2XzSrAsKQpgYpeXPzFkwNLHQwS5xVrYaL7aKn155nR2J0dPCunLn4LrR8d-bLjqfaLhpAG2tGRZF4RuWgblEy_1DhbmszchchOWOs3ZwAZ_Lj-1bT535Ye/s7200/Original%20Sunrisers%20Hyderabad%20PNG-SVG%20File%20Download%20Free%20Download.png", "#f26522"),
    "Mumbai Indians": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcIHFJONN-c6wVsb8I0TI5u1He8Vh5aUlmZ7vPzd6paraXfCf5r-bNdOoT3rqBA5S8Yu3DwefbB4C_Utu6a4E1XUXtdo28k2ViLDYs2fDS7cG9LO0S6ESd5pEZrE1GvYAf6M0_dTs9OibYMQAwkOQZvALvo-ggMxtTh_4JINiQsYeBWtQ0APFedzCZ/s7200/Original%20Mumbai%20Indians%20PNG-SVG%20File%20Download%20Free%20Download.png", "#045093"),
    "Royal Challengers Bangalore": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEMirAmSelGzQqwMqkzMifgCNy9asa4lGjk7tFe7WlVAQ3NU7eGj8nP0c-NRXNY6ZN5FgrDJV0k_UjOLa8rUHJDfEzFsj9qxgL_DxfB0y4RlFli0AnCxNqWXZ9wCATAZ1FBoZafwsUWddYNpVOyBEAxK7yIdLy4OkVjkUMEDErfWKE_54Rt2WW9iXL/s1178/Original%20Royal%20Challengers%20Bangalore%20PNG-SVG%20File%20Download%20Free%20Download.png", "#d71920"),
    "Kolkata Knight Riders": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhw4FPuHDf0g4n2Gaf_prBrTXdS7GO6zGVcS-Lx4ioHzH-HUUGm5gY7Sj2vmy_6HwxtSZ2fojvZrXqCUIljlZy_aenyml7DLwx3mRXTS-qWBHsBFpt85nq8Y7__HB6uK3JystxJDwx0KoLubgsAIWIH6xXoh2nxjLDM2bNV08uHlBj3zy6SQmfSIUuZ/s1024/Original%20Kolkata%20Knight%20Riders%20PNG-SVG%20File%20Download%20Free%20Download.png", "#3b215d"),
    "Kings XI Punjab": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWofXDOj6B3eYR3eBKQaPeJjTsblyohHrqK1JO4BEojD0u_Izr_2kIxmrI7Oli8_EvW9tNxB4Qi_OotqkyIWTkOsg6xIroj5U39vvmbGDPSJJXkSn5mzAF58_Mz5Fg8uIrXfJnXWlWrqSig2uxfuUGCrV3wPlZwuZ1OtWVXZUhWYeIzJyrH7klLVer/s1540/Original%20Punjab%20Kings%20PNG-SVG%20File%20Download%20Free%20Download.png", "#d71920"),
    "Chennai Super Kings": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn3plcgt5OnAx_VelXAj9Z8TWBiqg6B-xgCJ__kuFeXr1ClntuhvVu0IugURU6TfyHk9qUuECEpos1E5ayEmx0fAupMIvNLQnLOwavDhBYxkIwvRv9cmm7_qHZmlcSwr3Un-hJpy92AooR9Qn77PUcr4yRgAORYwoTBjTYOmyYlHbZ0nDyaL3HWqUk/s2141/Original%20Chennai%20Super%20Fun%20Logo%20PNG%20-%20SVG%20File%20Download%20Free%20Download.png", "#fdb913"),
    "Rajasthan Royals": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHxGVAL3asVmq-N8vAbTJ0Wk1C7WQNO4yr_O-7dIDgrszmr7L1ODXPuc5IzB8VGr941igDjeEX8OSZ1db2sDpn5uziRk1BVYAVRZBltH4A5FJGhfjmn8PzDLcP7qxCXVyuYQr1uaLktAqoNefxAgjVGXGXIcec8WYXBO4lB-4vtCCmcu2C9RhG5XXm/s1024/Original%20Rajasthan%20Royals%20Logo%20PNG-SVG%20File%20Download%20Free%20Download.png", "#254aa5"),
    "Delhi Capitals": ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixNFCNIFm0aH1xUBTkbrLQdE__aSNP32JP1zsee3iJW5va96W_r3qyl486fHQilJQjaVBJt0Fl0xAawdBD4duYEg6Sj-MgCNvVfWuA3UpO4oXBr4qt8WeaaS2Fhtbac8mfzE_euPhJ9hQUVxAgWQDLG1WgrJaSv1I2L4XgNGvFoxrdWQq_LUi82XIw/s944/Original%20Delhi%20Capitals%20Logo%20PNG-SVG%20File%20Download%20Free%20Download.png", "#17449b")
}


# Dynamic background theme

# Streamlit config
st.set_page_config(page_title="IPL Win Predictor", layout="wide")
st.title('🏏 IPL Win Predictor')
st.image("https://i1.wp.com/crickettimes.com/wp-content/uploads/2023/03/IPL-2023-broadcast-and-streaming-details-1260x657.jpg?strip=all")

teams = sorted(list(team_logos.keys()))

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the batting team', teams)
    st.image(team_logos[batting_team][0], width=100)
with col2:
    bowling_team = st.selectbox('Select the bowling team', teams)
    st.image(team_logos[bowling_team][0], width=100)

cities = sorted([
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru']
)
selected_city = st.selectbox('Match City', cities)
target = st.number_input('Target Score', min_value=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score', min_value=0)
with col4:
    wickets = st.number_input('Wickets Lost', min_value=0, max_value=9)
with col5:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)

# Session state
st.session_state.setdefault('show_chart', False)
st.session_state.setdefault('history', [])

if st.button('🎯 Predict Win Probability'):
    if batting_team == bowling_team:
        st.error('Batting and bowling teams must be different.')
        st.stop()
    if overs == 0:
        st.warning('Please enter overs completed.')
        st.stop()

    runs_left = target - score
    balls_left = 120 - int(overs * 6)
    remaining_wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [remaining_wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(df)
    r_1 = round(result[0][0] * 100)
    r_2 = round(result[0][1] * 100)

    # Bar View
    st.subheader("📊 Win Probability")
    st.markdown(f"""
    <div style="border: 1px solid #ccc; border-radius: 10px; overflow: hidden; height: 45px; display: flex;">
        <div style="width: {r_2}%; background-color: {team_logos[batting_team][1]}; color: white; display: flex; align-items: center; justify-content: center;">
            {batting_team} {r_2}%
        </div>
        <div style="width: {r_1}%; background-color: {team_logos[bowling_team][1]}; color: white; display: flex; align-items: center; justify-content: center;">
            {bowling_team} {r_1}%
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.session_state['stored_result'] = (r_1, r_2, batting_team, bowling_team, runs_left, balls_left, remaining_wickets, crr, rrr, selected_city)
    st.session_state['history'].append({"bat": batting_team, "bowl": bowling_team, "city": selected_city, "bat%": r_2, "bowl%": r_1})

    with st.expander("📋 Match Summary"):
        st.write(f"🏟️ **City**: {selected_city}")
        st.write(f"🏏 **{batting_team}**: {score}/{10 - remaining_wickets} in {overs} overs")
        st.write(f"🎯 **Target**: {target}")
        st.write(f"📉 **Runs Left**: {runs_left}, **Balls Left**: {balls_left}")

    if r_2 > r_1:
        st.success(f"{batting_team} is in a strong position! Needs {runs_left} runs from {balls_left} balls.")
    else:
        st.warning(f"{bowling_team} has the upper hand! {batting_team} needs {runs_left} from {balls_left} balls with only {remaining_wickets} wickets left.")

    colA, colB, colC = st.columns(3)
    with colA:
        st.metric("Current Run Rate", round(crr, 2))
    with colB:
        st.metric("Required Run Rate", round(rrr, 2))
    with colC:
        st.metric("Wickets Remaining", remaining_wickets)

    st.subheader("🏏 Target Progress")
    st.progress(min(score / target, 1.0))

# Pie chart
if st.button("📎 Show Pie Chart"):
    st.session_state['show_chart'] = True

if st.session_state.get('show_chart') and 'stored_result' in st.session_state:
    r_1, r_2, batting_team, bowling_team, *_ = st.session_state['stored_result']

    fig = go.Figure(data=[go.Pie(
        labels=[f"{batting_team} ({r_2}%)", f"{bowling_team} ({r_1}%)"],
        values=[r_2, r_1],
        hole=0.4,
        marker=dict(colors=[team_logos[batting_team][1], team_logos[bowling_team][1]]),
        textinfo='label+percent',
        hoverinfo='label+value',
    )])

    fig.update_layout(
        title="🎯 Win Probability Pie Chart",
        annotations=[dict(text='Win %', x=0.5, y=0.5, font_size=20, showarrow=False)],
        showlegend=False,
        paper_bgcolor='white',  # You can change this if you add theme toggle
        margin=dict(t=40, b=20, l=20, r=20)
    )

    st.plotly_chart(fig, use_container_width=True)

# Export PDF
if st.button("📝 Export Summary as PDF") and 'stored_result' in st.session_state:
    r_1, r_2, batting_team, bowling_team, runs_left, balls_left, remaining_wickets, crr, rrr, city = st.session_state['stored_result']
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="IPL Win Prediction Summary", ln=1, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"City: {city}", ln=1)
    pdf.cell(200, 10, txt=f"Batting Team: {batting_team}", ln=1)
    pdf.cell(200, 10, txt=f"Bowling Team: {bowling_team}", ln=1)
    pdf.cell(200, 10, txt=f"Win Chances: {batting_team} - {r_2}%, {bowling_team} - {r_1}%", ln=1)
    pdf.cell(200, 10, txt=f"Runs Left: {runs_left}, Balls Left: {balls_left}", ln=1)
    pdf.cell(200, 10, txt=f"Wickets Remaining: {remaining_wickets}", ln=1)
    pdf.cell(200, 10, txt=f"CRR: {round(crr, 2)}, RRR: {round(rrr, 2)}", ln=1)
    pdf.output("match_summary.pdf")
    st.success("PDF exported as match_summary.pdf")

# Show history
if st.button("📂 Show Historical Predictions"):
    if st.session_state['history']:
        hist_df = pd.DataFrame(st.session_state['history'])
        st.dataframe(hist_df)
    else:
        st.info("No history found yet.")

# Reset all session state
if st.button("🔁 Reset Inputs"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
