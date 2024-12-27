import streamlit as st

from app.scope import scope_player_round_components
from app.scope import scope_round_scores


def new_game_button(scope):

	widget_key = 'widget_' + 'new_game_button'
	button = st.button(
						label='New game (reset scores)',
						type='secondary',
						on_click=reset_game, 
						args=(scope, ),
						key=widget_key,
						)
	return button

def reset_game(scope):
	scope_round_scores(scope)
	scope_player_round_components(scope)

