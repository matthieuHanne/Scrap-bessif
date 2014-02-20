/* Post index*/
define(['app', 'backbone'], function(App, Backbone) {
    'use strict';

	var Router = {
		'initialize': function(){
			var routes = {
				'routes':{ 
					'': 'index',
					'blog': 'blog',
					'about': 'about',
				},
				
				'index': function(){
					console.log('index route');
				},
				'about': function(){
					require(['modules/about/main'], function(AboutMain){
						AboutMain.initialize();
					});
					console.log('about route');},
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


