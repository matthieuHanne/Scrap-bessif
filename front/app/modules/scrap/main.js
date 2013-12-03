/* About module*/
define(['app', 'backbone'], function(App, Backbone) {
	'use strict';

	var Scrap = _.extend({
		'initialize': function(){
			// Set up views
			require(['modules/scrap/views/index'],
			function(ScrapViewIndex){
				App.view.render((new ScrapViewIndex()).render(), '#container');
				//get projects from API
				/*Menu at last, because he load his elements from */
				//postsCollection.fetch({'success': function(){
				// Set up waipointsi
				//
				//}});
			});
		}.bind(this)
	});
	return Scrap;
});
