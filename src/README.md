# Multi Stage Docker build example
`Dockerfile` contains various stages which are tagged by a name using `as`.

## Commands used
- docker build . -t weather-api:v1
- docker build . -t weather-api:v1 --target=final - Build image using a specific stage
- docker run -p 5000:5000 weather-api:v1 - Run image