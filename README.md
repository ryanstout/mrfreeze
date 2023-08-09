MrFreeze is a tool for sending cold emails. Use natural language to search for
comapnies that fit a query ("find startup's that have less than 50 people in the
health care space"), then find people in those companies based on another query.
(Find people with a title similar to "...")

# Setup/Requirements

A recent version of Postgres running on localhost

```
asdf python install 3.11.1
asdf local 3.11.1
pip install poetry
poetry install
```

# Details

MrFreeze consists of python code to manages the AI company search, and a Remix app in the `web` folder for the user interface

# Run

The remix app shells out to python so you need to run `poetry shell` before running `npm run dev`

```
poetry shell
cd web
npm run dev
```

# Example searches

Find all people working in the partnership org in all companies between 100 and 1000 employees

Find technology accounting firms

# Generate prisma

```
PRISMA_PY_DEBUG_GENERATOR=1 npx prisma generate
```

```
python -m bin.fetch_companies_and_people "cljon3f5k0000bv6hdu9vhfq8" "healthcare" "purchasing software"
```

mkdir llama2
cd llama2
