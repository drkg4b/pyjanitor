import pandas as pd
import pytest
from pyspark.sql import SparkSession
from sklearn.datasets import load_iris

import janitor.spark


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.getOrCreate()
    yield spark
    spark.stop()


@pytest.fixture(scope="module")
def df(spark):
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    return spark.createDataFrame(df)


@pytest.mark.functions
def test_clean_names(df):
    df = df.clean_names()
    expected_columns = [
        "sepal_length_cm",
        "petal_width_cm",
        "sepal_width_cm",
        "petal_length_cm",
    ]
    assert set(df.columns) == set(expected_columns)
