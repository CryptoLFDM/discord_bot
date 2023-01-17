from enum import Enum


class Coin(Enum):
    atom = 0
    bitcoin = 1
    flux = 2
    bnb = 3
    osmosis = 4
    solana = 5
    comdex = 6


MapperSite = {
    "atom": "cosmos-hub",
    "bitcoin": "bitcoin",
    "flux": "flux-zelcash",
    "bnb": "bnb",
    "osmosis": "osmosis",
    "solana": "solana",
    "comdex": "comdex"
}


MapperApi = {
    "atom": "cosmos",
    "bitcoin": "bitcoin",
    "flux": "zelcash",
    "bnb": "binancecoin",
    "osmosis": "osmosis",
    "solana": "solana",
    "comdex": "comdex"
              }
