ha-monitoring-bot
=================

Simple Telegram Bot which monitors your servers (e.g. your Home Assistant server) and informs you via Telegram.

Installation
------------

    pip install https://github.com/hille721/ha-monitoring-bot

Configuration
-------------

You can configure everything via one json file. Example `example_botconfig.json`:

    {
        "BOT_ADMINS": [
            "@CHANGE_ME"
        ],
        "BOT_TOKEN": "",
        "HAMONITOR": {
            "HOSTS": {
                "google": {
                    "IP": "142.250.186.110",
                    "APPLICATIONS": {
                        "google": {
                            "PORT": 80,
                            "PATH": ""
                        },
                        "gmail": {
                            "PORT": 80,
                            "PATH": ""
                        }
                    }
                },
                "notexistent": {
                    "IP": "192.192.192.192",
                    "INTERVAL": 10,
                    "DELAY": 2,
                    "APPLICATIONS": {
                        }
                    }
                }
            },
            "DEFAULT_INTERVAL": 120,
            "DEFAULT_DELAY": 90
        },
    }

Start
-----

    export BOTCONFIG=example_botconfig.json
    errbot -c src/hamonitor/config.py

It is really recommended to run this inside a container or a service. There are also Ansible roles to deploy the bot (tbd).
