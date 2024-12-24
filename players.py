import streamlit as st





def render_player_config(scope):

	# How many people/teams are playing
	scope.no_of_players = st.pills(
		"Players", ['2 Players', '3 Players', '2 Teams', '3 Teams'], 
		selection_mode="single",
		default = scope.no_of_players
		)
	
	col1, col2, col3 = st.columns(3)

	if scope.no_of_players == '2 Players':
		
		with col1 : scope.player_1 = st.text_input("Name of Player 1", scope.player_1 )
		with col2 : scope.player_2 = st.text_input("Name of Player 1", scope.player_2)
	
	if scope.no_of_players == '3 Players':
		with col1 : scope.player_1 = st.text_input("Name of Player 1", scope.player_1 )
		with col2 : scope.player_2 = st.text_input("Name of Player 2", scope.player_2)
		with col3 : scope.player_3 = st.text_input("Name of Player 3", scope.player_3)
	
	if scope.no_of_players == '2 Teams':
		with col1 : scope.player_1 = st.text_input("Name of Team 1", scope.player_1)
		with col2 : scope.player_2 = st.text_input("Name of Team 2", scope.player_2)

	if scope.no_of_players == '3 Teams':
		with col1 : scope.player_1 = st.text_input("Name of Team 1", scope.player_1)
		with col2 : scope.player_2 = st.text_input("Name of Team 2", scope.player_2)
		with col3 : scope.player_3 = st.text_input("Name of Team 3", scope.player_3)



	if st.button('Start Game'):
		scope.show_scoring = True
		scope.show_players = False




