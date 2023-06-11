# Project Planner

A tool for helping to plan woodworking cuts using the fewest number of boards/pieces.

## Getting Started

Run `make setup` to create the virtual environment and install dependencies:
```
make setup
```

Copy the project manifest template:
```
cp project.yaml.tmpl project.yaml
```

Edit `project.yaml` in your editor of choice listing out the materials in your project
and the cuts you will need to make for each of them.

Invoke the script:
```
make run
```