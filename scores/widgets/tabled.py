
import streamlit as st



def tabled_slider(scope, player_no):
	widget_key = 'widget_' + 'tabled_' + str(player_no) 

	number_input = st.slider(
								label = "Points Tabled", 
								value=scope['player_' + str(player_no) + '_tabled'], 
								min_value=0, 
								max_value=1500,
								step=5,
								on_change=change_tabled, 
								args=(scope, player_no),
								key=widget_key,
								)


def change_tabled(scope, player_no):
	new_value = scope['widget_' + 'tabled_' + str(player_no)]
	prev_value = scope['player_' + str(player_no) + '_tabled']

	scope['player_' + str(player_no) + '_tabled'] = new_value

	# Uodate Score
	delta = new_value - prev_value
	scope['round_score_player_' + str(player_no)] += delta


