# Implementation Engineer Interview Questions Response.

## SECTION A

### Question One

#### Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one. (10 pts) 

* _REST API Integration._

<p>As an example, we will demonstrate on how Fetching data from a hypothetical REST API can be accomplished. We shall use an API endpoint of (https://jsonplaceholder.typicode.com/todos/1) to get details about a To Do. In this demonstration, we will make use of requests library to query an API Endpoint and get the To Do details. We sha utilize requests library, a python based  module that allows us to send HTTP requests using python. Below is the code that will help us accomplish this. If requests is not already installed onto your system, yiu can run the command below to install it assuming you have pip already installed.</p>
<P>In production ready applications, we may consider using the Django Rest Framework to build API's and authenticate API Endpoints to allocate resources appropriately to customers.</p>

``` 
pip install requests
``` 


__Code__

```Python 
 import requests

# Get the target url
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# Check the url connection status respone
if response.status_code == 200:
    # Extract data in json
    data = response.json()
    # print json data
    print(data)
else:
    # If the page is not fetched, throw an error
    print(f"Error: {response.status_code}")

```
<p>When we execute/run the code, we obtain an output as shown in below.</p>

__Output__

>{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


* _Websockets Integration._

<p>
A communication protocol called WebSocket allows for full-duplex communication channels over a single, persistent connection. Although it is intended for use with web servers and browsers, it can be applied to any application where real-time communication is required. WebSocket is appropriate for applications that need low latency and real-time updates since it allows bi-directional communication between clients and servers. Often in a Django application, we would implement Views and urls to handle requests from the browser then respond asynchronously without having to initiate a page reload. This can be compared with a direct messaging application. When a message is sent, you receive it in realtime. In Django, web sockets can be integrated with the Django Channels to develop a more robust and scalable communictaion/notification channel/protocol. For demonstration purposes, we shall utilize a python library called websocket-client. One may view more about websocket-client from their official github repository https://github.com/websocket-client/websocket-client. To use this package, one must install the libaryy via the command:
</p>


``` 
pip install websocket-client 
``` 
<p>
To connect to the demo echo server at wss://api.gemini.com/v1/marketdata/BTCUSD, we shall use the python script below.
</p>


__Code__

```Python 
# Import necessary libraries
import websocket  # Library for WebSocket communication
import threading  # Library for creating and managing threads
import time       # Library for time-related functions

# Callback function called when a message is received from the server
def on_message(ws, message):
    print(f"Received message: {message}")

# Callback function called when there is an error with the WebSocket connection
def on_error(ws, error):
    print(f"Error: {error}")

# Callback function called when the WebSocket connection is closed
def on_close(ws, close_status_code, close_msg):
    print(f"Closed with status code {close_status_code}: {close_msg}")

# Callback function called when the WebSocket connection is opened
def on_open(ws):
    # Function to be run in a separate thread after the connection is opened
    def run():
        # Send messages to the server at intervals
        for i in range(5):
            time.sleep(1)
            ws.send(f"Hello, Server! Message {i}")

        # Wait for a short period and then close the connection
        time.sleep(1)
        ws.close()

    # Start a new thread to run the 'run' function
    threading.Thread(target=run).start()

# Entry point of the program
if __name__ == "__main__":
    # Enable WebSocket trace for debugging purposes
    websocket.enableTrace(True)

    # Create a WebSocketApp instance with the specified URL and callbacks
    ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Set the on_open callback function
    ws.on_open = on_open

    # Run the WebSocket connection indefinitely
    ws.run_forever()

```

<P>
When the code is executed, we get the responses from the echo server as shown in the Block quote below.
</P>

__Output__

> Received message: {"eventId":1682999884287795,"events":[{"delta":"13.481","price":"37809.12","reason":"place","remaining":"13.481","side":"ask","type":"change"}],"socket_sequence":187,"timestamp":1700855140,"timestampms":1700855140434,"type":"update"}

* _GraphQL Integration._

</p>
GraphQL is a query runtime engine and an open-source data query and manipulation language for APIs. It was created by Facebook in 2012 and launched in 2015. GraphQL is intended to be a more powerful and flexible alternative to REST APIs.

Clients can use GraphQL to describe exactly the data they require from an API, and the server will only deliver that data. In contrast, REST APIs require customers to make several queries to obtain all of the data they require as we demonstrated on the REST API Integration we coded above. GraphQL also has a type system that assures clients can only request data that is available in the API. This reduces errors and makes GraphQL APIs easier to comprehend and use for developers. In this example, we shall use python package called Grephene to build and test our GraphQL API code. To get started, one should have the both grephene and pytests installed on their local environment or systemwide. The command below can be used for installation of these two packages.
</p>

``` 
pip install graphene pytest
``` 
__creating schema__

<p>We will can create a basic GraphQL schema using graphene, and then write tests using pytest.
First thing, we create a chema and store it in a file named schema.py, this ofcourse can be of any name. Then we also create a test file on a separate file.
On a Linux terminal</p>

``` 
touch schema.py

touch test_schema.py
```

The following will be the code for our schema.py and test_schema.py respectively.

*schema.py*
```Python 
# schema.py
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"

schema = graphene.Schema(query=Query)

```

*test_schema.py*
```Python 
# test_schema.py
# test_schema.py
import json
from graphene.test import Client
from schema import schema

def test_hello_query():
    client = Client(schema)

    # Define your GraphQL query
    query = """
    query {
        hello
    }
    """

    # Perform the query
    result = client.execute(query)

    # Check if the response is as expected
    assert result == {"data": {"hello": "Hello World"}}
```

<p>
 To run the test against the schema, we shall run the command below.
</p>

```
pytest test_schema.py
```

We then get an output below.

__Output__

```
================================================================================ test session starts =================================================================================
platform linux -- Python 3.11.2, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/voltageitlabs/Desktop/PreScreening
collected 1 item                                                                                                                                                                     

test_schema.py .                                                                                                                                                               [100%]

================================================================================= 1 passed in 0.10s ==================================================================================

```

### Question Two
<p>Give a walkthrough of how you will manage a data streaming application sending
one million notifications every hour while giving examples of technologies and
configurations you will use to manage load and asynchronous services. (10 pts)</p>

<p>
    A solid architecture is required to properly manage a data streaming application that sends one million notifications per hour.
    I will consider the following configurations and package implementations to keep this application stable.
</p>

* __Message Broker Setup__

<p>
In addition to using Django Channels with Channels-Redis for WebSockets and asynchronous communication, it's crucial to explore advanced features of Redis, such as clustering, to enhance scalability and fault tolerance. By implementing clustering, the message broker can efficiently handle the high volume of notifications, ensuring a resilient and scalable infrastructure. Additionally, I will consider incorporating message compression techniques to optimize payload size, reducing bandwidth usage and improving overall system efficiency. Regularly reviewing and optimizing Redis configurations is essential to fine-tune performance as the application scales. I will also implement robust authentication and authorization mechanisms for the message broker to safeguard against unauthorized access as well as mitigating potential security vulnerabilities. Lastly, I will Set up a comprehensive monitoring and alerting for the message broker to detect issues promptly and maintain continuous availability.
</p> 

* __Notification Processing__

<p>
In extending Django Signals and utilizing Celery tasks for real-time notification processing, it's beneficial to implement task priority settings within Celery. This ensures critical notifications are prioritized for immediate processing, maintaining timely delivery. I will make use of retry policies for Celery tasks to gracefully handle potential failures, preventing the loss of important notifications. I will also Consider incorporating a message queue system, such as RabbitMQ, alongside Celery for improved task distribution and management, however, often, Celery just does well. To enhance performance, introduce logging and monitoring tools to track notification processing times and identify potential bottlenecks. I shall Explore the use of caching mechanisms to store frequently accessed data, reducing the load on the database during notification processing and further optimizing performance.
</P>

* __Database for User Data__

<p>
Beyond using Django ORM with PostgreSQL for managing user data, I will also consider implementing database sharding to horizontally partition data and distribute the load efficiently. This strategy enhances scalability, allowing the system to handle increasing amounts of data seamlessly. Regularly, I will perform database backups and establish a robust disaster recovery plan to ensure data integrity and availability. I will also Implement Django's database connection pooling to optimize database connection handling and enhance overall performance. I will as well Explore database replication options to ensure high availability and fault tolerance. Periodically, I will analyze and optimize both database schema and queries to maintain optimal performance as the dataset grows, ensuring efficient data retrieval.
</p>

* __Load Balancing__

<p>
I will use Gunicorn in conjunction with Nginx to balance load. 
In addition to utilizing Gunicorn with Nginx for load balancing, I will consider configuring auto-scaling to dynamically adjust the number of Gunicorn workers based on traffic patterns. I will Implement Nginx caching mechanisms to cache static content, reducing the load on the Django application server and improving response times. I will also Set up health checks and failover mechanisms to ensure high availability in the event of server failures, enhancing the overall reliability of the system. Regularly, I will monitor and analyze load balancer performance to identify and address potential bottlenecks promptly. This proactive approach ensures the load balancing infrastructure operates optimally under varying traffic conditions.
</p>

* __Security__

<p>
To improve application security, I will use Django's built-in security features, such as middleware and decorators. As one of the steps, I will Enforce SSL/TLS for secure data transmission and user data protection, deactivate debug to False amongst other things.
To augment the security measures mentioned, I will also enforce Two-Factor Authentication (2FA) for user accounts, adding an extra layer of protection against unauthorized access. Staying vigilant on updating Django, Gunicorn, Nginx, and other dependencies regularly to patch any security vulnerabilities promptly shall never be an exclusive strategy. If possible, I will Implement a Web Application Firewall (WAF) to provide an additional layer of defense against common web application attacks. I will also Conduct routine security audits to identify and address potential vulnerabilities, ensuring the system remains resilient against evolving threats. Leverage Django's security middleware to mitigate common security risks such as Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF). This comprehensive security approach significantly strengthens the overall security posture of the data streaming application.
</p>

### Queston Three

<p>
Encryption and hashing are essential techniques in ensuring data security. I have come across few important exncryption Algorithms and their possible implementations. For this, I will write simple Python scripts to demonstrate these encryption Algorithms.
</p>

* __One-Way Hashing__

*Example One - SHA-256 Hashing*

<p>
To demonstrate on this example, I shall use the hashlib python package. Hashlib comes pre installed in Python, however, if by chance it isn't there, we can go ahead and insatall it using the command:
</p>

```
pip install hashlib
```

<p>
The following is the encryption testing code.
</p>

__Code__

```Python
# Import libraries
import hashlib

# Create a hashing function
def sha256_hash(data):
    hashed = hashlib.sha256(data.encode()).hexdigest()
    return hashed

# Example usage
original_data = "Test text 1!"
hashed_data = sha256_hash(original_data)
print(f"Original Data: {original_data}")
print(f"SHA-256 Hash: {hashed_data}")

```
__Output__
<p>
From the code above, we are trying to hash a sentence "Test text 1!", on our output console, we obtain the information below.
</p>

```
Original Data: Test text 1!
SHA-256 Hash: 869297af031fb9520b603295d34f9ede3201565145b60e62af6623f69d9a3564
```
<p>We can see the Hashed value alongisde the original text</p>

*Example Two - MD5-Hashing*
<p>
Our second One way demonstration shall be based on the MD5-Hashing mechanism. Just as the first example, we shall use the hashlib library.
</p>

__Code__
```Python
# Import libraries
import hashlib

# Create a hasching function
def md5_hash(data):
    hashed = hashlib.md5(data.encode()).hexdigest()
    return hashed

# Example usage
original_data = "Test Text 1!"
hashed_data = md5_hash(original_data)
print(f"Original Data: {original_data}")
print(f"MD5 Hash: {hashed_data}")
```

__Output__

```
Original Data: Test Text 1!
MD5 Hash: b9584c9631b248822b01720c7f3e0a92
```

<p>As can be seen, our second hashing algorithm (MD5) is abit weaker than the first algorithm (SHA-256)</p>

* __Two-way Hashing__

<p>For Two way hashing, we can demonstrate on how to encryot a message and decrypt when it gets to its destination. For this eaxmple, we can use a more advanced cryptographic package called cryptography. Cryptography can be installed using a command below</p>

```
pip install cryptography
```

*Example One - AES Encryption*

__Code__

```Python
# Import libraries
from cryptography.fernet import Fernet

# Create an encryption at the info source
def aes_encrypt(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt the info at the destination
def aes_decrypt(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Example usage
original_data = "This is a very confidential information!"
encryption_key = Fernet.generate_key()

encrypted_data = aes_encrypt(original_data, encryption_key)
decrypted_data = aes_decrypt(encrypted_data, encryption_key)

# Compare the encrypted and decrypted text.
print(f"Original Data: {original_data}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data}")

```

__Output__

<p>
The following is the output of the code above when executed.
</p>

```
Original Data: This is a very confidential information!
Encrypted Data: b'gAAAAABlYRovxTUzB378h5v8zBPOrT41XKw5J_5hryWBBh_ElcSI_i-SwKnEuZ9h4SHlK0xEJ6wKF6kcq5WBF3nGxaxaUGl4CymwPTggp0iMHjU5rAvVHlSsSePk4YGtAoyVrdmJHQmF'
Decrypted Data: This is a very confidential information!
```
<p>
We can see that the DEcrypted data is similar to the Encrypted data. The Hash is as well of a very lengthy string making it cambusum to guess or crack
</p>

*Example Two - RSA Encryption*

__Code__

```Python
# Import libraries
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Encrypt data at the source
def rsa_encrypt(data, public_key):
    public_key = serialization.load_pem_public_key(public_key, backend=default_backend())
    encrypted_data = public_key.encrypt(data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return encrypted_data

# Decrypt data at the destination
def rsa_decrypt(encrypted_data, private_key):
    private_key = serialization.load_pem_private_key(private_key, password=None, backend=default_backend())
    decrypted_data = private_key.decrypt(encrypted_data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)).decode()
    return decrypted_data

# Example usage
original_data = "This is a very confidential information!"
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
public_key = private_key.public_key()

encrypted_data = rsa_encrypt(original_data, public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
decrypted_data = rsa_decrypt(encrypted_data, private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))

# Compare the encrypted and Decrypted information
print(f"Original Data: {original_data}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data}")

```

__Output__
<p>
The output of the RSA Algorithm above yields the results below
</p>

```
Original Data: This is a very confidential information!
Encrypted Data: b'\x1d:B"\x92A\xc8A\x02\xf3\x8dP\x82\x9c\x0f\xe5Pa\xdd\x9bL\xef\xd9\x8fT|)\x93\xac\x0b\x9f\xbefU\xd9a\x94/\x9b\xc1\x89\xb7\x0e\xc1\x9b@\x0b\xe0\x1e\xc8c\xc9OH\xf4\xc6\xc4\x00\xe8\x96g\xfd\xb6R\'+\x9d.\xdb3B\xb9\xa3LE1\xafO=E\xa7\xb8?~\xd0\xbcQ\xd4\x10\xd7@5\x1c\x9f\xfdO\x00\\\x1d\xbb\x06s\x06\xfa\x0e\xe7J\x8e\x9f\xe7\xae\xcb\x1b!\x08\xe8\xfc\x90\xaa_\xe6i\xe7\x95|\xf8Z#\x1fZmI+\x9f\xa0\xfc\x12\xec\xa7q\x04\x95\x1b\x11M\x82\xd81\xb2K\x92935#\xf9\xee\x9fy!\x9c\xc9\x0b.*,z\x8fi\xb6D\xe2\xb0I\xaf\x19Y\x8f^\x10VAT\xef\\\xe9\xc8^`\'\x9e\x9a\xcb\x86>\x92J[>\xf1I\xbfT\xfa\xe9L\nl\xa7\xb2\xbd\xcd^\xf4\xbe>u\x14\xb3\xc0\x08\x19o\x9c,\xf4"\x01\xc7\xb2\xf9\x83\xa5b\t\x13\x90x )\x13\xb8T\xaaX\xc3\x00*v\xa3\xd9&`5P\xa9'
Decrypted Data: This is a very confidential information!
```
<p>In summary, the encryption algorithm of the RSA is more reliable in the Two way hashing family, however, the SHA-256 seem to be better in the One-way hashing family.</p>

## SECTION B

### Question One
<p>
Create a login and a success page in Django. A mockup of the created pages
should also be submitted. The mockups should have been created by using
advanced design/wireframe tools thus showcasing prowess in usage of the
tools and use of production server deployments on uwsgi/nginx. Ensure that
the sessions are well and securely managed.(60 pts)
</p>

<p>
The following software and packages was used to design and implement the Login system flow.
</p>

* Django as Backend Technology.
* Django Allauth package to handle authentication flow.
* Tailwind css and HTML for User Interface Design.
* Figma for Designing the UI.
* Gunicorn alongside ngix as proxy server for deplyment hosted on Railway.

<P>
The following are the Design mockups of the system.
</P>

__Landing Page__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/LandingPage.png "Login")

__Login Page__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/Login.png "Login")

__Signup Page__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/Signup.png "Login")

__Success Page__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/Success.png "Login")


__Password Reset Page__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/ResetPassword.png "Login")

__Password Reset Email Sent__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/EmailSent.png "Login")

__Change Password Form__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/ChangePassword.png "Login")


__Password Change Notification__

![Login page](https://guruwritershub-email-static-files.s3.eu-north-1.amazonaws.com/PasswordChangedSuccessfully.png "Login")

<p>
The link to my figma account used for the design is:
</p>

[Figma mockup files design](https://www.figma.com/file/1MIf8e0WGOARuABjPQISmu/InterIntelQuestions?type=design&node-id=0-1&mode=design&t=IVnFXIUIfltpPxfH-0)

<p>
Feel free to check it out
</p>

<p>
Packages installed were Tailwind, Django and Django allauth done using the commands below. We also used whitenoise to compress and serve static files and decouple to serve environmental variables
</p>

> pip install python-decouple

> pip install django

> pip install django-allauth

> python -m pip install django-tailwind 

> pip install whitenoise
> pip install gunicorn

 __Software Functionalities__

The functionalities of this software will be very basic:

* Login
* Signup
* Reset password

A live demo of this project was hosted on Railway using Gunicorn and nginx as the Proxy server. Feel free to test it out. The link is below.

[Live Demo](https://web-production-e0eb.up.railway.app/)

To run the project locally on your machine, follow the steps below:
* git clone 
* Navigate to the project's directory
* pip install -r requirements.txt
* python manage.py runserver
* Access the website via 127.0.0.1:8000 on your browser















