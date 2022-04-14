# piazza-scraper
scrape piazza posts for your class

## usage
1. make and start a virtual environment e.g. ```virtualenv env && source env/bin/activate```
2. install requirements e.g. ```pip install -r requirements.txt```
3. copy config.txt into config.py via ```cp config.txt config.py```
4. write your piazza email and password securely into config.py
5. run the scraper ```python3 scraper.py```

## more stuff
- posts are put into the same file ```outputs/piazza_posts.md```, so rerunning the program will overwrite previous results
- I used selenium to check out links and scrape html since piazza doesn't use a publically available API call to grab data separately
- scraper may take a while (took 1 hr for 600 posts on macbook pro), have thought about parallelizing it though which would be pretty cool using multiprocessing correctly with locks
- config.py kinda important! make sure you put the correct url for your class's piazza and the number of posts you'd like to scrape
- invalid post ids that were not successfully scraped are printed to console at the end
- some of the selenium methods are deprecated so console mayn be flooded oops
