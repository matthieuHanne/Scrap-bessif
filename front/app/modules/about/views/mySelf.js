/*global define*/

define(['backbone', 'text!modules/about/templates/mySelf.tpl', 'text!modules/about/templates/resume.tpl', 'text!modules/about/templates/skills.tpl'], function(Backbone, tpl, resumeTpl, skillsTpl){
    'use strict';

    return Backbone.View.extend({
		'tagName'	: 'section',
		'className'	: 'section',
		'id': 'section2',
        'initialze'	: function(){
        },
        'events': {
			'click li' : 'showTopic'
        },
        'render': function(){
            this.$el.html(_.template(tpl));
            return this;
        },
        'showTopic' : function(){
			this.$el.find('.focus').slideUp("slow", "easeOutQuart").html(_.template(skillsTpl)).slideDown("slow", "easeInQuart");

        } 
    });
});
