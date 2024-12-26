import streamlit as st


def red_threes_number_input(scope, player_no):
	widget_key = 'widget_' + 'red_threes_' + str(player_no) 

	number_input = st.number_input(
								label = "Red Threes", 
								value=scope['player_' + str(player_no) + '_red_threes'], 
								min_value=0, 
								max_value=4,
								on_change=change_red_threes, 
								args=(scope, player_no),
								key=widget_key,
								)


def change_red_threes(scope, player_no):
	new_value = scope['widget_' + 'red_threes_' + str(player_no)]
	prev_value = scope['player_' + str(player_no) + '_red_threes']

	scope['player_' + str(player_no) + '_red_threes'] = new_value

	# Update Score
	if new_value == 4: 
		# prev value was 3 so 300 (you get 4 x 200 for all 4 red 3s) so 5 is the delta
		delta = 5
	elif prev_value == 4:
		# this score must be 300 (last score was 800) so -5
		delta = -5
	else:
		delta = new_value - prev_value
	scope['round_score_player_' + str(player_no)] += (delta * 100)

