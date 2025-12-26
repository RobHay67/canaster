
import streamlit as st



def canaster_dirty_number_input(scope, player_no):
	widget_key = 'widget_' + 'canaster_dirty_' + str(player_no) 

	number_input = st.number_input(
								label = "Un-Natural Canaster", 
								value=int(scope['player_' + str(player_no) + '_canaster_dirty']), 
								min_value=0, 
								max_value=22,
								on_change=change_canaster_dirty, 
								args=(scope, player_no),
								key=widget_key,
								)


def change_canaster_dirty(scope, player_no):
	new_value = scope['widget_' + 'canaster_dirty_' + str(player_no)]
	prev_value = scope['player_' + str(player_no) + '_canaster_dirty']

	scope['player_' + str(player_no) + '_canaster_dirty'] = new_value

	# Update Score
	delta = new_value - prev_value
	scope['round_score_player_' + str(player_no)] += (delta * 300)
