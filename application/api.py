"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv('https://raw.githubusercontent.com/caschern/Sound-Vibe/main/DATA/music_data.csv')
    return df