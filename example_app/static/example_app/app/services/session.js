import Ember from 'ember';
import DS from 'ember-data';
import SessionService from 'ember-simple-auth/services/session';

export default SessionService.extend({
  store: Ember.inject.service(),

  account: Ember.computed('data.authenticated.account_id', function() {
    const accountId = this.get('data.authenticated.user_id');
    if (!Ember.isEmpty(accountId)) {
      return DS.PromiseObject.create({
        promise: this.get('store').find('user', accountId)
      });
    }
  })
});
