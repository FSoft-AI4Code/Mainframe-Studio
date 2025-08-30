const CracoAlias = require("craco-alias");

module.exports = {
  babel: {
    plugins: [
      [
        "@emotion",
        {
          // sourceMap is on by default but source maps are dead code eliminated in production
          sourceMap: true,
          autoLabel: "dev-only",
          labelFormat: "[local]",
          cssPropOptimization: true
        }
      ]
    ]
  },
  plugins: [
    {
      plugin: CracoAlias,
      options: {
        source: "tsconfig",
        baseUrl: ".",
        tsConfigPath: "./tsconfig.paths.json"
      }
    }
  ]
};
