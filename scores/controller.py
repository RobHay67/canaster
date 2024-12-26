import streamlit as st

from scores.build_column import build_column
from scores.widgets.next_round import next_round_button


def render_scoring(scope):
	# so we either render 2 or 3 columns
	if scope.players_qty == 2:
		col1, col2 = st.columns(2)
		with col1:build_column(scope, scope.player_1, 1)
		with col2:build_column(scope, scope.player_2, 2)
	else:
		col1, col2, col3 = st.columns(3)
		with col1:build_column(scope, scope.player_1, 1)
		with col2:build_column(scope, scope.player_2, 2)
		with col3:build_column(scope, scope.player_3, 3)
		
	next_round_button(scope)
		





















