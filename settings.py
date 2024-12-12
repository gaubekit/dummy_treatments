from os import environ

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='weakestlinkdemo', num_demo_participants=4,
                        app_sequence=['App01ConsentAndCheck',
                                      'App03WeakestLink',
                                      ])]





DEBUG = False
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['optInConsent',
                      'consent',
                      'micCheck',
                      'cameraCheck',
                      'audioCheck',
                      'numberVideo', 'colorVideo',
                      'payoff_ppg',
                      'payoff_round',
                      'past_group_id',
                      'arrival_time',
                      'wait_page_arrival',
                      'is_dropout',
                      'svo',
                      'perfect_stranger_id',
                      # TODO: add pvq_1, pvq_2, pvq_3, pvq_4, pvq_5
                      ]

SESSION_FIELDS = ['group_matrix']
ROOMS = [
    dict(
        name='HapsPilot',
        display_name='HAPS Pilot'
    )]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'
OTREE_REST_KEY = 'otreehapsserverrest3'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
