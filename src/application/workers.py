from random import randint


def get_response_for_post_balances(data: dict[str, str]) -> dict[str, str]:
    response = data.copy()
    response.pop("openDate", None)
    response.pop("closeDate", None)
    match data["clientId"][0]:
        case "8":
            result = {
                "currency": "US", "maxLimit": "2000.00",
                "balance": f"{randint(1, 2000):.2f}"
            }
        case "9":
            result = {
                "currency": "EU", "maxLimit": "1000.00",
                "balance": f"{randint(1, 1000):.2f}"
            }
        case _:
            result = {
                "currency": "RUB", "maxLimit": "10000.00",
                "balance": f"{randint(1, 10000):.2f}"
            }
    response.update(result)

    return response
