from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class City(BaseModel):
    name_city: str
    country: str
    mayor: str
    population: int | None = None
    date_founded: int | None = None
    area: float | None = None
    ranking: int


class Country(BaseModel):
    country: str
    leader: str
    capital: str
    population: int | None = None
    area: float | None = None
    ranking: int


city1 = {
    "name_city": "London",
    "country": "England",
    "mayor": "Sadiq Khan",
    "population": 8799800,
    "date_founded": 47,
    "area": 1572.03,
    "ranking": 2
}

city2 = {
    "name_city": "Tokyo",
    "country": "Japan",
    "mayor": "Yuriko Koike",
    "population": 13988129,
    "date_founded": 1868,
    "area": 2194.07,
    "ranking": 3
}

city3 = {
    "name_city": "Paris",
    "country": "France",
    "mayor": "Anne Hidalgo",
    "population": 2165423,
    "date_founded": 508,
    "area": 105.4,
    "ranking": 4
}

city4 = {
    "name_city": "Montreal",
    "country": "Canada",
    "mayor": "Valérie Plante",
    "population": 1762949,
    "date_founded": 1642,
    "area": 431.50,
    "ranking": 1
}

country1 = {
    "country": "Chile",
    "leader": "Gabriel Boric",
    "capital": "Santiago",
    "population": 18430408,
    "area": 756096.3,
    "ranking": 1
}

country2 = {
    "country": "India",
    "leader": "Droupadi Murmu",
    "capital": "New Delhi",
    "population": 1375586000,
    "area": 3287263,
    "ranking": 4
}

country3 = {
    "country": "Norway",
    "leader": "Harald V",
    "capital": "Oslo",
    "population": 5425270,
    "area": 385207,
    "ranking": 2
}

country4 = {
    "country": "South Africa",
    "leader": "Cyril Ramaphosa",
    "capital": "Cape Town",
    "population": 60142978,
    "area": 1221037,
    "ranking": 3
}

city_list = [city1, city2, city3, city4]
country_list = [country1, country2, country3, country4]

@app.post("/country")
async def post_country(country: Country):
    return country


@app.get("/city")
async def get_city():
    return city_list


@app.get("/country/{ranking}")
async def get_country(ranking: int):
    for country in country_list:
        if country.get("ranking") == ranking:
            return country
    return {"Country not found"}
