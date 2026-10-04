# ML_Salary_Prediction
## Project Overview
This project builds a complete Machine Learning workflow using the Salary Dataset. The goal is to predict salary from years of professional experience and expose the trained model through an interactive Streamlit application.

## Dataset
Source: https://raw.githubusercontent.com/SagarChhabriya/data-science/refs/heads/main/datasets/TBD/salary_dataset.csv

Columns:
- `Experience Years` — input feature
- `Salary` — prediction target

## Workflow
1. Load the dataset
2. Explore the data
3. Check and clean missing/duplicate records
4. Split data into training and testing sets
5. Train Linear Regression
6. Evaluate using MAE, MSE, RMSE and R²
7. Serialize the model with Joblib
8. Build an interactive Streamlit UI
9. Deploy through Streamlit Community Cloud

## Run Locally

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Train and save the model:
```bash
python train_model.py
```

Run Streamlit:
```bash
streamlit run app.py
```

## Project Structure

```text
Salary_ML_Project/
│
├── data/
├── model/
│   └── salary_model.pkl
├── notebooks/
│   └── model_training.ipynb
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Model
**Linear Regression**

The model predicts salary using `Experience Years`.

## Evaluation Metrics
The training script prints:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## GitHub
After creating your GitHub repository:

```bash
git init
git add .
git commit -m "Initial salary prediction project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Do not upload `venv/` to GitHub.

## Streamlit Deployment
1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Deploy.
6. Submit the public application URL.

## Assignment Deliverables
- GitHub Repository Link
- Streamlit App Link
- Dataset Source
- Project Description
- Model Used
- Evaluation Metrics
- Screenshot of deployed application
