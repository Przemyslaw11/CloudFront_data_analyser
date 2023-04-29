# CloudFront_data_analyser
Tool that allows you to analyze your CloudFront logs.

CloudFront_data_analyser is a project that offers a simple yet powerful solution for analyzing access logs to web applications stored in Amazon CloudFront. The tool allows you to easily load your log file or generate synthetic data, and gain insights into your website traffic.

With CloudFront_data_analyser, you can analyze unique IP addresses visiting your website, the number of visits from a single IP address, distribution of traffic between different "edge locations", traffic distribution depending on the country, and more. The tool also features an endpoint frequency threshold analysis, which can help you identify potential security breaches based on the HTTP response code and request method.

To ensure maximum security for your web application, the tool also includes an algorithm that can detect whether a given sequence of requests to endpoints may be a brute force attack.

Overall, CloudFront_data_analyser is an easy-to-use, yet powerful tool that can help you gain insights into your web application's traffic and ensure its security.

# Configuration:

### ⚫STEP 1 
  Clone repository:
  
    $ git clone https://github.com/Przemyslaw11/CloudFront_data_analyser.git
    
### ⚪STEP 2:
  Make venv and install necessary requirements:
  
    $ python3 -m venv myenv
    $ source myenv/bin/activate
    $ pip install -r requirements.txt

### ⚫STEP 3
  Ensure that you are in CloudFront_data_analyser directory and run tests:
  
    $ python -m unittest discover tests
    
### ⚪STEP 4:
  Open 'app.ipynb' jupyter notebook and run all cells.

# Docs
  Documentation for the project is available under the following link: https://przemyslaw11.github.io/CloudFront_data_analyser.github.io/
