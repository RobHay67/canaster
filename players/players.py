import streamlit as st


def render_player_config(scope):

	# How many people/teams are playing
	scope.players_qty = st.pills(
		"Game Type / Participants", 
		['2 Players', '3 Players', '2 Teams', '3 Teams'], 
		selection_mode="single",
		default = scope.players_button
		)
	
	col1, col2, col3 = st.columns(3)

	if scope.players_qty == '2 Players':
		scope.players_qty = 2
		with col1 : scope.player_1 = st.text_input("Name of Player 1", scope.player_1 )
		with col2 : scope.player_2 = st.text_input("Name of Player 1", scope.player_2)
	
	if scope.players_qty == '3 Players':
		scope.players_qty = 3
		with col1 : scope.player_1 = st.text_input("Name of Player 1", scope.player_1 )
		with col2 : scope.player_2 = st.text_input("Name of Player 2", scope.player_2)
		with col3 : scope.player_3 = st.text_input("Name of Player 3", scope.player_3, placeholder='this')
	
	if scope.players_qty == '2 Teams':
		scope.no_of_teams = 2
		with col1 : scope.player_1 = st.text_input("Name of Team 1", scope.player_1)
		with col2 : scope.player_2 = st.text_input("Name of Team 2", scope.player_2)

	if scope.players_qty == '3 Teams':
		scope.no_of_teams = 3
		with col1 : scope.player_1 = st.text_input("Name of Team 1", scope.player_1)
		with col2 : scope.player_2 = st.text_input("Name of Team 2", scope.player_2)
		with col3 : scope.player_3 = st.text_input("Name of Team 3", scope.player_3)

	render_start_game_button(scope)


def render_start_game_button(scope):

	st.button(
		label='Start Game',
		key='widget_start_game_button',
		on_click=update_game_status, args=(scope, ),
		type='primary',
		)


def update_game_status(scope):
	# Game Settings
	scope.game_started = True

	scope.show_scoring = True
	scope.show_players = False
	






