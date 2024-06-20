import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

# Function to generate the graph
def generate_graph():
    G = nx.Graph()

    # Add nodes
    G.add_node(1, label="Node 1")
    G.add_node(2, label="Node 2")
    G.add_node(3, label="Node 3")
    G.add_node(4, label="Node 4")

    # Add edges
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)

    return G

# Function to draw the graph using Pyvis
def draw_graph(G):
    net = Network(notebook=True)
    net.from_nx(G)
    net.show("graph.html")

# Streamlit app
st.title("Interactive Node Graph")

# Generate and draw graph
G = generate_graph()
draw_graph(G)

# Load and render the graph in Streamlit
HtmlFile = open("graph.html", "r", encoding="utf-8")
source_code = HtmlFile.read()
components.html(source_code, height=600, scrolling=True)
