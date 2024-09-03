import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class Option:
    def __init__(self, strike_price, time_to_maturity, spot_price):
        self.strike_price = strike_price
        self.time_to_maturity = time_to_maturity
        self.spot_price = spot_price  # Rename for clarity

    def payoff(self, spot_price):
        raise NotImplementedError("Payoff method from the relevant subclass should be used.")
    
    def bsm_price(self, sigma, risk_free_rate, option_type='call'):
        d1 = (np.log(self.spot_price / self.strike_price) + (risk_free_rate + 0.5 * sigma**2) * self.time_to_maturity) / (sigma * np.sqrt(self.time_to_maturity))
        d2 = d1 - sigma * np.sqrt(self.time_to_maturity)
        if option_type == 'call':
            return self.spot_price * norm.cdf(d1) - self.strike_price * np.exp(-risk_free_rate * self.time_to_maturity) * norm.cdf(d2)
        elif option_type == 'put':
            return self.strike_price * np.exp(-risk_free_rate * self.time_to_maturity) * norm.cdf(-d2) - self.spot_price * norm.cdf(-d1)
    
    def monte_carlo_price(self, time_step_count, sigma, risk_free_rate):
        dt = self.time_to_maturity / time_step_count
        np.random.seed(42)
        price_paths = []
        for i in range(10000):  # 10,000 simulations
            path = [self.spot_price]
            for _ in range(time_step_count):
                Z = np.random.standard_normal()
                St = path[-1] * np.exp((risk_free_rate - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
                path.append(St)
            price_paths.append(path)
        
        payoffs = [self.payoff(path[-1]) for path in price_paths]
        option_price = np.exp(-risk_free_rate * self.time_to_maturity) * np.mean(payoffs)
        return option_price

    def implied_volatility(self, target_price, option_type='call'):
        pass

    def historic_volatility(self):
        pass

class EuropeanCallOption(Option):
    def payoff(self, spot_price):
        return max(spot_price - self.strike_price, 0)
    
class EuropeanPutOption(Option):
    def payoff(self, spot_price):
        return max(self.strike_price - spot_price, 0)

    def bsm_price(self, sigma, risk_free_rate):
        return self.bsm_price(sigma, risk_free_rate, option_type='put')
    
class AsianOption(Option):
    def __init__(self, strike_price, time_to_maturity, spot_price, option_type='call'):
        super().__init__(strike_price, time_to_maturity, spot_price)
        self.option_type = option_type
    
    def average_price(self, price_path):
        return np.mean(price_path)
    
    def payoff(self, average_price):
        if self.option_type == 'call':
            return max(average_price - self.strike_price, 0)
        elif self.option_type == 'put':
            return max(self.strike_price - average_price, 0)
    
    def mc_price(self, time_step_count, sigma, risk_free_rate):
        dt = self.time_to_maturity / time_step_count
        np.random.seed(42)
        price_paths = []
        for i in range(10000):  # 10,000 simulations
            path = [self.spot_price]
            for _ in range(time_step_count):
                Z = np.random.standard_normal()
                St = path[-1] * np.exp((risk_free_rate - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
                path.append(St)
            price_paths.append(path)
        
        average_prices = [self.average_price(path) for path in price_paths]
        payoffs = [self.payoff(avg_price) for avg_price in average_prices]
        option_price = np.exp(-risk_free_rate * self.time_to_maturity) * np.mean(payoffs)
        return option_price

if __name__ == '__main__':
    spot_price = 150  
    strike_price = 160
    time_to_maturity = 1  # 1 year
    sigma = 0.2  # Example volatility
    risk_free_rate = 0.05  # 5% risk-free rate

    # European Call Option Example
    european_call = EuropeanCallOption(strike_price, time_to_maturity, spot_price)
    theoretical_call_price = european_call.bsm_price(sigma, risk_free_rate, option_type='call')
    mc_call_price = european_call.monte_carlo_price(1000, sigma, risk_free_rate)
    print(f"European Call Option Price: {theoretical_call_price - mc_call_price}")

    

    # # European Put Option Example
    # european_put = EuropeanPutOption(strike_price, time_to_maturity, spot_price)
    # put_price = european_put.bsm(sigma, risk_free_rate)
    # print(f"European Put Option Price: {put_price}")

    # # Asian Call Option Example
    # asian_call = AsianOption(strike_price, time_to_maturity, spot_price, option_type='call')
    # asian_call_price = asian_call.mc_price(time_step_count=252, sigma=sigma, risk_free_rate=risk_free_rate)
    # print(f"Asian Call Option Price: {asian_call_price}")
