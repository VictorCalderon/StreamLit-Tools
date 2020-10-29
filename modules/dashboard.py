import streamlit as st
import seaborn as sns
import altair as alt


def dashboard():

    # Data Table title
    st.write("Iris dataset loaded from Seaborn")

    # Generate dataset
    data = sns.load_dataset('iris')

    # Rename columns
    data.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']

    # Columns
    col1, col2 = st.beta_columns([1, 3])

    with col1:

        # Rows to display
        rows = st.text_input(label='Number of rows to display', value="10", key='input-text-nrows')

    try:
        # Get rows
        nrows = int(rows)
        st.table(data.sample(nrows, random_state=42))

    except:
        raise('Number of rows must be an integer')

    # Declare columns
    col1, col2 = st.beta_columns([3, 4])

    with col1:

        # Scatter plot
        st.write("Iris dataset scatter plot")

        # Get unique species
        species_list = ['all'] + list(data['Species'].unique())

        # Select species to isolate
        species = st.selectbox(
            'Which species would you like to check first?', 
            species_list
        )

    # Is cleared button
    is_cleared = st.button('Clear Selection', 'clear-selection-button')

    # Change clear string to ''
    if is_cleared or species == 'all':
        species = ''

    # Filter table
    filtered_data = data[data['Species'].str.contains(species)]

    # Scatterplot by feature
    scatter_iris = alt.Chart(filtered_data).mark_circle()

    # Configure plot
    scatter_iris = scatter_iris.encode(
        alt.X('Petal Width'), 
        alt.Y('Petal Length'),
        alt.Color('Species', legend=alt.Legend(orient="bottom"))
        )

    # Move legend
    alt.Legend(direction='vertical')

    # Plot data
    st.altair_chart(scatter_iris, use_container_width=True)

    return 0