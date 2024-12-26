import streamlit as st


def render_sidebar(scope):
	with st.sidebar:
		st.header("Canaster Scorer")

		render_show_players_button(scope)
		end_round = st.button("End Round", key="widget_end_round")
		new_game = st.button("New Game", key="widget_new_game")
		house_rules = st.button("House Rules", key="widget_house_rules")




		if scope.game_started == True:
			render_scoreboard_heading(scope)
			render_scoreboard(scope)



def render_scoreboard(scope):

	position_1 = str(scope.player_1) + ' = ' + str(scope.score_total_player_1)
	position_2 = str(scope.player_2) + ' = ' + str(scope.score_total_player_2)
	position_3 = str(scope.player_3) + ' = ' + str(scope.score_total_player_3)

	st.write(position_1)
	st.write(position_2)

	if scope.players_qty == 3:
		st.write(position_3)
	



def render_scoreboard_heading(scope):
	# construct the heading
	st.write('Scoring')
	title_string = ''

	if scope.players_qty == 2:
		title_string = str(scope.player_1) + ' vs ' + str(scope.player_2)

	if scope.players_qty == 3:
		title_string = str(scope.player_1) + ' vs ' + str(scope.player_2)+ ' vs ' + str(scope.player_3)

	st.subheader(title_string)





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

