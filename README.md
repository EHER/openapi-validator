# openapi-validator
A microservice to validate [OpenAPI Specification](https://openapis.org).

## Building
```
docker build -t eher/openapi-validator .
```

## Running
```
docker run -it --rm -v 5000:5000 eher/openapi-validator
```

## Validating
```
curl --data @spec.json localhost:5000
```
or to use http status
```
curl --silent --write-out "%{http_code}" --output /dev/null --data @spec.json localhost:5000
```
