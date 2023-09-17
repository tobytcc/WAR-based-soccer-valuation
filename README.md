## Abstract

This project aims to experiment with a **wins-above-replacement (WAR) approach to valuating players in soccer**. 

A wins-above-replacement (WAR) approach is central to judging player skill and valuation, particularly in baseball and basketball leagues, such as the MLB or NBA. It compares a player's all-round statistics to a theoretically average player in their position, with the resultant statistic estimating how many more wins that player generates based on an average player.

The [MLB](https://www.mlb.com/glossary/advanced-stats/wins-above-replacement) pioneered the use of WAR to evaluate players, given the position-reliant nature that required metrics to compare players within the same position.

The NBA uses a more fluid and advanced version of WAR, looking to standardise statistics across roles. NBA's [VORP](https://www.basketball-reference.com/leaders/vorp_career.html) metric, Nate Silver's [RAPTOR](https://fivethirtyeight.com/features/how-our-raptor-metric-works/) metric, or John Holliger's [PER](https://www.basketball-reference.com/about/per.html) metric all attempt different methods at valuing the average difference in value for players.

We will take a non-rigid approach, **relying on dimensionality reduction techniques to determine the overall value of differences in all statistics to a statistical average**. We will be comparing players to a theoretical average in their position and in the same league. We can then use this model-estimated statistic to estimate a theoretical valuation for every player based on their underlying statistics over their past 5 seasons. 

## Approach

Raw datasets have been taken from JaseSiv's [WorldFootballR](https://jaseziv.github.io/worldfootballR/) database, and underlying data is taken from [FBref](https://fbref.com/en/) and [Transfermarkt](https://www.transfermarkt.com/).

Data cleaning was done through R, Python, and Excel. In particular, a player's valuations and position were estimated through taking their valuation from their past club, or from the previous year.

Our model can then be applied in two main steps:

    1. Calculating a generic "VORP" (Value Over Replacement Player - similar to NBA approach) by averaging relevant statistics and using Principal Component Analysis (PCA) to generate a singular WAR statistic primarily based on variance to the theoretically "average" player. 
    
    Our PCA analysis has two goals: to maximise variance across per90/% statistics (prioritising capture of variance across players to find "value above average"), and minimising information loss when reducing dimensions. 

    2. Regressing valuations seperately based on a player's position and league to calculate an objective "underlying" valuation. Each player will have a calculated valuation, and a market value from Transfermarkt.

## Operating Instructions

**UPDATE (17/09/2023):** Website is no longer up. Program can be run by running app.py and hosting the website on your own device.

This is what the app should look like (ignore the terrible UI - will improve if given time):
![app-photo](/img/app-photo.png)

The app features several basic interactive elements, such as dropdown menus to choose your player (on both sides), and interactive graphs.
![interactive-photo](/img/app-interactive.png)

## Reflection

I used this project as an introduction to sports analytics, an area I have major interest in. This project gave me huge insight into how data-driven the industry has shifted towards, and how statistics weigh into market value (as all clubs use statistical models to value players). I would like to explore sports analytics and valuation extensively in the future.

In terms of project learning, I can split it into four steps: 

    1. Data collection was fun - I think data engineering could be an area I could explore more.

    2. Data processing for machine learning took a lot of time, but it taught me a lot about working with Pandas, NumPy, and SciPy. Data processing is an area of improvement for me.

    3. PCA Analysis was really fun! Even if the program was based on previous libraries, I learnt a lot about statistical methods and optimization, as well as vector calculations through my research and prep in understanding this method.

    4. Designing the Dash app was very time-consuming, and I discovered that I don't enjoy front-end design (although it is a very useful skill). I want to work with more frameworks in future to find simpler, more efficient front-end designs for my projects.

I learnt a lot about other crucial elements for data science. I enacted best practices in version control, documentation, and data management throughout the project. I also ensured I was coding regularly, and purposely struggling through difficult aspects to gain a better experience - this was probably why I learnt so much!

## Known Issues

- When running the Dash app, the first runthrough will fail to render (throw errors in processing graph). Refreshing always fixes this issue.

- The website cannot handle missing data (of which I have tried to reduce as much as possible), given a lack of exceptions or redundencies. 

## Limitations

- Better/more accurate approaches towards dimensionality reduction (particularly reducing data loss) can allow our model to determine better relationships between different statistics, and provide a more accurate valuation as a result. This can be attempted in the future.

- This approach discounts the "team factor" in calculations. For instance, players generally have better offensive stats on winning teams, in an offensively-geared formation, or if given more license to roam forward. Our approach treats all players in an average team - much like WAR in other sports.

- Stats can be better optimised:
    - Statistics weighted have a slight preference towards offensive strengths - this is an inherent issue with modern stats counting, as defensive statistics are not as prioritised in datasets. **To remedy this, I've overprioritised (overweighted) defensive stats on a few occasions.**
    - Per90/percentage stats can be created from counting stats through further preprocessing.
    - A statistical approach to finding weights and reducing covariances can help fine-tune weights and relationships between variables, uncovering the "true" importance of each statistics - this would require lots of time.

## Further Developments

- I am planning to further research in this area by implementing future webscraping/API data to analyse future transfers, evaluating transfers in future transfer windows, or answering specific research questions, such as:
    - Does the "British Premium" exist from an objective viewpoint?
    - How does player valuation progression work for younger players in different leagues?
    - What are the other major factors that affect valuation besides underlying stats - e.g. team situation, playstyle fit, off-field situation, etc.

- Player Projections can be done by expanding research to look at specific players throughout their careers, and by comparing them to similar players (regardless of position or league).

- How effective is this method of valuation compared to other methods?

- Such research can be applied to other sporting leagues. Does our findings carry over to other leagues (NBA, MLB, etc.)? Does player valuation correlate to performance similarly in other sports?