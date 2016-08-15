/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'frontend',
    environment: environment,
    rootURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {
    ENV.API_URL = 'https://yourdomain.com'; // Replace this with your own deployed domain
    ENV.APP.API_HOST = 'https://yourdomain.com'; // Replace this with your own deployed domain
  }
  ENV['ember-simple-auth'] = {
    authorizer: 'authorizer:token'
  };
  ENV['ember-simple-auth-token'] = {
    serverTokenEndpoint: '/api/api-token-auth/',
    identificationField: 'username',
    passwordField: 'password',
    tokenPropertyName: 'token',
    authorizationPrefix: 'Token ',
    authorizationHeaderName: 'Authorization',
  };


  return ENV;
};
