# Global Economy Dashboard

An interactive data dashboard designed to visualize data analysis on billionaires and the economy around the world. The project focuses on categories, demographics, and other relevant metrics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need the following software installed:

- Python 3.x
- pip

Install the required libraries:

```
pip install pandas plotly dash
```

### Installing

A step-by-step series of examples to get your development environment running:

1. **Clone the repository:**

```
git clone https://github.com/yourusername/global-billionaire-dashboard.git
```

2. **Navigate to the project directory:**

```
cd global-billionaire-dashboard
```

3. **Run the application:**

```
python app.py
```

## Running the tests

To run automated tests for this system, follow the instructions below.

### End-to-end tests

These tests ensure the dashboard functions correctly from end to end.

Example: test_dash_app.py
```
import unittest

class TestDashboard(unittest.TestCase):
def test_layout(self):
# Test if the layout is correct
pass

if name == 'main':
unittest.main()
```

### Coding style tests

These tests check the code for PEP 8 compliance.

```
import pep8
import unittest

class TestCodeStyle(unittest.TestCase):
def test_pep8_conformance(self):
style = pep8.StyleGuide(quiet=False)
result = style.check_files(['app.py'])
self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

if name == 'main':
unittest.main()
```

## Deployment

To deploy this project on a live system, you can use services like Heroku, AWS, or any other cloud service that supports Dash applications.

## Built With

* [Dash](https://dash.plotly.com/) - The web framework used
* [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
* [Plotly](https://plotly.com/python/) - Data visualization

## Datasets

This project uses the Billionaires Statistics Dataset 2023 and Global Country Information Dataset 2023 obtained from [Kaggle](https://www.kaggle.com/). The billionaires dataset contains information about billionaires around the world, including their demographics, wealth sources, and other relevant details. The global country dataset contains information regarding the economic indicators, environmental factors, healthcare metrics, and more, for each nation in the world.

### Source
- [Billionaires Statistics Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset)
- [Global Country Information Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023?resource=download)

### Description
The first dataset includes various attributes about billionaires such as name, net worth, age, industry, and country of citizenship. It is used to analyze trends and patterns among the world's wealthiest individuals. The second dataset covers a wide range of indicators and attributes for all 195 countries, and it is used to enable in-depth analyses and cross-country comparisons. 

### Citation and Usage Rights
Please refer to the Billionaire dataset's [Kaggle page](https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset) and the Global Country dataset's [Kaggle page](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023?resource=download) for any citation, usage rights, or license information.

## Authors

* **Manasi Mangalvedhe** - [mnmanasi](https://github.com/mnmanasi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
