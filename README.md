## Requirements

This application use a docker then if you don't have a docker desktop installed, you need a install this. For install follow this link and download it: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Running local server

Once you have docker installed you have to follow the next steps:

1. Clone repository -> `git clone https://github.com/Coria97/technical-evaluation-stormtech.git`
2. Into to repository -> `cd .\technical-evaluation-stormtech\`
3. Open docker desktop application
4. Run this command -> `docker compose up -d --build`

## Endpoint

### GET /api/v1/tracking/<tracking_number>

**Description:** this service return the package info and their sheet_number

#### Example response 200 OK:
~~~
{
    "tracking": 18,
    "weight": 500000.0,
    "height": 1997.0,
    "status": 1,
    "package_type": "S",
    "client": {
        "name": "Roman",
        "email": "roman@riquelme.com",
        "street": "Avellaneda",
        "street_number": 31,
        "phone_number": "1234141"
    },
    "sheet_number": 1
}
~~~

#### Example response 400 Bad Request:
~~~
{
    "error": "No Package matches the given query."
}
~~~
