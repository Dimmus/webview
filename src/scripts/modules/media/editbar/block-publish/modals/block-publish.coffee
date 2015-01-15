define (require) ->
  BaseView = require('cs!helpers/backbone/views/base')
  template = require('hbs!./block-publish-template')
  _ = require('underscore')
  require('less!./block-publish')

  return class BlockPublishModal extends BaseView
    template: template

    templateHelpers: () ->
      publishBlockers: @publishBlockers(@model)

    initialize: () ->
      @listenTo(@model, 'change:publishBlockers', @render)

    publishBlockers: (model) ->
      book = model.isBook()
      title = model.get('title')
      isPublishable = model.get('isPublishable')
      containedPublishable = model.get('areContainedPublishable')
      contents = model.get('contents')?.models
      publishBlockers = model.get('publishBlockers')
      formatted = []

      if isPublishable is false
        _.each publishBlockers, (blockers) ->
          formatBlockers = blockers.replace('_', ' ')
          formatted.push("#{formatBlockers} in #{title}")

      if book and containedPublishable is false
        _.each contents, (content) ->
          title = content.get('title')
          publishBlockers = content?.get('publishBlockers')
          if publishBlockers isnt undefined and publishBlockers isnt null
            formatBlockers = publishBlockers[0].replace('_', ' ')
            formatted.push("#{formatBlockers} in #{title}")

      return formatted
