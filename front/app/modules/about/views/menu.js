/*global define*/

define(['backbone', 'text!modules/about/templates/menu.tpl', 'waypoints', 'easing'], function(Backbone, tpl){
	'use strict';

	return Backbone.View.extend({
		'initialize': function(){
		},
		   'events': {
			   'click .btn-navbar' : 'toggleSidebar',
		   'click .navigation li' : 'goTo'
		   },
		   'render': function(){
			   this.$el.html(_.template(tpl));
			   return this;
		   },
		   'initScroll': function(){
			   /* waypoints ininitalisations */

			   $('section').waypoint(function (direction) {
				   var sectionId = parseInt($(this).attr('id').substr($(this).attr('id').length-1));
				   if (direction === 'down') {
					   $('.navigation li[section="' + sectionId + '"]').addClass('active').siblings().removeClass('active');
				   }
				   else {
					   $('.navigation li[section="' + (sectionId-1) + '"]').addClass('active').siblings().removeClass('active');
				   }
			   });

			   /**/
			   return this;
		   },
		   'toggleSidebar': function(){
			   $('html').toggleClass('expanded');
			   return this;
		   },
		   'goTo': function(evt){
			   var section = evt.currentTarget.getAttribute('section')
			   	   var htmlbody = $('html,body');
				   if (section == 1) {
					   htmlbody.animate({
						   scrollTop: $('#section' + section).offset().top
					   }, 500, 'easeOutQuart');
				   }
				   else {
					   htmlbody.animate({
						   scrollTop: $('#section' + section).offset().top + 70
					   }, 500, 'easeOutQuart');
				   }
		   }
	});
});
