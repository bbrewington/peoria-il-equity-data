# peoria-il-equity-data

Working with data from Peoria Equity Accountability Program (PeAP), for Peoria, IL (US): https://peoriagov.org/375/Minority-and-Women-Owned-Business-Regist

This repo was inspired by this GovLove episode, "Diversity and Inclusion in Peoria, IL with Melodi Green": https://elgl.org/podcast-diversity-and-inclusion-in-peoria-il-with-melodi-green/

Google My Map (using most recent scrape results): https://www.google.com/maps/d/u/0/edit?mid=1XfwyjE-2GxCKEsbhDYnsC0eY4UUetTc&usp=sharing

## How to run it yourself

1. Open a command line (Mac: Terminal, Windows: [git bash](https://gitforwindows.org/))
2. Clone this repo & Set it as working directory
    ```bash
    > git clone https://github.com/bbrewington/peoria-dei-data
    > cd peoria-dei-data
    ```
3. Run the setup script.  This will create a virtual environment for your project and install the packages listed in `requirements.txt`
   ```bash
   > setup.sh
   ```
4. Run the code
  - Option 1, Jupyter Notebook: Open get_dei_data.ipynb and select Jupyter kernel that was installed by above setup script (this way, you'll be running the Jupyter notebook in same virtual environment w/ package versions noted in requirements.txt)
  - Option 2, Python script: With virtual environment active, run `python3 get_dei_data.py`

NOTE: if you run into any issues following the above, feel free to submit a bug report in "Issues" tab

## Contributing

Glad to collaborate on this and/or pass off to Peoria people (especially women & minorities in tech in Peoria :smile:) - feel free to Fork & Pull Request if you want to submit changes.  Also, you're welcome to reach out and request me to add you as co-owner of the repo

## Next Steps (TODO's)

- Grab peoria.org Minority-Owned Businesses & see if they're captured
  - [ ] https://peoria.org/black-owned-peoria/
  - [ ] https://peoria.org/hispanic-owned-peoria
- [ ] Set up `peoria_dei_data/get_dei_data.py` to accept command-line arguments (via something like argparse)
- [ ] Handle businesses with multiple locations
