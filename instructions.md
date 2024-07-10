# Installing dependencies
1. Create a virtual environment
2. install dependencies with `pip install -r requirements.txt`

# Generating the "Overview" page
1. Go to pages `pages/Overview/Overview.py` and follow the instructions there

# Let's visualize our first page

1. Go to `main.py` at the root of the project and:
    a. Import the `Overview.py` file
    b. add an entry `"Overview": Overview` in the pages dictionary

2. Run `taipy run main.py` and take a look at your page!

# Generating the "Analysis" page
1. Go to `pages/Analysis/Analysis.py` and follow the instructions there

# Creating a shared header for all pages
1. Go to `root.md` and `root.py` and follow the instructions there
The instructions to fill `root.md` are in `instructions_root.md`
When finished, add the root page to the pages dictionary with the following entry: `"/": root_page`

# Generating the "Predictions" page with scenarios, data nodes and tasks
0. Go to `configuration/config.py` and follow the instructions there to learn about data nodes, tasks and scenarios
1. Go to `pages/Predictions/Predictions.py` and follow the instructions there