#!/bin/bash

docker stop $(docker ps -q --filter ancestor=snippetdog)
