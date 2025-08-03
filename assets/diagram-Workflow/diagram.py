from diagrams import Diagram, Cluster
from diagrams.custom import Custom

with Diagram("Fraud Detection Workflow", show=True):

    with Cluster("Data Ingestion"):
        data = Custom("Raw Data", "./icons/csv.png")

    with Cluster("Data Engineering"):
        preprocess = Custom("Preprocessing", "./icons/gear.png")
        smote = Custom("SMOTE", "./icons/balance.png")

    with Cluster("Modeling"):
        train = Custom("Model Training", "./icons/brain.png")

    with Cluster("Evaluation"):
        eval = Custom("Evaluation", "./icons/chart.png")

    data >> preprocess >> smote >> train >> eval
