# 9 Tile Puzzle Solver

![Static Badge](https://img.shields.io/badge/v3.10.12-blue?logo=python&logoColor=yellow&labelColor=gray)

## Table of contents

- [Architecture](#Architecture)
- [Folder Structure](#folder-structure)
- [Setup](#Setup)
- [Local Development](#local-development)

## Architecture
## Folder Structure
```plaintext
9-tile-puzzle-solver/
                    ├──game/                Main Application Framework Code
                    ├──sol/
                          ├──solution.py      Algorithms Implementation to Solve the Puzzle
                          ├──test.py          Testing code to check the working of Algorithms
                          ├──time.py          Code to show different efficiencies of different algorithm Implementations
                    ├──requirements.txt     Python Dependencies 
                    ├──README.md            Documentation File
```

## Install all the necessary libraries:

### Navigate to the app directory

```bash
cd 9-tile-puzzle-solver/game/
```

### Create and activate Virtual Environment

```bash
python -m venv env
source env/bin/activate
```

```bash
pip install -r requirements.txt
```

## To Run Locally and Test
```
python3 puzzle.py
```

# Docker Setup Guide

## Overview

This guide is designed to help contributors set up and run the backend service using Docker. Follow these steps to ensure that your development environment is configured correctly.

## Prerequisites

Before you start, ensure you have the following installed:

- Docker
- Python

## Installation Instructions

### 1. Build the Docker Image

Navigate to the project's root directory and build the Docker image. Typically, this is done with the following command:

```Bash
docker build -t <image_name> .
```

### 3 Run the Docker Container

Run the Docker container using the following command:

```bash
docker run -p 8000:8000 <image_name>
```

This command starts a detached container that maps port 8000 of the container to port 8000 on the host.
