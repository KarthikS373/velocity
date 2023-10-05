# Use a base image with Python and Jupyter Notebook
FROM jupyter/scipy-notebook:bbf0ada0a935

# Switch to the root user to install system-level dependencies
USER root
WORKDIR /tmp

# Install system-level dependencies
RUN apt-get update && \
    apt-get install -yq --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire project directory into the Docker image
COPY . velocity
WORKDIR /velocity
RUN chmod -R +x scripts

# Install Poetry globally
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set environment variables to prevent pip from complaining
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=""

# Install project dependencies using Poetry
RUN if [[ -n "${FULL}" ]] ; then \
    /usr/local/bin/poetry install --no-root --no-interaction --no-ansi --no-dev --extras "full" ; else \
    /usr/local/bin/poetry install --no-root --no-interaction --no-ansi --no-dev ; fi

# Switch back to the notebook user
USER $NB_UID

# Set the working directory to /home/jovyan/work
WORKDIR "$HOME/work"

# Configure Jupyter Lab to enable it
ENV JUPYTER_ENABLE_LAB "yes"

# Copy any additional configuration and startup scripts
# COPY jupyter_notebook_config.py /etc/jupyter/

# Set other environment variables
# ENV MY_ENV_VARIABLE "my_value"

# Run tests if TEST argument is provided
ARG TEST
RUN if [[ -n "${TEST}" ]] ; then \
    /usr/local/bin/poetry run pytest tests ; fi
