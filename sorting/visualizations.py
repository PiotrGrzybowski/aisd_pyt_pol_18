import json
import plotly.graph_objects as go

from sorting.research import ORDERED, REVERSED, RANDOM


def show_algorithm_complexities(filename):
    with open(filename) as f:
        result = json.load(f)

    domain = result[ORDERED].keys()

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[ORDERED].values()), mode='lines+markers', name=ORDERED))
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[REVERSED].values()), mode='lines+markers', name=REVERSED))
    figure.add_trace(go.Scatter(x=list(domain), y=list(result[RANDOM].values()), mode='lines+markers', name=RANDOM))
    figure.show()


def show_complexities(filenames, order_type):
    figure = go.Figure()
    for filename in filenames:
        with open(filename) as f:
            result = json.load(f)

        domain = result[ORDERED].keys()
        figure.add_trace(go.Scatter(x=list(domain), y=list(result[order_type].values()), mode='lines+markers',
                                    name=f"{filename.split('_')[0]}_{order_type}"))

    figure.show()


def show_complexities_types(filenames, types):
    figure = go.Figure()
    for filename in filenames:
        for order_type in types:
            with open(filename) as f:
                result = json.load(f)

            domain = result[ORDERED].keys()
            figure.add_trace(go.Scatter(x=list(domain), y=list(result[order_type].values()), mode='lines+markers',
                                        name=f"{filename.split('_')[0]}_{order_type}"))

    figure.update_layout({
        'font_size': 18
    })
    figure.show()


if __name__ == '__main__':
    filenames = [
        'BubbleSortSmart_200.json',
        # 'BubbleSort_200.json',
        # 'InsertionSort_200.json',
        'InsertionSort_1000.json',
        'QuickSort_3000.json'
    ]
    show_complexities_types(filenames, [ORDERED, REVERSED, RANDOM])
