#!/bin/bash

docker run --env SDENV=local --rm -it -p 80:80 -v "$(pwd)"/app:/app snippetdog
