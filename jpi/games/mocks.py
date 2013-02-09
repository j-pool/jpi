__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

import datetime

NOW = datetime.datetime.now()

MOCK_GAMES = [
    [#year
    	[#week
    		{#game
    		'home': 'GB',
    		'away': 'MIN',
			'date': NOW,
			'type': 'regular',
			'spread': -5
    		},
    		{
    		'home': 'ARZ',
    		'away': 'PIT',
			'date': NOW,
			'type': 'regular',
			'spread': -2
    		},
    		{
    		'home': 'SEA',
    		'away': 'SF',
			'date': NOW,
			'type': 'regular',
			'spread': 4
    		},
    		{
    		'home': 'DET',
    		'away': 'NYG',
			'date': NOW,
			'type': 'regular',
			'spread': 0.5
    		},
    		{
    		'home': 'NYJ',
    		'away': 'MIA',
			'date': NOW,
			'type': 'regular',
			'spread': 0
    		}
    	],
        [#week
            {#game
            'home': 'ATL',
            'away': 'SF',
			'date': NOW,
			'type': 'regular',
			'spread': -1
            },
            {
            'home': 'OAK',
            'away': 'SD',
			'date': NOW,
			'type': 'regular',
			'spread': 14
            },
            {
            'home': 'JAC',
            'away': 'TB',
			'date': NOW,
			'type': 'regular',
			'spread': 1
            },
            {
            'home': 'TEN',
            'away': 'GB',
			'date': NOW,
			'type': 'regular',
			'spread': 1.5
            },
            {
            'home': 'BUF',
            'away': 'NO',
			'date': NOW,
			'type': 'regular',
			'spread': 17.5
            }
        ],
    ],
    [#year
        [#week
            {#game
            'home': 'WAS',
            'away': 'OAK',
			'date': NOW,
			'type': 'regular',
			'spread': -2
            },
            {
            'home': 'BAL',
            'away': 'NYE',
			'date': NOW,
			'type': 'regular',
			'spread': 10
            },
            {
            'home': 'SEA',
            'away': 'STL',
			'date': NOW,
			'type': 'regular',
			'spread': 12
            },
            {
            'home': 'CHI',
            'away': 'PHI',
			'date': NOW,
			'type': 'regular',
			'spread': -7
            },
            {
            'home': 'HOU',
            'away': 'DAL',
			'date': NOW,
			'type': 'regular',
			'spread': 4
            }
        ],
    ]
]