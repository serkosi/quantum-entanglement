# Quantum Entanglement

[NTangled Dataset](https://github.com/LSchatzki/NTangled_Datasets) is introduced to support quantum machine learning, this dataset consists of quantum states with varying degrees and types of multipartite entanglement. It serves as a benchmark for supervised learning classification tasks in quantum systems.

The repository includes trained weights for three different ansatzes:​
- Hardware Efficient Ansatz
- Strongly Entangling Ansatz
- Convolutional Ansatz

These are provided across various numbers of qubits, depths, and target values of entanglement. The data is available in both Numpy (.npy) and text (.txt) formats.

The dataset contains numerical data (e.g., entanglement measures, circuit parameters) that can be treated as features. These features can be directly fed into classical ML algorithms for tasks like classification, regression, or clustering.

By applying classical ML, we can uncover patterns, perform dimensionality reduction, or even predict physical properties that relate to the underlying physics phenomena.

## Approach for a Classical ML Project

1. Data Preprocessing:
    - Load the dataset using NumPy or Pandas.
    - Normalize or standardize features.
    - Perform exploratory data analysis (EDA) to understand correlations and distributions.

2. Feature Engineering:
    - Extract meaningful features from the raw quantum state data.
    - Consider techniques like principal component analysis (PCA) to reduce dimensionality.

3. Model Selection:
    - Start with classical methods such as logistic regression, decision trees, or support vector machines.
    - Evaluate models using cross-validation and standard metrics (accuracy, precision, recall).

4. Visualization and Interpretation:
    - Plot feature distributions, decision boundaries, or PCA projections to gain insights.
    - Compare results across different ansatzes or parameter settings.

