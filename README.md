# Options Pricing using MC Simulations

This repository contains a Python project focussed on options pricing using Monte Carlo simulations and the Black Scholes model. It was meant as an exercise to deepen my understanding of how pricing models work and the relationship between implied volatility and actual market prices.

## Project Aims
 * Implement and compare two options pricing models: Monte Carlo (MC) simulations and the Black-Scholes model
 * Analyse implied volatility data and compare options prices predicted by the MC simulation with actual market prices
 * Plot the volatility smile and volatility surface and compare the plots to what is theoretically expected
 * The current analysis focused on American options of AAPL, consisting of various expiry dates and strike prices


 ## Project Structure
 * 'analysis.ipynb': Notebook containing the whole analysis, including data processing and implementations of pricing models
 * 'mc_pricing.ipynb': Notebook used to develop and test the MC and BS pricing models

 The option chain data for AAPL could not be added to the repository due to its large size, it can be found on [Kaggle](https://www.kaggle.com/datasets/kylegraupe/aapl-options-data-2016-2020/discussion?sort=hotness). 


## Acknowledgements
This project serves as a practical exploration of the thoeries presented in Options, Futures, and Other Derivatives by John C. Hull. I also referred to existing implementations of specific aspects of the analysis online. I have credited these sources in the `analysis.ipynb` notebook. If there are any mistakes, inaccuracies, or conceptual flaws in this project, feel free to submit a pull request or drop me a note at asaadkhaja99@gmail.com.

