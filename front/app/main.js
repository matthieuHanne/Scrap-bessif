/* require initialisation*/
require.config({
    'baseUrl': require.appConfig.host,
    'paths': {
        'backbone': 'lib/backbone-0.9.9.min',
        'app': 'app/app',
        'modules': 'app/modules',
        'underscore': 'lib/lodash',
        'waypoints': 'lib/waypoints',
        'easing': 'lib/jquery-easing.1.3',
        'bootstrap': 'lib/bootstrap.min',
        'resources': 'app/resources',
    },
    'shim': {
        'backbone': {
            'deps': [
                'lib/lodash-1.0.0.min',
                'lib/jquery-1.8.3.min',
            ],
            'exports': 'Backbone'
        },
        'easing': {
            'deps': [
            	'lib/jquery-1.8.3.min'
            ]
        }

    }
});

define(['app'],
    function(App) {
    App.initialize();
});
