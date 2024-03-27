0x10. Python - Network #0

1. **What a URL is:**
   - A URL (Uniform Resource Locator) is a reference to a web resource that specifies its location on a computer network and the mechanism for retrieving it. It typically consists of a protocol identifier (such as "http://" or "https://"), followed by the domain name or IP address, and optional additional components like path and query parameters.

2. **What HTTP is:**
   - HTTP (Hypertext Transfer Protocol) is a protocol used for transmitting hypermedia documents, such as HTML. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

3. **How to read a URL:**
   - A URL can be read from left to right. For example:
     ```
     https://www.example.com:8080/path/to/resource?param1=value1&param2=value2
     ```
     - Scheme: https
     - Domain: www.example.com
     - Port: 8080
     - Path: /path/to/resource
     - Query string: param1=value1&param2=value2

4. **The scheme for an HTTP URL:**
   - The scheme for an HTTP URL typically starts with either "http://" for unsecured connections or "https://" for secured connections.

5. **What a domain name is:**
   - A domain name is a human-readable label that corresponds to a unique IP address on the internet. It's used to identify websites and other resources.

6. **What a sub-domain is:**
   - A sub-domain is a domain that is part of a larger domain. For example, in "subdomain.example.com", "subdomain" is the sub-domain of "example.com".

7. **How to define a port number in a URL:**
   - A port number can be defined in a URL by appending ":" followed by the port number after the domain name or IP address. For example: "http://example.com:8080".

8. **What a query string is:**
   - A query string is a part of a URL that contains data to be passed to the web server as key-value pairs. It begins with a question mark (?) and includes parameters separated by ampersands (&), such as "?param1=value1&param2=value2".

9. **What an HTTP request is:**
   - An HTTP request is a message sent by a client (such as a web browser) to a server, requesting a resource such as a web page.

10. **What an HTTP response is:**
    - An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains the requested resource along with status information.

11. **What HTTP headers are:**
    - HTTP headers are additional pieces of information sent along with an HTTP request or response. They provide metadata about the message, such as content type, caching directives, and authentication tokens.

12. **What the HTTP message body is:**
    - The HTTP message body is the data transmitted after the headers in an HTTP request or response. It contains the content of the requested resource (in the case of a response) or data to be sent to the server (in the case of a request).

13. **What an HTTP request method is:**
    - An HTTP request method is a command used by a client to specify the desired action to be performed on a resource. Common methods include GET (retrieve), POST (submit data), PUT (update), DELETE (remove), etc.

14. **What an HTTP response status code is:**
    - An HTTP response status code is a three-digit number sent by a server to indicate the success, failure, or other status of an HTTP request. Examples include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).

15. **What an HTTP Cookie is:**
    - An HTTP Cookie is a small piece of data sent from a website and stored on the user's computer by the user's web browser. Cookies are commonly used for session management, user tracking, and personalization.

16. **How to make a request with cURL:**
    - To make a request with cURL (a command-line tool for transferring data with URLs), you can use the following syntax:
      ```
      curl [options] [URL]
      ```
      For example:
      ```
      curl https://www.example.com
      ```

17. **What happens when you type google.com in your browser (Application level):**
    - When you type "google.com" in your browser and press Enter, the browser sends an HTTP request to the domain "google.com" asking for the default webpage. Google's servers receive this request, process it, and then send back an HTTP response containing the HTML, CSS, and JavaScript code needed to render the Google homepage. The browser then interprets this code and displays the Google homepage to the user. Additionally, various other processes might occur in the background, such as DNS resolution to translate the domain name into an IP address and establishing a secure HTTPS connection if supported.
