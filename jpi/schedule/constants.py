__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com'

import datetime

NOW = datetime.datetime.now()

MOCK_SCHEDULE = [
    [#year
    	[#week
    		{#game
    		'home': 'GB',
    		'away': 'MIN',
			'date': NOW,
			'type': 'regular'
    		},
    		{
    		'home': 'ARZ',
    		'away': 'PIT',
			'date': NOW,
			'type': 'regular'
    		},
    		{
    		'home': 'SEA',
    		'away': 'SF',
			'date': NOW,
			'type': 'regular'
    		},
    		{
    		'home': 'DET',
    		'away': 'NYG',
			'date': NOW,
			'type': 'regular'
    		},
    		{
    		'home': 'NYJ',
    		'away': 'MIA',
			'date': NOW,
			'type': 'regular'
    		}
    	],
        [#week
            {#game
            'home': 'ATL',
            'away': 'SF',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'OAK',
            'away': 'SD',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'JAC',
            'away': 'TB',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'TEN',
            'away': 'GB',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'BUF',
            'away': 'NO',
			'date': NOW,
			'type': 'regular'
            }
        ],
    ],
    [#year
        [#week
            {#game
            'home': 'WAS',
            'away': 'OAK',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'BAL',
            'away': 'NYE',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'SEA',
            'away': 'STL',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'CHI',
            'away': 'PHI',
			'date': NOW,
			'type': 'regular'
            },
            {
            'home': 'HOU',
            'away': 'DAL',
			'date': NOW,
			'type': 'regular'
            }
        ],
    ]
]