import streamlit as st

from app.scope import scope_player_round_components


def next_round_button(scope):

	widget_key = 'widget_' + 'next_round_button'
	button = st.button(
						label='Next Round (apply scores)',
						type='primary',
						on_click=update_total_scores, 
						args=(scope, ),
						key=widget_key,
						)
	return button


def update_total_scores(scope):
	scope.score_total_player_1 += scope.round_score_player_1
	scope.score_total_player_2 += scope.round_score_player_2
	scope.score_total_player_3 += scope.round_score_player_3
	# Reset the scores for the next round
	scope.round_score_player_1 = 0
	scope.round_score_player_2 = 0
	scope.round_score_player_3 = 0
	scope_player_round_components(scope)