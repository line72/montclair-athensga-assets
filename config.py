# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'athensga',
    package_name = 'montclair-athensga',
    name = 'Go Athens',
    description = 'Real Time Tracking of the Buses for Athens, GA',
    url = 'https://athensga.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.4.3',
        revision = 2,
        title = 'Go Athens',
        first_run_text = "Welcome to Athens, GA's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.athensga',
        app_store_id = 'REPLACE_ME',
        app_store_url = 'https://apps.apple.com/us/app/go-athensga/idREPLACE_ME'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.athensga',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.athensga'
    )
)
