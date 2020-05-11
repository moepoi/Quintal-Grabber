# Quintal Grabber

*Get Data from Quintal Private API*

[![pipeline status](https://gitlab.com/moepoi/Quintal-Grabber/badges/master/pipeline.svg)](https://gitlab.com/moepoi/Quintal-Grabber/-/commits/master)

## Installation

Installation is simple. It can be installed from pip using the following command:
```sh
$ pip3 install -r requirements.txt
```

## Usage

```sh
from Quintal import QuintalGrabber

id = 3645
quintal = QuintalGrabber(id)
x = quintal.get_identity()
print (x)
```

## Credit

Moe Poi ~ / [@moepoi](https://github.com/moepoi)
