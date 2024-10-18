# ------------------------------------------------------------------------------
# General Commands
# ------------------------------------------------------------------------------

# Install Node Dependencies
install:
    npm install

# Start the development server
dev:
    npm run dev

# ------------------------------------------------------------------------------
# Prettier
# ------------------------------------------------------------------------------

# Check if code is formatted correctly
prettier-check:
    npx prettier . --check

# Format code with Prettier
prettier-format:
    npx prettier . --check --write
