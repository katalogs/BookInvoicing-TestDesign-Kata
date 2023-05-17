module.exports = {
  preset: 'ts-jest',
  clearMocks: true,
  coverageDirectory: "coverage",
  // An array of regexp pattern strings used to skip coverage collection
  coveragePathIgnorePatterns: [
    "<rootDir>/node_modules/(?!@foo)"
  ],
  globals: {
    "ts-jest": {
      "tsconfig": "tsconfig.json",
      "diagnostics": true
    }
  },
  moduleFileExtensions: [
    "ts",
    "tsx",
    "js"
  ],
  // A map from regular expressions to module names that allow to stub out resources with a single module
  moduleNameMapper: {
    "@app/(.*)": "<rootDir>/src/book_invoicing/$1",
  },
  testEnvironment: "node",
  testRegex: "(/tests/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?)$",
  transform: {
    "^.+\\.(ts|tsx)$": "ts-jest"
  },
  transformIgnorePatterns: [
    "<rootDir>/node_modules/(?!@foo)"
  ],
  moduleDirectories: ["node_modules", "src"],
};
