import streamlit as st


def vertical_spacer(spaces: int = 1, nrows: int = 1):
    """Separate content vertically
    """
    return [st.text(" " * spaces) for _ in range(nrows)]