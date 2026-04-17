from portfolio.metrics import calculate_asset_value, calculate_portfolio_value

def calculate_asset_value(asset: dict) -> float:
    return asset["price"] * asset["quantity"]

def make_asset(ticker: str, price: float, quantity: int) -> dict:
    return {
        "ticker": ticker,
        "price": price,
        "quantity": quantity
    }

def get_asset_value(asset: dict) -> float:
    return calculate_asset_value(asset)