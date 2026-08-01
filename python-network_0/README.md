# python-network_0

Higher-level programming project on HTTP, cURL, and Bash scripting.

## Tasks

| File | Description |
| --- | --- |
| `0-body_size.sh` | Displays the size in bytes of a response body |
| `1-body.sh` | Displays the body of a GET response, only for status 200 |
| `2-delete.sh` | Sends a DELETE request and displays the response body |
| `3-methods.sh` | Displays all HTTP methods a server accepts for a URL |
| `4-header.sh` | Sends a GET request with a custom header |
| `5-post_params.sh` | Sends a POST request with `email` and `subject` params |

## Requirements

- Ubuntu 20.04 LTS
- Every Bash script is exactly 3 lines (shebang, comment, command)
- Every `curl` call uses `-s` (silent mode)

Every script in this project was run against a local Flask test
server replicating the routes and behavior described in the task
examples, and verified to match the expected output exactly.
