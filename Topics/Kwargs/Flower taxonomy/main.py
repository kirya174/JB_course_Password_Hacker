iris = {}


def add_iris(id_n, species, petal_length, petal_width, **add_features):
    iris[id_n] = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    for key in add_features:
        iris[id_n][key] = add_features[key]