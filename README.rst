.. image:: https://github.com/hille721/ha-monitoring-bot/actions/workflows/python-test.yml/badge.svg
    :alt: build
    :target: https://github.com/hille721/ha-monitoring-bot/actions/workflows/python-test.yml

=================
ha-monitoring-bot
=================

Simple Telegram Bot which monitors your servers (e.g. your Home Assistant server) and informs you via Telegram.

Installation
============

.. code-block::

    pip install git+https://github.com/hille721/ha-monitoring-bot.git

Configuration
=============

You can configure everything via one json file. Example `example_botconfig.json`:

.. code-block::

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
                            "PATH": "/gmail"
                        }
                    }
                },
                "notexistent": {
                    "IP": "192.192.192.192",
                    "APPLICATIONS": {}
                    "INTERVAL": 20,
                    "DELAY": 5
                    }
                }
            },
            "DEFAULT_INTERVAL": 120,
            "DEFAULT_DELAY": 90
        },
    }

Start
=====

.. code-block::

    export BOTCONFIG=example_botconfig.json
    errbot -c src/hamonitor/config.py

It is really recommended to run this inside a container or a service. There is also an Ansible roles to deploy the bot as a
`service <https://github.com/hille721/ha-monitoring-bot/contrib/roles>`_.
