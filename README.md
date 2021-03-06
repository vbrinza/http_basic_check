# basic-http_check
NOTE: Supported only the 200, 404 and 500 HTTP responses

Prerequisites:
 Python 3

How to run:
1. Clone the repo
```
git clone https://github.com/vbrinza/http_basic_check
```
2. Start a virtual environment
```
python3 -m venv http_basic_check && source http_basic_check/bin/activate && cd http_basic_check
```
3. Start an HTTP server and inject the supported by the check HTTP verbs. It will run in foreground. To continue an other terminal/tab is needed.
```
./basic_http_server.py -verb 200  # to simulate 200
./basic_http_server.py -verb 404  # to simulate 404
./basic_http_server.py -verb 500  # to simulate 500
```
3. Repeat the step 2
4. Install dependencies
```
pip install -r requirements.txt
```
5. Run the script
```
./check_script.py -u http://localhost:9000
```
