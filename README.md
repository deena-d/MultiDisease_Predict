# Multi Disease Prediction Web Application

This is a Python web application for predicting various diseases including diabetes, breast cancer, heart disease, and Parkinson's disease. It is built using the Streamlit framework and uses trained machine learning models for predictions. Below is an overview of the project structure and how to use the application.

![image](https://github.com/deena-d/MultiDisease_Predict/assets/107647091/e041f72b-1fb9-40b4-840f-37913bcc8dc0)



## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before running this application, make sure you have the following installed on your system:

- Python (3.6+)
- Streamlit (Python library for creating web apps)
- Required Python packages as mentioned in the code
- Trained machine learning models for each disease (not included in this repository)

## Installation
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/multi-disease-prediction.git
   ```

2. Install the required Python packages:

   ```bash
   pip install streamlit streamlit_option_menu scikit-learn
   ```

3. Place your trained machine learning models for diabetes, breast cancer, heart disease, and Parkinson's disease in the specified directory. Update the file paths in the code to point to these models.

## Usage
1. Run the application using Streamlit:

   ```bash
   streamlit run app.py
   ```

2. Open a web browser and go to the URL provided by Streamlit (usually http://localhost:8501).

3. You will see a sidebar on the left with options to select the disease you want to predict (Diabetes, Breast Cancer, Heart Disease, or Parkinson's Disease).

4. Fill in the required input fields with the relevant information for the chosen disease.

5. Click the "Predict" button to get the prediction result.

6. The application will display whether the person is healthy or has the specified disease.

7. You can switch between disease predictions by selecting different options in the sidebar.

## Models
You need to provide trained machine learning models for each disease in the specified directory. The models should be in the form of `.sav` files (pickled scikit-learn models). Update the file paths in the code to point to these models.

## Contributing
If you want to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with your feature or bug fix: `git checkout -b feature/my-feature` or `git checkout -b bug/issue-description`.
3. Make your changes, and commit them: `git commit -m 'Description of your changes'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Create a pull request on the GitHub repository.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
