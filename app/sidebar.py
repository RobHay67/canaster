import streamlit as st

from app.widgets.players import render_show_players_button
from app.widgets.scoreboard import render_scoreboard_heading
from app.widgets.scoreboard import render_scoreboard
from app.widgets.new_game import new_game_button
from scores.widgets.next_round import next_round_button

def render_sidebar(scope):
	with st.sidebar:
		st.title("Canaster Scorer")
		st.caption('version == 0.3')

		render_show_players_button(scope)
		st.divider()
		new_game_button(scope)
		# new_game = st.button("New Game", key="widget_new_game")
		st.divider()
		house_rules = st.button("House Rules", key="widget_house_rules")
		st.divider()
		
		if scope.game_started == True:
			round_number = str(scope.round_number)
			st.subheader('Round ' + round_number)
			next_round_button(scope)

			# render_scoreboard_heading(scope)
			# render_scoreboard(scope)




	






