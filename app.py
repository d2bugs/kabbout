import streamlit as st


st.set_page_config(layout="wide", page_title="Kabbout", page_icon=":smiley:",initial_sidebar_state="expanded")
hide_streamlit_style = """
<style>
button[kind="header"] {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Kabbout :smiley:")
# add players from 2-4
st.sidebar.title("Add Players")
player1 , player2, player3, player4 = None, None, None, None
player1 = st.sidebar.text_input("Player 1")
# add a button to remove player
player2 = st.sidebar.text_input("Player 2")
player3 = st.sidebar.text_input("Player 3")
player4 = st.sidebar.text_input("Player 4")
addPlayers = st.sidebar.button("Add Players")
players = [player1, player2, player3, player4]

players = [player for player in players if player != '']
# make names first letter capital

if players in [None, []]:
    st.warning("Please add players")
playerScores = None
if players not in [None, []]:
    # add scores
    st.title("Add Scores")
    if len(players) == 1:
        st.warning("Please add more players")
    if player1 not in [None, '']:
        score1 = st.number_input(f"{player1.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score1")
        scores = [int(score1)]
    if player2 not in [None, '']:
        score2 = st.number_input(f"{player2.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score2")
        scores = [int(score1), int(score2)]
    if player3 not in [None, '']:
        score3 = st.number_input(f"{player3.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score3")
        scores = [int(score1), int(score2), int(score3)]
    if player4 not in [None, '']:
        score4 = st.number_input(f"{player4.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score4")
        scores = [int(score1), int(score2), int(score3), int(score4)]
    addScores = st.button("Add Scores")
    
        # remove empty scores
    playerScores = {player: score for player, score in zip(players, scores) if player != '' or score != 0}
    # table that doesnt have index column
    # sort dict by value
    playerScores = dict(sorted(playerScores.items(), key=lambda item: item[1],reverse=True))
    findHighScore = max(playerScores.values())
    findMidHighScore = max(playerScores.values())-50
    findMidLowScore = min(playerScores.values())+50
    findLowScore = min(playerScores.values())
    
    if playerScores not in [None, {}]:
        st.table(playerScores)
        st.bar_chart(playerScores)