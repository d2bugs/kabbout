import streamlit as st


st.set_page_config(layout="wide", page_title="Kabbout", page_icon=":smiley:",initial_sidebar_state="expanded")
hide_streamlit_style = """
<style>
button[data-testid="manage-app-button"] {visibility: hidden;}
button[kind="header"] {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Kabbout :smiley:")
# i wanna add a gif here
st.markdown("""<iframe src="https://giphy.com/embed/l2JefM9MQ21ARH5tK" width="100%" height="350px" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>""",unsafe_allow_html=True)
# add players from 2-4
st.sidebar.title("Add Players")
player1 , player2, player3, player4 = None, None, None, None
known_players = st.sidebar.toggle("Known Players")
if known_players:
    players = st.sidebar.multiselect("Players",['Saleh','Morta','Achref','Mehdi','Abbes','Khalil','Sandra','Fatma'])
    if len(players)==1:
        st.warning("Please add more players")
    if len(players)==2:
        player1 , player2 = players[0], players[1]
    if len(players)==3:
        player1 , player2 , player3 = players[0], players[1], players[2]
    elif len(players)==4:
        player1 , player2 , player3 , player4 = players[0], players[1], players[2], players[3]
else:
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
scores = None
if players not in [None, []]:
    # add scores
    st.sidebar.title("Add Scores")
    if len(players) == 1:
        st.warning("Please add more players")
    if player1 not in [None, '']:
        score1 = st.sidebar.number_input(f"{player1.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score1")
        if score1:
            scores = [int(score1)]
    if player2 not in [None, '']:
        score2 = st.sidebar.number_input(f"{player2.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score2")
        if score2:
            scores = [int(score1), int(score2)]
    if player3 not in [None, '']:
        score3 = st.sidebar.number_input(f"{player3.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score3")
        if score3:
            scores = [int(score1), int(score2), int(score3)]
    if player4 not in [None, '']:
        score4 = st.sidebar.number_input(f"{player4.capitalize()}'s Score", value=0, step=50, min_value=0, max_value=1500, key="score4")
        if score4:
            scores = [int(score1), int(score2), int(score3), int(score4)]
    addScores = st.sidebar.button("Add Scores")
    
    # remove empty scores
    if scores != [] or scores != None and addScores:
        playerScores = {player: score for player, score in zip(players, scores) if player != '' or score != 0}
    # table that doesnt have index column
    # sort dict by value
    playerScores = dict(sorted(playerScores.items(), key=lambda item: item[1],reverse=True))
    findMidHighScore , findMidHighScorePlayer = 0, 0
    midHighPlayer = None
    findHighScorePlayer = playerScores[max(playerScores, key=playerScores.get)]
    # get player name with highest score
    high = playerScores[max(playerScores)]
    # get player name with lowest score
    low = playerScores[min(playerScores, key=playerScores.get)]

    PLAYERS = []
    for player, score in playerScores.items():
        PLAYERS.append([player, score])
    PLAYERS.sort(key=lambda x: x[1], reverse=True)
    findHighScore = PLAYERS[0][1]
    findHighScorePlayer = PLAYERS[0][0]
    findMidHighScore = PLAYERS[1][1]
    findMidHighScorePlayer = PLAYERS[1][0]
    findMidLowScore = PLAYERS[-2][1]
    findMidLowScorePlayer = PLAYERS[-2][0]
    findLowScore = PLAYERS[-1][1]
    findLowScorePlayer = PLAYERS[-1][0]
    if playerScores not in [None, {}]:
        st.table(playerScores)
        if scores != []:
            # bar chart  arrange from lowest to highest
            st.bar_chart(scores)
        if findHighScore > 1000 and len(players) == 4:
            st.title("Results")
            st.write(f"L 7ALLOUF: {findLowScorePlayer} with **{findLowScore}**")
            st.write(f"HAB YJI LOWEL: {findMidLowScorePlayer} with **{findMidLowScore}**")
            st.write(f"YBET YHAREB: {findMidHighScorePlayer} with **{findMidHighScore}**")
            st.write(f"KAHBET E TAWLA: {findHighScorePlayer} with **{findHighScore}**")
        elif findHighScore > 1000 and len(players) == 3:
            st.title("Results")
            st.write(f"L 7ALLOUF: {findLowScorePlayer} with **{findLowScore}**")
            st.write(f"HAB YJI LOWEL: {findMidLowScorePlayer} with **{findMidLowScore}**")
            st.write(f"KAHBET E TAWLA: {findHighScorePlayer} with **{findHighScore}**")
        elif findHighScore > 1000 and len(players) == 2:
            st.title("Results")
            st.write(f"L 7ALLOUF: {findLowScorePlayer} with **{findLowScore}**")
            st.write(f"KAHBET E TAWLA: {findHighScorePlayer} with **{findHighScore}**")