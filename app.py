from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


def process_table():
    # Load the CSV file
    df = pd.read_csv("Table_Input.csv")

    # Extract values for calculations
    alpha = df.iloc[4, 1] + df.iloc[19, 1]  # A5 + A20
    beta = df.iloc[14, 1] / df.iloc[6, 1]  # A15 / A7
    charlie = df.iloc[12, 1] * df.iloc[11, 1]  # A13 * A12

    # Create Table 2
    table_2 = pd.DataFrame({
        "Category": ["Alpha", "Beta", "Charlie"],
        "Value": [alpha, beta, charlie]
    })
    return df, table_2


@app.route('/')
def index():
    table_1, table_2 = process_table()
    return render_template('index.html', table_1=table_1.to_html(index=False), table_2=table_2.to_html(index=False))


if __name__ == '__main__':
    app.run(debug=True)
