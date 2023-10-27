import { searchClient } from '@algolia/client-search';
import { liteClient } from 'algoliasearch/lite';

import './app.css';

const client = searchClient('QPBQ67WNIG', 'b590ae1153bf574215ca1605c19eb1fe');
const clientLite = liteClient('QPBQ67WNIG', 'b590ae1153bf574215ca1605c19eb1fe');

client.addAlgoliaAgent('Browser playground', '0.0.1');

const searchButton = document.querySelector('#search');

searchButton?.addEventListener('click', async () => {

  const { results } = await client.searchForHits({
    requests: [
      {
        indexName: 'docsearch',
        query: 'docsearch',
        hitsPerPage: 50,
      },
    ],
  });

  const liteResults = await clientLite.search({
    requests: [
      {
        indexName: 'docsearch',
        query: 'docsearch',
        hitsPerPage: 50,
      },
    ],
  });

  const parent = document.querySelector('#results');

  results[0].hits?.forEach(({ objectID }) => {
    const children = document.createElement('p');
    children.innerHTML = objectID;

    parent?.appendChild(children);
  });

  liteResults.results[0].hits?.forEach(({ objectID }) => {
    const children = document.createElement('p');
    children.innerHTML = objectID + 'LITE';

    parent?.appendChild(children);
  });
});
