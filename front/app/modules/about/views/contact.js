/*global define*/

define(['backbone', 'text!modules/about/templates/contact.tpl'], function(Backbone, tpl){
    'use strict';

    return Backbone.View.extend({
		'tagName'	: 'section',
		'className'	: 'section',
		'id': 'section4',
        'initialze'	: function(){
        },
        'render': function(){
            this.$el.html(_.template(tpl));
            return this;
        }
    });
});
