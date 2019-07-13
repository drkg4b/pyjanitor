import pandas as pd
import pytest


@pytest.mark.functions
def test_expand_column():
    data = {
        "col1": ["A, B", "B, C, D", "E, F", "A, E, F"],
        "col2": [1, 2, 3, 4],
    }

    df = pd.DataFrame(data)
    expanded_df = df.expand_column(column_name="col1", sep=", ", concat=False)
    assert expanded_df.shape[1] == 6


@pytest.mark.functions
def test_expand_and_concat():
    data = {
        "col1": ["A, B", "B, C, D", "E, F", "A, E, F"],
        "col2": [1, 2, 3, 4],
    }

    df = pd.DataFrame(data).expand_column(
        column_name="col1", sep=", ", concat=True
    )
    assert df.shape[1] == 8

@pytest.mark.functions
def test_expand_dropfirst():
    data = {
        "col1": ["A, B", "B, C, D", "E, F", "A, E, F"],
        "col2": [1, 2, 3, 4],
    }

    df = pd.DataFrame(data).expand_column(
        column_name="col1", sep=", ", concat=False, drop_first=True
    )
    assert df.shape[1] == 5
    assert 'A' not in df.columns

@pytest.mark.functions
def test_expand_concat_dropfirst():
    data = {
        "col1": ["A, B", "B, C, D", "E, F", "A, E, F"],
        "col2": [1, 2, 3, 4],
    }

    df = pd.DataFrame(data).expand_column(
        column_name="col1", sep=", ", concat=True, drop_first=True
    )
    assert df.shape[1] == 7
    assert 'A' not in df.columns
