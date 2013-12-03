/*global define*/

define(['backbone', 'text!modules/about/templates/projects.tpl','resources/projects/items' ,'bootstrap'], function(Backbone, tpl, Items){
    'use strict';

    return Backbone.View.extend({
		'tagName'	: 'section',
		'className'	: 'section',
		'id': 'section3',
        'initialze'	: function(){

        },
        'events'    : {
			'click .article-tags li' : 'indexProject'         	
        },
        'render': function(){
            this.$el.html(_.template(tpl));
            return this;
        },
        'indexProject': function(){
        	console.log(Items['CommOnEcoute'])
        }
    });
});
