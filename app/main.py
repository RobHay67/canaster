## pipenv shell
## streamlit run streamlit_app.py


# -------------------------------------------------------
# 	uv run streamlit run app/main.py
# 	source .venv/bin/activate
# -------------------------------------------------------





import streamlit as st

from scope import scope_init
from sidebar import render_sidebar
from players.players import render_player_config
from scores.controller import render_scoring


if 'initialised' not in st.session_state:
	scope = scope_init(st.session_state)
else:
	scope = st.session_state

render_sidebar(scope)

if scope.show_players is True: 
	render_player_config(scope)

if scope.show_scoring is True:
	render_scoring(scope)



# print('='*66)
# print('Total Keys in Scope = ', len(scope))
# st.divider()
# for count, key in enumerate(sorted(st.session_state)):
# 	print(count+1, key, st.session_state[key])
# 	st.write(count+1, key, st.session_state[key])
# print('='*66)




