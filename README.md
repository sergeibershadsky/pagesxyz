# PagesXYZ


## Installation

```bash
./manage.py migrate
./manage.py createsuperuser
```

## Usage

Run developer server
```bash
./manage.py runserver
```

Obtain auth token
```
http http://localhost:8000/api-token-auth/ username=username password=password
```

Examples
```bash
# get root element
http http://localhost:8000/tree/1/ "Authorization: Token f2a57ad8d5765f6c4aa5bed76842dc1d983c057f"

# create child to root
http http://localhost:8000/tree/ "Authorization: Token f2a57ad8d5765f6c4aa5bed76842dc1d983c057f" parent=1 name="Second page"
```

Swagger docs http://localhost:8000/api/schema/swagger-ui/
