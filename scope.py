import streamlit as st


def scope_init(scope):
	

	# print_system_info_to_terminal()
	# set_streamlit_page_config()								# should only run onetime
	
	if 'initialised' not in scope:	
		scope.initialised = True
		# scope.allow_auto_login = True			# TODO for releases purposes only - delete later
		# scope.config = {}
		# scope.config['project_description'] = 'Share Picker'
		# scope.config['project_start_time'] 	= time.time()
		
		scope.show_players = False
		scope.show_scoring = False
		scope.round_number = 1

		scope.no_of_players = None

		scope.player_1 = 'Rob'
		scope.player_2 = 'Fliss'
		scope.player_3 = ''
		scope.player_1_score = 0
		scope.player_2_score = 0
		scope.player_3_score = 0

		


	print(scope)
	return scope
