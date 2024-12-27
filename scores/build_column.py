import streamlit as st

from scores.widgets.gone_out import gone_out_checkbox
from scores.widgets.concealed import gone_out_concealed_checkbox
from scores.widgets.canaster_natural import canaster_natural_number_input
from scores.widgets.canaster_dirty import canaster_dirty_number_input
from scores.widgets.red_threes import red_threes_number_input
from scores.widgets.tabled import tabled_slider_input, tabled_number_input
from scores.widgets.hand import hand_slider_input, hand_number_input

def build_column(scope, player_name, player_no):

	
	total_score = scope['score_total_player_' + str(player_no)]
	st.subheader(player_name + '   ( ' + str(total_score) + ' )')

	st.write('points down = ', points_down_score(total_score) )
	st.write('')

	# Render Score Widgets
	gone_out_checkbox(scope, player_no)
	gone_out_concealed_checkbox(scope, player_no)
	canaster_natural_number_input(scope, player_no)
	canaster_dirty_number_input(scope, player_no)
	red_threes_number_input(scope, player_no)
	tabled_number_input(scope, player_no)
	hand_number_input(scope, player_no)

	# Score for this round
	round_number = str(scope.round_number)
	round_score = str(scope['round_score_player_' + str(player_no)])
	# st.subheader('round ' + round_number + ' score = ' + round_score)
	st.subheader(round_score)


def points_down_score(total_score):

	points_down = 0

	if total_score <  	0 	 : points_down = 0
	if total_score > 0 and total_score <= 1500 : 
		points_down = 50
	if total_score >= 1500 and total_score < 3000: 
		points_down = 90
	if total_score >= 3000: 
		points_down = 120
		
	return points_down