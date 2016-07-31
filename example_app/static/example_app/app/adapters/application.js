import DRFAdapter from './drf';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';


export default DRFAdapter.extend(DataAdapterMixin, {
  authorizer: 'authorizer:token',
});
