# Portable environment guidance

Use an environment explicitly supplied by the user, event, or repository. Do not assume a virtualenv path, Conda environment name, operating system, package manager, or globally installed tool.

- Run from the challenge directory and place generated data in `.work/` when practical.
- Before lengthy work, record the interpreter/tool version and confirm required dependencies are available.
- For Python, use the project's documented virtual environment or create a task-local environment only when the user authorizes dependency changes.
- Use SageMath only when the mathematical workload needs it and a Sage environment is available or approved.
- Report unavailable dependencies rather than silently installing packages or changing global environments.
- Include relevant environment setup and versions in reproducible solver notes.
