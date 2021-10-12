# Purpose
This project is meant to streamline the search for ABC triplets on the TNG Tech website. This is accomplished by automating the clicking of the "Start" button and logging the results of the search locally, for curiosity's sake.

# Installation
This project uses Selenium to emulate a browser to do the work of the ABC triplet search. Specifically, it is designed with the Chrome driver, though it is easy enough to use your own browser's driver.

To get started, simply run `pip install -r requirements.txt` and make sure that the [latest Chrome driver](https://chromedriver.storage.googleapis.com/index.html) (or whatever your preferred browser's driver is) is installed on your machine, and in your `PATH` environment variable.

Change the settings in `config.json` to reflect your name, and how many parallel threads you would like to use to search. I use an AMD Threadripper 1950x, so 16 threads works well enough for me that it never uses 50% of my CPU power. Know your system, and change this setting appropriately.

# Running
To run the search, simply do `python main.py`. As the search progresses, the `output.ndjson` file will log your results. To analyze your results, run `python analysis.py` to get statistics on how well you're doing. A histogram will show you the distribution of q (quality) values you've found on your triplets.