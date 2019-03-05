class Config(object):
    JOBS = [
        {
            'id': 'booking',
            'func': 'tasks:booking',
            'args': (),
            'trigger': {
                'type': 'cron',
                'day_of_week': "mon-sun",
                'hour': '5',
                'minute': '0-1',
                'second': '2,5,10'
            }
        }
        ,
        {
            'id': 'checkin',
            'func': 'tasks:checkin',
            'args': '',
            'trigger': {
                'type': 'cron',
                'day_of_week': "mon-sun",
                'hour': '8',
                'minute': '0',
                'second': '11'
            }
        },
        {
            'id': 'clearLog',
            'func': 'tasks:clearLog',
            'args': '',
            'trigger': {
                'type': 'cron',
                'day_of_week': "mon-sun",
                'hour': '8',
                'minute': '0',
                'second': '11'
            }
        }
    ]

    SCHEDULER_API_ENABLED = True
