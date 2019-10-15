from main.models import Portfolio

portfolio_names = "Chairman", "Vice-Chairman", "Secretary", "Treasurer", "Other", "Member"


def create_portfolios():
    for name in portfolio_names:
        if not Portfolio.objects.filter(portfolio_name=name).exists():
            portfolio = Portfolio()
            portfolio.portfolio_name = name
            if name != "Member":
                portfolio.is_Exec = True
            else:
                portfolio.is_Exec = False
            portfolio.save()
            print(name + " does not exist")
    print("Hello")
