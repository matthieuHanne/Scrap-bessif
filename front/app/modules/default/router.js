/* Post index*/
define(['app', 'backbone'], function(App, Backbone) {
    'use strict';

	var Router = {
		'initialize': function(){
			var routes = {
				'routes':{ 
					'': 'index',
					'scrap': 'scrap',
				},
				
				'index': function(){
					console.log('index route');
				},
				'scrap': function(){
					require(['modules/scrap/main'], function(ScrapMain){
						console.log('scrap route');
						ScrapMain.initialize();
					});
				},
				'blog': function(){console.log('blog route');}
			};
		new (Backbone.Router.extend(routes))();
	}}; 
    return Router;
});
/*
            'default': function(){
            },
            'posts/edit': function(){
                App.view.render(PostView.render, $('.content'));
                alert('tata');
            }
*/


