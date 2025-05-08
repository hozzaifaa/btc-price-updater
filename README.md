# Bitcoin Price Tracker - Auto-Update Kaggle Dataset

This project automatically tracks Bitcoin prices using the CoinGecko API and updates a dataset on Kaggle every day. The dataset is available for public access and contains a time series of Bitcoin prices over time.

## Features
- Fetches Bitcoin price from the CoinGecko API
- Automatically appends new data to a CSV file (`btc_prices.csv`)
- Updates Kaggle dataset daily using GitHub Actions
- Includes metadata and version control for Kaggle dataset

## How It Works
1. The script fetches the latest Bitcoin price from the CoinGecko API.
2. It appends the timestamp and price to the `btc_prices.csv` file.
3. The `update_dataset.py` script is triggered via GitHub Actions to update the Kaggle dataset.

## Setup

### Prerequisites
1. **Kaggle account**: You must have a Kaggle account. Create an API token from [Kaggle API settings](https://www.kaggle.com/account).
2. **GitHub account**: You need a GitHub repository to use GitHub Actions.

### Installing the Project Locally
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/btc-price-updater.git
    cd btc-price-updater
    ```

2. Create a virtual environment:
    ```bash
    python -m venv kaggle
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      .\kaggle\Scripts\activate
      ```
    - On Linux/macOS:
      ```bash
      source kaggle/bin/activate
      ```

4. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Set Kaggle credentials as environment variables or place the `kaggle.json` file in the `.kaggle` folder:
    - **Windows**: Place `kaggle.json` in `C:\Users\yourusername\.kaggle\`
    - **Linux/macOS**: Place `kaggle.json` in `~/.kaggle/`

6. Create the Kaggle dataset manually (once) using the command:
    ```bash
    kaggle datasets create -p dataset
    ```

### GitHub Actions
This project includes a GitHub Actions workflow to automate dataset updates:
- The workflow will run daily at 12:00 UTC to fetch new Bitcoin prices and update the Kaggle dataset.

### Contributing
Feel free to fork the repository, create pull requests, and contribute to the project.

## License
This project is licensed under the MIT License.
