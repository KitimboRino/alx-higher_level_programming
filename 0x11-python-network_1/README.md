0x11. Python - Network #1

### Fetching Internet Resources with urllib:

1. **Fetching a Web Page:**
   ```python
   import urllib.request

   with urllib.request.urlopen('http://example.com/') as response:
       html = response.read()
       # Process the HTML here
   ```

2. **Decoding Response Body:**
   ```python
   import urllib.request

   with urllib.request.urlopen('http://example.com/') as response:
       html = response.read().decode('utf-8')
       # Process the decoded HTML here
   ```

### Using the requests Package:

**Note:** As you mentioned, `requests` is generally simpler and more user-friendly than `urllib`.

1. **Installing requests:** If you haven't already, install the requests package using pip:
   ```
   pip install requests
   ```

2. **Making a GET Request:**
   ```python
   import requests

   response = requests.get('http://example.com/')
   if response.status_code == 200:
       html = response.text
       # Process the HTML here
   ```

3. **Making a POST/PUT/etc. Request:**
   ```python
   import requests

   payload = {'key1': 'value1', 'key2': 'value2'}
   response = requests.post('http://example.com/post', data=payload)
   ```

4. **Fetching JSON Resources:**
   ```python
   import requests

   response = requests.get('http://example.com/data.json')
   if response.status_code == 200:
       data = response.json()
       # Process the JSON data here
   ```

5. **Manipulating Data from an External Service:**
   This depends heavily on the structure of the external service and the data it provides. Once you fetch the data (as shown in previous examples), you can manipulate it using Python's data manipulation libraries like `pandas`, `numpy`, etc., or simply with built-in Python data structures and methods.

These examples give a good starting point for fetching and manipulating data from external services using Python.
