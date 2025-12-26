import streamlit as st

from scores.widgets.gone_out import set_other_player_out_status_to_false


def gone_out_concealed_checkbox(scope, player_no):
	widget_key = 'widget_' + 'gone_out_concealed_' + str(player_no) 

	number_input = st.checkbox(
								label = "Concealed Out ?", 
								value=scope['player_' + str(player_no) + '_concealed'], 
								on_change=update_gone_out, 
								args=(scope, player_no),
								key=widget_key,
								)


def auto_update_out_status(scope, player_no):
	previous_out_status = scope['player_' + str(player_no) + '_gone_out']
	new_concealed_status = scope['widget_' + 'gone_out_concealed_' + str(player_no)]

	if new_concealed_status is True:
		if previous_out_status is False:
			scope['player_' + str(player_no) + '_gone_out'] = True
			scope['round_score_player_' + str(player_no)] += 100
			

def update_gone_out(scope, player_no):
	# Only 1 player can go out so we need to override/untick
	# other players who are also ticked as having gone out
	# we assume the latest tick is correct
	# this function updates the latest column and scores
	
	new_status = scope['widget_' + 'gone_out_concealed_' + str(player_no)]
	
	if player_no == 1: # we are updating player 1
		if scope.player_1_concealed is False : 
			scope.round_score_player_1 += 100
			auto_update_out_status(scope, 1)
		else :
			scope.round_score_player_1 += -100
		set_other_player_out_status_to_false(scope, 2)
		set_other_player_out_status_to_false(scope, 3)
	if player_no == 2:
		if scope.player_2_concealed is False : 
			scope.round_score_player_2 += 100
			auto_update_out_status(scope, 2)
		else : 
			scope.round_score_player_2 += -100
		set_other_player_out_status_to_false(scope, 1)
		set_other_player_out_status_to_false(scope, 3)
	if player_no == 3:
		if scope.player_3_concealed is False : 
			scope.round_score_player_3 += 100
			auto_update_out_status(scope, 3)
		else : 
			scope.round_score_player_3 += -100
		set_other_player_out_status_to_false(scope, 1)
		set_other_player_out_status_to_false(scope, 2)

	# store the new status
	scope['player_' + str(player_no) + '_concealed'] = new_status



