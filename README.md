# InstaStats
Simple python script for tracking number of posts, followers and followings over time. No API-key needed.
I used this case to learn more about Python programming and get myself into it.

## Scraping data

### Direct execution
```
python save.py <account>
```

### Scheduled via crontab

```
# m h dom mon dow command
55 19 * * * screen -dmS stats python save.py <account>
```
