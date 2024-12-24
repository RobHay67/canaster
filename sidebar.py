import streamlit as st


def render_sidebar(scope):
	with st.sidebar:
		st.header("Canaster Scorer")

		players = st.button("Players", key="widget_players")
		end_round = st.button("End Round", key="widget_end_round")
		new_game = st.button("New Game", key="widget_new_game")
		house_rules = st.button("House Rules", key="widget_house_rules")


		if players:
			scope.show_players = True

		
		st.write('Rounds')


