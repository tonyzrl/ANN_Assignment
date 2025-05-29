# Predicting Task–Employee Mapping Penalties with a From-Scratch ANN

A self-contained implementation of a feed-forward artificial neural network (ANN) built from first principles in NumPy, designed to predict the penalty score of assigning 10 tasks to 5 employees.

## Repository Structure
├── data/

│ ├── task_assignment_data.csv ← 100 generated task→employee mappings + penalties

│ └── GenerateData.py ← Python script for generating the dataset 

├── results/

│ ├── modelA_Epoch_vs_Loss.png ← Model A: training & validation loss vs. epoch

│ ├── modelA_LR_vs_TestLoss.png ← Model A: test loss vs. learning rate

│ ├── modelA_AF_vs_Loss.png ← Model A: train & val loss for ReLU vs. Sigmoid

│ ├── modelA_BS_vs_EpochTime.png ← Model A: epoch time vs. batch size

│ ├── modelB_Epoch_vs_Loss.png ← Model B: training & validation loss vs. epoch

│ ├── modelB_LR_vs_TestLoss.png ← Model B: test loss vs. learning rate

│ ├── modelB_AF_vs_Loss.png ← Model B: train & val loss for ReLU vs. Sigmoid

│ └── modelB_BS_vs_EpochTime.png ← Model B: epoch time vs. batch size

└── ANN_Notebook.ipynb ← Google Colab notebook: data prep, model code, training & plots


Data directory contains the input assignment mapping data and the Python program used to generate the input mapping. Results directory contains all the comparison plots from running the notebook in Google Colab.
The implementation of the neural network is done within the ANN_Notebook.ipynb Python notebook.

## Quick Start
Open in Google Colab:
https://colab.research.google.com/github/tonyzrl/ANN_Assignment/blob/main/ANN_Notebook.ipynb 

(Optional) Local install (If not already installed):
pip install numpy pandas matplotlib

Run through ANN_Notebook.ipynb, if in Colab: select Runtime → Run all.
