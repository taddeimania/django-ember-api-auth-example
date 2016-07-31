import DS from 'ember-data';

export default DS.Model.extend({
  owner: DS.attr('number'),
  body: DS.attr('string'),
});
