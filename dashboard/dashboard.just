# ------------------------------------------------------------------------------
# General Commands
# ------------------------------------------------------------------------------

# Install Node Dependencies
install:
    npm install

# Install Node Dependencies in CI
ci-install:
    npm ci

# Start the development server
dev:
    npm run dev

# ------------------------------------------------------------------------------
# Eslint
# ------------------------------------------------------------------------------

eslint-check:
    npx eslint .

eslint-fix:
    npx eslint . --fix

# ------------------------------------------------------------------------------
# Prettier
# ------------------------------------------------------------------------------

# Check if code is formatted correctly
prettier-check:
    npx prettier . --check

# Format code with Prettier
prettier-format:
    npx prettier . --check --write
