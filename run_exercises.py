import portfolio.data
import portfolio.report
from portfolio.assets import make_asset
my_portfolio = portfolio.data.create_portfolio("Retirement")
portfolio.report.print_report(my_portfolio)