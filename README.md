## Abstract

This project aims to experiment with a **wins-above-replacement (WAR) approach to valuating players in soccer**. 

A wins-above-replacement (WAR) approach is central to judging player skill and valuation, particularly in baseball and basketball leagues, such as the MLB or NBA. It compares a player's all-round statistics to a theoretically average player in their position, with the resultant statistic estimating how many more wins that player generates based on an average player.

The [MLB](https://www.mlb.com/glossary/advanced-stats/wins-above-replacement) pioneered the use of WAR to evaluate players, given the position-reliant nature that required metrics to compare players within the same position.

The NBA uses a more fluid and advanced version of WAR, looking to standardise statistics across roles. NBA's [VORP](https://www.basketball-reference.com/leaders/vorp_career.html) metric, Nate Silver's [RAPTOR](https://fivethirtyeight.com/features/how-our-raptor-metric-works/) metric, or John Holliger's [PER](https://www.basketball-reference.com/about/per.html) metric all attempt different methods at valuing the average difference in value for players.

We will take a non-rigid approach, **relying on machine learning techniques to determine the overall value of differences in all statistics to a statistical average**. We will be comparing players to a theoretical average in their position and in the same league. We can then use this model-estimated statistic to estimate a theoretical valuation for every player based on their underlying statistics over their past 5 seasons. 

## Approach

Raw datasets have been taken from JaseSiv's [WorldFootballR](https://jaseziv.github.io/worldfootballR/) database, and underlying data is taken from [FBref](https://fbref.com/en/) and [Transfermarkt](https://www.transfermarkt.com/).

Data cleaning was done through R, Python, and Excel. In particular, a player's valuations were estimated through taking their valuation from their past club, or from the previous year.

Our model can then be applied in two main steps:
    1. Calculating a generic WAR by averaging relevant statistics and using Principal Component Analysis (PCA) to generate a singular WAR statistic primarily based on variance to the theoretically "average" player.
    2. Regressing valuations seperately based on a player's position and league to calculate an objective "underlying" valuation.

## Limitations

- Better/more accurate approaches towards dimensionality reduction (particularly reducing data loss) can allow our model to determine better relationships between different statistics, and provide a more accurate valuation as a result. This can be attempted in the future.

- This approach discounts the "team factor" in calculations. For instance, players generally have better offensive stats on winning teams, in an offensively-geared formation, or if given more license to roam forward. Our approach treats all players in an average team - much like WAR in other sports.

## Further Developments

- I am planning to further research in this area by implementing future webscraping/API data to analyse future transfers, evaluating transfers in future transfer windows, or answering specific research questions, such as:
    - Does the "British Premium" exist from an objective viewpoint?
    - How does player valuation progression work for younger players in different leagues?
    - What are the other major factors that affect valuation besides underlying stats - e.g. team situation, playstyle fit, off-field situation, etc.

- Player Projections can be done by expanding research to look at specific players throughout their careers

- How effective is this method of valuation compared to other methods?

- Such research can be applied to other sporting leagues. Does our findings carry over to other leagues (NBA, MLB, etc.)? Does player valuation correlate to performance similarly in other sports?