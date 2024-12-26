import streamlit as st


def scope_init(scope):
	

	# print_system_info_to_terminal()
	# set_streamlit_page_config()								# should only run onetime
	
	if 'initialised' not in scope:	
		scope.initialised = True

		# Game Info
		scope.players_qty = None				# 2 or 3
		scope.players_button = '2 Players'
		scope.game_started = False

		# Screens to Display (single page app)
		scope.show_players = False
		scope.show_scoring = False
		
		# Player Details
		scope.player_1 = 'Rob'
		scope.player_2 = 'Fliss'
		scope.player_3 = None

		scope_round_scores(scope)
		scope_player_round_components(scope)	

	return scope

def scope_round_scores(scope):
	# Score Tracking
	scope.round_number = 1
	scope.round_score_player_1 = 0
	scope.round_score_player_2 = 0
	scope.round_score_player_3 = 0
	scope.score_total_player_1 = 0
	scope.score_total_player_2 = 0
	scope.score_total_player_3 = 0



def scope_player_round_components(scope):
	for player_no in [1,2,3]:
		scope['player_' + str(player_no) + '_gone_out'] = False
		scope['player_' + str(player_no) + '_concealed'] = False
		scope['player_' + str(player_no) + '_canaster'] = 0
		scope['player_' + str(player_no) + '_canaster_dirty'] = 0
		scope['player_' + str(player_no) + '_red_threes'] = 0
		scope['player_' + str(player_no) + '_hand'] = 0
		scope['player_' + str(player_no) + '_tabled'] = 0



		


