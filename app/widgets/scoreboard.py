import streamlit as st


def render_scoreboard_heading(scope):
	# construct the heading
	# st.write('Scoring')
	title_string = 'Scores > '

	if scope.players_qty == 2:
		title_string = str(scope.player_1) + ' v ' + str(scope.player_2)

	if scope.players_qty == 3:
		title_string = str(scope.player_1) + ' v ' + str(scope.player_2)+ ' vs ' + str(scope.player_3)

	st.header(title_string)
	st.divider()


def render_scoreboard(scope):

	position_1 = str(scope.player_1) + ' = ' + str(scope.score_total_player_1)
	position_2 = str(scope.player_2) + ' = ' + str(scope.score_total_player_2)
	position_3 = str(scope.player_3) + ' = ' + str(scope.score_total_player_3)

	st.write(position_1)
	st.write(position_2)

	if scope.players_qty == 3:
		st.write(position_3)