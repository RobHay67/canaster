
import streamlit as st


def hand_slider_input(scope, player_no):
	widget_key = 'widget_' + 'hand_old_' + str(player_no) 

	number_input = st.slider(
								label = "Points in Hand (negative)", 
								value=scope['player_' + str(player_no) + '_hand'], 
								min_value=0, 
								max_value=500,
								step=5,
								on_change=change_hand, 
								args=(scope, player_no),
								key=widget_key,
								)

def hand_number_input(scope, player_no):
	widget_key = 'widget_' + 'hand_' + str(player_no) 

	number_input = st.number_input(
								label = "Points in Hand (negative)", 
								value=scope['player_' + str(player_no) + '_hand'], 
								min_value=0, 
								max_value=1000,
								step=5,
								on_change=change_hand, 
								args=(scope, player_no),
								key=widget_key,
								)


def change_hand(scope, player_no):
	new_value = scope['widget_' + 'hand_' + str(player_no)]
	prev_value = scope['player_' + str(player_no) + '_hand']

	scope['player_' + str(player_no) + '_hand'] = new_value

	# Update Score
	delta = prev_value - new_value
	scope['round_score_player_' + str(player_no)] += delta
