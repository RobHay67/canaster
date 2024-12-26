import streamlit as st

from scores.widgets.gone_out import gone_out_checkbox
from scores.widgets.concealed import gone_out_concealed_checkbox
from scores.widgets.canaster_natural import canaster_natural_number_input
from scores.widgets.canaster_dirty import canaster_dirty_number_input
from scores.widgets.red_threes import red_threes_number_input
from scores.widgets.hand import hand_slider
from scores.widgets.tabled import tabled_slider


def build_column(scope, player_name, player_no):

	# Render Score Widgets
	st.subheader(player_name)
	gone_out_checkbox(scope, player_no)
	gone_out_concealed_checkbox(scope, player_no)
	canaster_natural_number_input(scope, player_no)
	canaster_dirty_number_input(scope, player_no)
	red_threes_number_input(scope, player_no)
	tabled_slider(scope, player_no)
	hand_slider(scope, player_no)
	
	st.header(scope['round_score_player_' + str(player_no)])

