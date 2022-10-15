$ pip install requests
Collecting requests
  Using cached https://files.pythonhosted.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl
<-- output omitted for brevity -->
$ python
>>> import requests
>>> requests.get("https://api.github.com")
<Response [200]>

# pip install requests installs a community library from a public package repository.
# python invokes a Python interactive shell.
# import requests imports the library into our Python code.
# requests.get("https://api.github.com") sends an HTTPS request to https://api.github.com and<Response [200]> shows that the request was successful.