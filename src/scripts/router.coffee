define [
  'backbone'
  'cs!pages/app/app'
], (Backbone, AppView) ->

  return new class Router extends Backbone.Router
    initialize: () ->
      @appView = new AppView()

      # Default Route
      @route '*actions', 'default', () ->
        @appView.render('home')

      @route 'content', 'content', () ->
        @appView.render('content')

      @route 'content/:uuid', 'media', (uuid) ->
        @appView.render('content', {uuid: uuid})
