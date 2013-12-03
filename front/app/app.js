/* App */

define(['backbone'],function(Backbone) {
	'use strict';

	var App = _.extend({
		'config': require.appConfig,
		'initialize': function(){
			require(
				['modules/default/router', 'modules/default/views/main'],
				function(DefaultRouter, DefaultViewsMain){
					/*Router initialisation*/
					DefaultRouter.initialize();
					this.view = new DefaultViewsMain($('#main'));
					Backbone.history.start({ pushState: true });
					return this;
				}.bind(this)
			);
		}
	});
	window.App = App;
	return App;

});
