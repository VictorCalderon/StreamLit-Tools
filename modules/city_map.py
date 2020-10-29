import streamlit as st
import pandas as pd
import numpy as np


def city_map():

    # Map
    st.write("Generate a map visualization")

    # Load map data
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [18.46, -69.95],
        columns=['lat', 'lon'])

    # Map of the area
    st.map(map_data)

    return 0