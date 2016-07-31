import Ember from 'ember';

export default Ember.Component.extend({
  actions: {
    edit() {
      this.set("editing", true);
    },
    save(secret) {
      secret.save().then(() => {
        this.send("cancel");
      });
    },
    cancel() {
      this.set("editing", false);
    },
    remove(secret) {
      secret.destroyRecord().then(() => {
        this.set("editing", false);
      });
    },
  }
});
