import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_path = os.path.join(BASE_DIR, 'static')

def get_graphs():
    graphs = []
    for file in os.listdir(static_path+"/graphs"):
        if file.endswith(".png"):
            graphs.append(file)
    return graphs