# data Folder

## Files & Folders

These are all in the top-level .gitignore - currently storing source of truth scraped data in Google Drive / My Maps, in Brent's account: brent.brewington@gmail.com --> so not saving the actual scraped 

- `/data`
  - `scrape_run_YYYYMMDD`
    - `/pages`: HTML page content, filename is ####.html where #### is the page id (code saves these locally so user can re-run scraper without re-sending GET request to web server)
    - `business_pages_parsed.csv`: output of the scraper, table with one row per business
    - `business_pages.txt`: URL of indiviual business pages, from https://www.eprismsoft.com/business/showCert?id=140
