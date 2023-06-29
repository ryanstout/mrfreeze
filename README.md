MrFreeze is a tool for sending cold emails. Use natural language to search for
comapnies that fit a query ("find startup's that have less than 50 people in the
health care space"), then find people in those companies based on another query.
(Find people with a title similar to "...")

# Setup

asdf python install 3.11.1
asdf local 3.11.1
pip install poetry
poetry install
brew install openapi-generator
npm install -g swagger-converter

# Run

```
poetry shell
python -m mrfreeze
```

# RocketReach API

If you need to update the rocketreach spec to 3.0, do so at https://converter.swagger.io/#/Converter/convertByContent

`openapi-generator generate -i src/rocketreach/rocketreach_openapi_spec_v3.json -g python -o src/rocketreach/api --skip-validate-spec`

# Example searches

Find all people working in the partnership org in all companies between 100 and 1000 employees

Find technology accounting firms
