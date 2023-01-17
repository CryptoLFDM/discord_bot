from enum import Enum


class Coin(Enum):
    atom = 0
    bitcoin = 1
    flux = 2
    bnb = 3


MapperSite = {
    "atom": "cosmos-hub",
    "bitcoin": "bitcoin",
    "flux": "flux-zelcash",
    "bnb": "bnb"
              }


MapperApi = {
    "atom": "cosmos",
    "bitcoin": "bitcoin",
    "flux": "zelcash",
    "bnb": "binancecoin"
              }
