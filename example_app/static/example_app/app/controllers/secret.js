import Ember from 'ember';

export default Ember.Controller.extend({
  session: Ember.inject.service('session'),

  actions: {
    createSecret() {
      let body = this.get("newSecretBody");
      this.store.createRecord("secret", {
        body: body,
        owner: this.get("session.account")
      }).save();
    }
  }
});

