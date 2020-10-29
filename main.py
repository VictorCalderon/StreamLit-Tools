# Import modules and helpers
import streamlit as st
from modules import dashboard, city_map, settings
from helpers import vertical_spacer

# Tabs
CURRENT_TAB = 1

# Add title
st.header('StreamLit Demo')

# Columns for tabs
col1, col2, col3, _ = st.beta_columns([1, 1, 1, 3])

with col1:
    if st.button('Dashboard'):
        CURRENT_TAB = 1

with col2:
    if st.button('City Maps'):
        CURRENT_TAB = 2
    
with col3:
    if st.button('Settings'):
        CURRENT_TAB = 3


# Separation
vertical_spacer(nrows=2)

if CURRENT_TAB == 1:

    # Run dashboard
    dashboard()

# Conditional map
if CURRENT_TAB == 2:

    # Run city map
    city_map()

# Settings
if CURRENT_TAB == 3:

    # Run settings
    settings()