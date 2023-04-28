# CloudFront_data_analyser
Tool that allows you to analyze your CloudFront logs.

CloudFront data analyser is a tool that allows for the analysis of access logs to a web application stored in Amazon CloudFront. The project enables loading a file with data or generating synthetic data and then performing various analyses on the log set.

The tool allows for the analysis of unique IP addresses visiting the website, the number of visits from a single IP address, distribution of traffic between different "edge locations", traffic distribution depending on the country, and detecting endpoints that have been visited more than x times based on HTTP code and method.

In addition, the tool offers an algorithm that suggests whether a given sequence of requests to endpoints may be a brute force attack.
