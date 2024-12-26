import streamlit as st

def gone_out_checkbox(scope, player_no):
	widget_key = 'widget_' + 'gone_out_' + str(player_no) 

	number_input = st.checkbox(
								label = "Gone Out", 
								value=scope['player_' + str(player_no) + '_gone_out'], 
								on_change=check_who_went_out, 
								args=(scope, player_no),
								key=widget_key,
								)


def set_other_player_out_status_to_false(scope, player_no):
	player_x_prev_out_status = scope['player_' + str(player_no) + '_gone_out']
	player_x_prev_con_status = scope['player_' + str(player_no) + '_concealed']

	if player_x_prev_out_status == True:
		scope['player_' + str(player_no) + '_gone_out'] = False
		scope['round_score_player_' + str(player_no)] += -100

	if player_x_prev_con_status == True:
		scope['player_' + str(player_no) + '_concealed'] = False
		scope['round_score_player_' + str(player_no)] += -100
		


def check_who_went_out(scope, player_no):
	# Only 1 player can go out so we need to override/untick
	# other players who are also ticked as having gone out
	# we assume the latest tick is correct
	# this function updates the latest column and scores
	
	new_status = scope['widget_' + 'gone_out_' + str(player_no)]
	
	if player_no == 1: # we are updating player 1
		if scope.player_1_gone_out  == False : 
			scope.round_score_player_1 += 100
		else : scope.round_score_player_1 += -100
		set_other_player_out_status_to_false(scope, 2)
		set_other_player_out_status_to_false(scope, 3)
	if player_no == 2:
		if scope.player_2_gone_out  == False : 
			scope.round_score_player_2 += 100
		else : scope.round_score_player_2 += -100
		set_other_player_out_status_to_false(scope, 1)
		set_other_player_out_status_to_false(scope, 3)
	if player_no == 3:
		if scope.player_3_gone_out  == False : 
			scope.round_score_player_3 += 100
		else : scope.round_score_player_3 += -100
		set_other_player_out_status_to_false(scope, 1)
		set_other_player_out_status_to_false(scope, 2)

	# store the new status
	scope['player_' + str(player_no) + '_gone_out'] = new_status




