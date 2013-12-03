/*global define*/

define(['backbone', 'text!modules/scrap/templates/index.tpl'], function(Backbone, tpl){
	'use strict';

	return Backbone.View.extend({
		'tagName'	: 'section',
		'className'	: 'section',
		'id': 'section1',
		'initialze'	: function(){
		},
		'render': function(){
			this.$el.html(_.template(tpl));
			return this;
		}
	});
});
