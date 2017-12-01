# Plivo Applications hosted on AWS Lambda

Set of AWS Lambda functions to handle Plivo calls.

## Building

Run `make <function>`, where `function` is a name of one of the `src/` subdirectories, for eg. `forward`.

## Adding new functions

1. Create a directory named as the function under `src/`.
1. Create a `lambda_function.py` file in the above directory, with `lambda_handler` function in it.
1. Add any dependencies to `src/requirements.txt`

## Plivo dependencies

The Plivo helper libraries are in `lib/plivo-python` via a git submodule.

## Deploying

For deployment, install dependencies and make sure configuration exists for awscli.
