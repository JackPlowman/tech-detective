# ------------------------------------------------------------------------------
# Common Commands
# ------------------------------------------------------------------------------

# Install python dependencies
install:
    poetry install

# Install playwright dependencies
playwright-install:
    poetry run playwright install

# End to End Tests
end-to-end-tests:
    poetry run pytest end_to_end

# Validate the schema of the project technologies and frameworks json file
validate-schema:
    poetry run check-jsonschema --schemafile schema_validation/project_technologies_and_frameworks_schema.json schema_validation/project_technologies_and_frameworks.json

# ------------------------------------------------------------------------------
# Cleaning Commands
# ------------------------------------------------------------------------------

# Remove all generated files
clean:
    find . \( \
      -name '__pycache__' -o \
      -name '.coverage' -o \
      -name '.mypy_cache' -o \
      -name '.pytest_cache' -o \
      -name '.ruff_cache' -o \
      -name '*.pyc' -o \
      -name '*.pyd' -o \
      -name '*.pyo' -o \
      -name 'coverage.xml' -o \
      -name 'db.sqlite3' \
    \) -print | xargs rm -rfv

# ------------------------------------------------------------------------------
# Ruff - Python Linting and Formating
# Set up ruff red-knot when it's ready
# ------------------------------------------------------------------------------

# Fix all Ruff issues
ruff-fix:
    just tests::ruff-format-fix
    just tests::ruff-lint-fix

# Check for Ruff issues
ruff-lint:
    poetry run ruff check .

# Fix Ruff lint issues
ruff-lint-fix:
    poetry run ruff check . --fix

# Check for Ruff format issues
ruff-format:
    poetry run ruff format --check .

# Fix Ruff format issues
ruff-format-fix:
    poetry run ruff format .

