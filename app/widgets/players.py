import streamlit as st


def render_show_players_button(scope):
	show_players = st.button(
		label="Players", 
		key="widget_players",
		on_click=change_player_button_status, args=(scope, ),
		# type='primary',
		)
	

def change_player_button_status(scope):
	previous_value = scope.show_players
	new_value = True if previous_value == False else False

	scope.show_players = new_value
	scope.show_scoring = False
