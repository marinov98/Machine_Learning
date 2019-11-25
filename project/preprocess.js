const arff = require('arff');
const nArff = require('node-arff');
const { readFile, writeFile } = require('fs');

readFile('Dataset.Marinov.arff', 'utf8', function(err, content) {
  if (err) return console.error(err);

  const { data } = arff.parse(content);

  for (const instance of data) {
    for (const attribute in instance) {
      if (instance[attribute] === 999 || instance[attribute] === 997) instance[attribute] = '';

      if (attribute.includes('Bereavement_')) {
        if (!instance[attribute]) instance[attribute] = 777;
      }
    }
  }

  writeFile('test.json', data, err => {
    if (err) console.error(err);

    console.log('successfully written!');
  });
});
