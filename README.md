# Stock-Price-Forecasting-using-Financial-and-Twitter-Data

## Overview

This project is designed to integrate **stock market data analysis**, **sentiment analysis of tweets**, and **forecasting of stock prices** using traditional statistical models like **ARIMA** and advanced machine learning models such as **GRU (Gated Recurrent Units)**. 
The system sources data from **MySQL** (for historical stock prices), **MongoDB** (for storing tweets related to stock tickers), and **Twitter** (for real-time sentiment analysis). 
The overall goal is to predict future stock prices while analyzing public sentiment towards different stocks based on Twitter data


## Prerequisites

To run the project, you'll need the following installed:

- **Python 3.x**
- **MySQL** (for stock price data)
- **MongoDB** (for tweet data storage)
- **Kafka** (for real-time streaming)
- **Jupyter Notebook** (for data analysis)
- **Required Python Libraries** (listed in `requirements.txt`)

## Features

- **Data Integration**:

    - Stock market data fetched from **MySQL** for historical prices.
    - Tweet data fetched and stored in **MongoDB** for analysis.
  <img width="1000" alt="Image" src="https://github.com/user-attachments/assets/e72b6041-51b3-49ef-9e06-645c87dcb835" />
- **Exploratory Data Analysis (EDA)**
  - **Missing Dates Identification**: We identified weekends and market closures where there were no stock data entries, which was achieved using date-related functions in pandas. This helped us understand the periods of inactivity in the stock market.
  
- **Volatility Analysis**: A key analysis performed during the COVID-19 pandemic was the volatility of stock prices. A 5-day rolling window was used to calculate volatility and visualize stock price fluctuations during the pandemic, especially during March 2020.

- **Insights**: Significant price volatility was observed during the March 2020 period, driven by the pandemic's market impact.

<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/08fa02d7-b057-407d-8b25-7ec19a162399" />
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/d1fb0b9b-896d-48e4-ae15-583aa7893875" />
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/27a15222-1699-4951-bad3-6cbc95f8d463" />
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/b8b80cac-6554-4831-a887-756c98603dca" />
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/53bbcb18-4e89-4916-b8c5-22266a6c60ea" />

- **Sentiment Analysis**: 
    - **VADER** and **HuggingFace** are used for sentiment analysis of tweets.

- **Stock Price Forecasting**: 
    - **ARIMA** and **GRU** models are applied for forecasting future stock prices based on historical data.

- **Performance Benchmarking**: 
    - **YCSB** is used to benchmark and compare the performance of **MySQL** and **MongoDB** in terms of throughput and latency.

- **Real-Time Streaming with Kafka**: 
    - Stream tweet data to analyze real-time sentiment and correlate it with stock price trends.

- **Interactive Dashboard**: 
    - **Dash** is used for creating an interactive dashboard where users can view stock price forecasts and sentiment trends.
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/f2f13865-68ba-40e9-9d4a-e425795f8741" />
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/b21d9a90-41d7-4706-a15f-281165417a51" />
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/0cc38f31-2194-4bd3-9e6c-37dd138102a2" />


## Installation

Follow these steps to get the project up and running:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tashi-2004/Stock-Price-Forecasting-using-Financial-and-Twitter-Data.git
   cd Stock-Price-Forecasting-using-Financial-and-Twitter-Data

# Setup Instructions

## Install Dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```
## Set Up MySQL

1. Create a database `stockdb` in MySQL.
2. Import the historical stock prices into the `stockdb` database.
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/e705884e-e3e8-4f4c-91e5-38c46303dff3" />

## Set Up MongoDB

1. Import tweet data into MongoDB's `stockdb` database.
<img width="1000" alt="Image" src="https://github.com/user-attachments/assets/6acddba3-ca0a-4ded-92ab-bd3f12a63af1" />

## Set Up Kafka

1. Configure Kafka for real-time streaming.
2. Ensure that your Kafka server, producer, and consumer are running properly.

<img width="1000" src="https://github.com/user-attachments/assets/bf4c049e-2008-42ad-ab5f-91f6bb665433" alt="Image">
<img width="1000" src="https://github.com/user-attachments/assets/fe6f94b3-71a5-4685-8c9d-30b127432d9a" alt="Image">

## Forecasting Models

The **ARIMA** and **GRU** models are used for stock price forecasting. The output of these models is used for predictions of 1-day, 3-day, and 7-day stock prices.

## Dashboard

An interactive **Dash** dashboard allows users to visualize stock price trends, sentiment trends, and model performance.

## Model Evaluation

### Metrics Used:
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**

### Key Insights:
- **ARIMA** performs better for stable stock price predictions.
- **GRU** performs better for volatile stock price predictions.

## Run YCSB Benchmarking

1. Use the provided `ycsb_benchmark.sh` file to run benchmarking on MySQL and MongoDB.

```bash
./ycsb.sh
```
<img width="1000" src="https://github.com/user-attachments/assets/32f45e6e-0517-46bf-91a9-601314c43823" alt="Image">
<img width="1000" src="https://github.com/user-attachments/assets/ea517688-e84d-40c5-bd17-b426aaefae19" alt="Image">
<img width="1000" src="https://github.com/user-attachments/assets/d38100e5-4954-4818-9df6-feeef3d09175" alt="Image">

## Kafka Producer & Consumer
Kafka will stream tweet data in real-time to analyze sentiment and correlate it with stock price movements.
<img width="1000" src="https://github.com/user-attachments/assets/cf1a4c16-cf19-4548-8361-21044b184bb5" alt="Image">
<img width="1000" src="https://github.com/user-attachments/assets/198e4735-2fbd-4a9c-bc64-f27832558b58" alt="Image">

## Contribution

We welcome contributions to this repository. Please feel free to fork the repository and submit issues or pull requests. Any improvements or optimizations are greatly appreciated.

## Contact

For queries or contributions, please contact:
**Tashfeen Abbasi**  
Email: abbasitashfeen7@gmail.com
