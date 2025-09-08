ROOT_DIR="$(git rev-parse --show-toplevel)"

${ROOT_DIR}/.venv/bin/python ${ROOT_DIR}/src/main.py "$@"