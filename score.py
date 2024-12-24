
# team_1_score = calculate_score(
# 			team_1_out, 
# 			team_1_red_threes, 
# 			team_1_natural_canasters, 
# 			team_1_dirty_canasters, 
# 			team_1_in_hand, 
# 			team_1_tabled
# 			)


import streamlit as st


# ['2 Players', '3 Players', '2 Teams', '3 Teams']

def render_scoring(scope):

	# so we either render 2 or 3 columns

	if scope.no_of_players in ['3 Players', '3 Teams']:
		col1, col2, col3 = st.columns(3)
		with col1:render_score_column(scope, scope.player_1, 1)
		with col2:render_score_column(scope, scope.player_2, 2)
		with col3:render_score_column(scope, scope.player_3, 3)
	else:
		col1, col2 = st.columns(2)
		with col1:render_score_column(scope, scope.player_1, 1)
		with col2:render_score_column(scope, scope.player_2, 2)
		
	
		

	



def calculate_score(out, concealed, red_threes, naturals, dirty, in_hand, tabled):
	round_score = 0

	if out == True: round_score += 100
	if concealed == True:round_score += 100
	
	if red_threes == 4 : round_score += 800
	if red_threes > 0 and red_threes < 4 : round_score += (red_threes*100)

	round_score += naturals * 500
	round_score += dirty * 300

	round_score += tabled
	round_score += in_hand * -1

	return round_score


def render_score_column(scope, player_name, col_no):

	# Create Variables
	player_out 			= 'player_' + str(col_no) + '_gone_out'
	player_concealed 	= 'player_' + str(col_no) + '_concealed'
	player_canasters 	= 'player_' + str(col_no) + '_canaster'
	player_unnaturals 	= 'player_' + str(col_no) + '_unnaturals'
	player_red_threes 	= 'player_' + str(col_no) + '_red_threes'
	player_in_hand		= 'player_' + str(col_no) + '_in_hand'
	player_tabled		= 'player_' + str(col_no) + '_tabled'
	# player_score		= 'player_' + str(col_no) + '_score'

	# Render Score Widgets
	st.subheader(player_name)
	# player_out 			= st.radio("Gone Out",["Gone Out", "Concealed"], key=player_out)
	player_out			= st.checkbox("Gone Out", value=False, key=player_out, on_change=check_who_went_out, args=(scope, col_no) )
	player_concealed	= st.checkbox("Concealed ?", value=False, key=player_concealed)
	player_canasters	= st.number_input("Natural Canaster", value=0, min_value=0, max_value=22, key=player_canasters)
	player_unnaturals	= st.number_input("Dirty Canaster", value=0, min_value=0, max_value=22, key=player_unnaturals)
	player_red_threes	= st.number_input("Red Threes", value=0, min_value=0, max_value=4, key=player_red_threes)
	player_in_hand		= st.slider("Points in Hand", value=0, min_value=0, max_value=500, step=5, key=player_in_hand)
	player_tabled		= st.slider("Points Tabled", value=0, min_value=0, max_value=1500, step=5, key=player_tabled)

	score = calculate_score(
		player_out, 
		player_concealed,
		player_red_threes, 
		player_canasters, 
		player_unnaturals, 
		player_in_hand, 
		player_tabled
		)
	
	st.header(score)


def check_who_went_out(scope, col_no):
	st.write('Player out was pressed > ', col_no )

	# which control was ticker
	player_out 			= 'player_' + str(col_no) + '_gone_out'
	player_concealed 	= 'player_' + str(col_no) + '_concealed'

	current_out = scope[player_out]
	current_concealed = scope[player_concealed]


	# so we need to check the state of other variables
	st.write('Current Out 			= ', current_out)
	st.write('Current Concealment 	= ', current_concealed)










# with col2:
# 		st.subheader(scope.player_2)
# 		team_2_out = st.radio("Gone Out",["Gone Out", "Concealed"], key='team_2_out')
# 		team_2_natural_canasters	= st.number_input("Natural Canaster", value=0, min_value=0, max_value=22, key='team_2_natural_canasters')
# 		team_2_dirty_canasters		= st.number_input("Dirty Canaster", value=0, min_value=0, max_value=22, key='team_2_dirty_canasters')
# 		team_2_red_threes			= st.number_input("Red Threes", value=0, min_value=0, max_value=4, key='team_2_red_threes')
# 		team_2_in_hand				= st.slider("Points in Hand", value=0, min_value=0, max_value=500, step=5, key='team_2_point_in_hand')
# 		team_2_tabled				= st.slider("Points Tabled", value=0, min_value=0, max_value=1500, step=5, key='team_2_point_on_deck')


# 		team_2_score = calculate_score(
# 			team_2_out, 
# 			team_2_red_threes, 
# 			team_2_natural_canasters, 
# 			team_2_dirty_canasters, 
# 			team_2_in_hand, 
# 			team_2_tabled
# 			)
# 		st.write(team_2_out)
# 		st.header(team_2_score)

# 	with col2:
# 		st.subheader(scope.player_3)
# 		team_3_out = st.radio("Gone Out",["Gone Out", "Concealed"], key='team_3_out')
# 		team_3_natural_canasters	= st.number_input("Natural Canaster", value=0, min_value=0, max_value=22, key='team_3_natural_canasters')
# 		team_3_dirty_canasters		= st.number_input("Dirty Canaster", value=0, min_value=0, max_value=22, key='team_3_dirty_canasters')
# 		team_3_red_threes			= st.number_input("Red Threes", value=0, min_value=0, max_value=4, key='team_3_red_threes')
# 		team_3_in_hand				= st.slider("Points in Hand", value=0, min_value=0, max_value=500, step=5, key='team_3_point_in_hand')
# 		team_3_tabled				= st.slider("Points Tabled", value=0, min_value=0, max_value=1500, step=5, key='team_3_point_on_deck')


# 		team_3_score = calculate_score(
# 			team_2_out, 
# 			team_2_red_threes, 
# 			team_2_natural_canasters, 
# 			team_2_dirty_canasters, 
# 			team_2_in_hand, 
# 			team_2_tabled
# 			)
# 		st.write(team_3_out)
# 		st.header(team_3_score)



