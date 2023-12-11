# weatherx

A small cli-based weather app to test poetry packaging. Following https://medium.com/clarityai-engineering/how-to-create-and-distribute-a-minimalist-cli-tool-with-python-poetry-click-and-pipx-c0580af4c026.#

Example: 

```
# Install package locally
>> pipx install git+https://github.com/danielseussler/weatherx.git

# Run 
>> weatherx temperature -n "Berlin, Germany"

# Help
>> weatherx --help
```
