from faker import Faker
import pandas as pd
import random
import uuid

fake = Faker()


def generate_x_edge_location() -> str:
    """Generates a random x-edge location code string."""
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.join(random.choices(letters, k=3))
    number = random.randint(1, 10)
    return f"{code}{number}"

def generate_single_log() -> dict:
    """
    Generates a dictionary containing simulated data for a web server log from CloudFront.

    Returns:
        dict: A dictionary containing the following keys:
            - date (str): The date of the log entry in YYYY-MM-DD format.
            - time (str): The time of the log entry in HH:MM:SS format.
            - x_edge_location (str): A randomly generated location code in the format of three uppercase letters
              followed by a number between 1 and 10.
            - sc_bytes (int): The number of bytes in the response sent to the client.
            - c_ip (str): The IP address of the client.
            - cs_method (str): The HTTP request method used by the client (e.g. GET, POST, HEAD).
            - host (str): The hostname of the server.
            - cs_uri_stem (str): The URI stem of the requested resource.
            - sc_status (int): The HTTP status code returned to the client.
            - cs_referer (str): The referer URL of the client.
            - cs_user_agent (str): The user agent string of the client.
            - cs_uri_query (str): The query string of the requested resource.
            - cs_cookie (str): The cookie sent by the client.
            - x_edge_result_type (str): The result type of the request as determined by the CDN (e.g. Hit, Miss, Error).
            - x_edge_request_id (str): A randomly generated UUID that uniquely identifies the request.
            - x_host_header (str): The Host header sent by the client.
            - cs_protocol (str): The protocol used by the client (e.g. HTTP/1.0, HTTP/1.1).
            - cs_bytes (int): The number of bytes in the request sent by the client.
            - time_taken (int): The time taken to process the request, in milliseconds.
            - x_forwarded_for (str): The X-Forwarded-For header sent by the client.
            - ssl_protocol (str): The SSL/TLS protocol version used for the connection.
            - ssl_cipher (str): The SSL/TLS cipher suite used for the connection.
            - x_edge_response_result_type (str): The result type of the response as determined by the CDN (e.g. Hit, Miss, Error).
            - cs_protocol_version (str): The version of the HTTP protocol used by the client.
            - fle_status (str): The status of the field-level encryption for the request (e.g. ForwardedByContentType, MalformedContentTypeClientError).
            - fle_encrypted_fields (str): A dash ("-") indicating that no fields were encrypted.
            - c_port (int): The port number used by the client.
            - time_to_first_byte (float): The time taken to receive the first byte of the response, in seconds.
            - x_edge_detailed_result_type (str): A more detailed result type of the request as determined by the CDN
              (e.g. Error, AbortedOrigin, ClientCommError).
            - sc_content_type (str): The content type of the response sent to the client (e.g. text/html, application/json).
            - sc_content_len (int): The length of the response content, in bytes.
            - sc_range_start (str): A dash ("-") indicating that the response does not contain a byte range.
            - sc_range_end (str): A dash ("-") indicating that the response does not contain a byte range.
            
    """

    timestamp = pd.Timestamp(year=2023, 
                             month=random.randint(1, 12), 
                             day=random.randint(1, 28), 
                             hour=random.randint(0, 23), 
                             minute=random.randint(0, 59), 
                             second=random.randint(0, 59))
    data_dict = {
            'date': timestamp.strftime('%Y-%m-%d'),
            'time': timestamp.strftime('%H:%M:%S'),
            'x_edge_location': generate_x_edge_location(),
            'sc_bytes': random.randint(100, 1000),
            'c_ip': fake.ipv4(),
            'cs_method':  random.choice(['GET', 'POST', 'HEAD']),
            'host': random.choice(["example.com", "test.com", "localhost"]),
            'cs_uri_stem': random.choice(['/endpoint_0', '/endpoint_1', '/endpoint_2', '/endpoint_3']),
            'sc_status': random.choice([200, 404, 403, 502, 301, 500]),
            'cs_referer': random.choice(["-", "http://google.com", "http://example.com"]),
            'cs_user_agent': random.choice(["Mozilla/5.0", "Chrome/94.0.4200.61", "Safari/537.36"]),
            'cs_uri_query': random.choice(["-", "id=123", "page=1"]),
            'cs_cookie': random.choice(["-", "sessionid=abc123", "user=PrzemSpyra"]),
            'x_edge_result_type': random.choice(["Hit", "Miss", "Error"]),
            'x_edge_request_id': str(uuid.uuid4()),
            'x_host_header': random.choice(["example.com", "test.com", "localhost"]),
            'cs_protocol': random.choice(["HTTP/1.0", "HTTP/1.1"]),
            'cs_bytes': random.randint(100, 1000),
            'time_taken': random.randint(100, 1000),
            'x_forwarded_for':  ".".join(str(random.randint(0, 255)) for _ in range(4)),
            'ssl_protocol': random.choice(["TLSv1.2", "TLSv1.3"]),
            'ssl_cipher': random.choice(["ECDHE-RSA-AES128-GCM-SHA256", "AES256-GCM-SHA384"]),
            'x_edge_response_result_type': random.choice(['Hit', 'RefreshHit', 'Miss', 'LimitExceeded', 'CapacityExceeded', 'Error', 'Redirect']),
            'cs_protocol_version': random.choice(['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0', 'HTTP/3.0']),
            'fle_status': random.choice([
                                          'ForwardedByContentType', 'ForwardedByQueryArgs', 'ForwardedDueToNoProfile', 
                                          'MalformedContentTypeClientError', 'MalformedInputClientError', 'MalformedQueryArgsClientError', 
                                          'RejectedByContentType', 'RejectedByQueryArgs', 'ServerError', 'FieldLengthLimitClientError', 
                                          'FieldNumberLimitClientError', 'RequestLengthLimitClientError']),
            'fle_encrypted_fields': '-',
            'c_port': random.randint(1000, 10000),
            'time_to_first_byte': 0.001,
            'x_edge_detailed_result_type': random.choice([
                                                        'Error', 'AbortedOrigin', 'ClientCommError', 'ClientGeoBlocked', 
                                                        'ClientHungUpRequest', 'InvalidRequest', 'InvalidRequestBlocked', 
                                                        'InvalidRequestCertificate', 'InvalidRequestHeader', 'InvalidRequestMethod', 
                                                        'OriginCommError', 'OriginConnectError', 'OriginContentRangeLengthError', 
                                                        'OriginDnsError', 'OriginError', 'OriginHeaderTooBigError', 'OriginInvalidResponseError', 
                                                        'OriginReadError', 'OriginWriteError', 'OriginZeroSizeObjectError', 'SlowReaderOriginError']),
            'sc_content_type': random.choice(['text/html', 'text/css', 'application/json', 'image/jpeg', 'audio/mpeg']),
            'sc_content_len': random.randint(70,100),
            'sc_range_start': '-',
            'sc_range_end': '-'  
        }

    return data_dict

def generate_data(number_of_visits: int = random.randint(100,1000)) -> pd.DataFrame:
    """Generates a pandas DataFrame containing simulated data for a given number of web server log entries."""
    df = pd.DataFrame(generate_single_log() for i in range(number_of_visits))
    return df
